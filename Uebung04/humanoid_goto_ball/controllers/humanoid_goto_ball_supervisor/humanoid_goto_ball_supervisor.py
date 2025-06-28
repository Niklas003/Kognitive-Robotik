"""visual tracking benchmark supervisor controller.

Manage the benchmark simulation execution and evaluate the performance
of the robot controller.
"""

from controller import Supervisor

#import numpy as np
import math
import sys
import random
import argparse


# simple mathematical function in 3D
# to safe dependency to numpy ;)
def dot(v1, v2):
    """Compute the dot product of 3D vectors v1 and v2."""
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def norm2(v):
    """Compute euclidean norm for a vector"""
    return math.sqrt(dot(v, v))

def normalize(v):
    """Return normalized 3D vector v."""
    det = norm2(v)
    return [v[0] / det, v[1] / det, v[2] / det]

def subtract(a, b):
  return [a[0]-b[0], a[1]-b[1], a[2]-b[2]]
  
def add(a, b):
  return [a[0]+b[0], a[1]+b[1], a[2]+b[2]]
  
'''
R[0] R[1] R[2]
R[3] R[4] R[5]
R[6] R[7] R[8]
'''

def multiply(R, v):
  return [ R[0]*v[0] + R[1]*v[1] + R[2]*v[2], R[3]*v[0] + R[4]*v[1] + R[5]*v[2], R[6]*v[0] + R[7]*v[1] + R[8]*v[2]]  
  
def transpose(R):
  return [ R[0], R[3], R[6],  R[1], R[4], R[7],  R[2], R[5], R[8] ]
  
# apply a coordinate transformation: R*x+t
def transform3(R, t, x):
  return add(multiply(R, x), t)
  

# apply the inverse coordinate transformation: R^T*(x-t)
def transform_inv3(R, t, x):
  return multiply(transpose(R), subtract(x, t))
  
# TODO: remove magic numbers!!!
def globalToImage(R, t, openingAngleWidth, p):
  
  #R = camera_node.getOrientation()
  #t = camera_node.getPosition()
  
  # transform ball position to camera coordinates
  v = transform_inv3(R, t, p)
  
  a = openingAngleWidth
  x = 320 - (v[0] / v[2]) * (320.0 / math.tan(a*0.5))  # tan
  y = 240 + (v[1] / v[2]) * (320.0 / math.tan(a*0.5))
  
  # NOTE: v[2] < 0 => ball is in front of the camera, not behind 
  if x >= 0 and y >= 0 and x < 640 and y < 480 and v[2] < 0:
    return v#[x,y]
  else:
    return None


class MovingTarget():
    """Class used to manage the move of the target object."""

    # parameters set to instant teleportation
    SPEED = 1000           # target object speed in meter/milliseconds
    ROTATION_SPEED = 1000  # target object speed in meter/milliseconds

    def __init__(self, node, bounds):
        """Default constructor.

        node: target object node.
        """
        self.x_min, self.x_max, self.y_min, self.y_max = bounds

        # Get fields.
        self.node = node
        self.translationField = self.node.getField('translation')
        self.rotationField = self.node.getField('rotation')

        self.targetPosition = None


    def nextTargetPoint(self):
        return (
            self.x_min + random.random()*(self.x_max - self.x_min), 
            self.y_min + random.random()*(self.y_max - self.y_min),
            self.node.getPosition()[2]) # keep z 

    def move(self, timestep):
        if self.targetPosition is None:
            self.targetPosition = self.nextTargetPoint()

        translation = self.node.getPosition()
        rotationAngle = self.node.getOrientation()[3]

        direction = subtract(self.targetPosition, translation)
        distance = norm2(direction)

        maxStep = MovingTarget.SPEED * timestep

        # reached target, generate new
        if distance < maxStep:
            self.targetPosition = self.nextTargetPoint() # generate a new target
            translation[0] += direction[0]
            translation[1] += direction[1]
        else:
            targetAngle = math.atan2(direction[1], direction[0]) - rotationAngle
            
            # limit the rotation speed
            if abs(targetAngle) > MovingTarget.ROTATION_SPEED:
                rotationStep = targetAngle / abs(targetAngle) * MovingTarget.ROTATION_SPEED
            else:
                rotationStep = targetAngle
            
            rotationAngle += rotationStep

            # limit the moving speed
            factor = maxStep / distance
            translation[0] += direction[0] * factor
            translation[1] += direction[1] * factor

        # apply translation
        self.translationField.setSFVec3f(translation)

        # apply rotation
        self.rotationField.setSFRotation([0.0, 0.0, 1.0, rotationAngle])

        return True


    def check_reached(self, robot):

        R = robot.getOrientation()
        t = robot.getPosition()

        p = self.node.getPosition()
        
        # transform object position to robot coordinates
        p_local = transform_inv3(R, t, p)
    
        
        if p_local[0] < 0.3 and p_local[0] > 0.1 and p_local[1] < 0.15 and p_local[1] > -0.15:
           return True
        else:
            return False


# Create the Supervisor instance.
robot = Supervisor()

# Get the time step of the current world.
timestep = int(robot.getBasicTimeStep() * 4)

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("--bounds", help="x_min x_max y_min y_max", nargs = 4, type=float, default=[1.5, 4.0, -3.0, 3.0])
parser.add_argument("--time", help="in s", type=float)

args = parser.parse_args()

x_min, x_max, y_min, y_max = args.bounds
#print(args.bounds)
#print(args.time)

# get reference to myself
targetName = robot.getFromDef('OBSERVER').getField("target").getSFString();
print(f"[Observer] observing {targetName}");

# Create instance of moving target object.
target = MovingTarget(robot.getFromDef(targetName), args.bounds)

#robotHead = robot.getFromDef('HEAD_CAM')

nao_robot     = robot.getFromDef('NAO_ROBOT')
camera_top    = robot.getFromDef('NAO_ROBOT.HEAD.CAM_TOP')
camera_bottom = robot.getFromDef('NAO_ROBOT.HEAD.CAM_BOTTOM')

camera_fov    = nao_robot.getField("cameraFieldOfView").getSFFloat()
camera_width  = nao_robot.getField("cameraWidth").getSFInt32()
camera_height = nao_robot.getField("cameraHeight").getSFInt32()
#print(fov, camera_width, camera_height)


hitsCount = 0
stepsCount = 5 # max rechable points
t0 = 0
time_begin = None
while robot.step(timestep) != -1:

    if robot.getTime() < 2.0:
        continue

    if time_begin is None:
        time_begin = robot.getTime()
        print("BEGIN")

    t = robot.getTime() - time_begin


    if target.check_reached(nao_robot):
        # update targers location
        target.move(timestep)
        hitsCount += 1
        
        # generate a status message
        score = int(float(hitsCount) / float(stepsCount) * 100.0 + 0.5)
        message = "[{:.2f}] Score: {:d} / {:d} => {:d}% ".format(t, hitsCount, stepsCount, score)

        print(message)
        
        
    if t >= args.time or hitsCount >= stepsCount:
        print("FINISHED:")
        print("-"*20)
        print(message)
        break

#robot.simulationSetMode(Supervisor.SIMULATION_MODE_PAUSE)
