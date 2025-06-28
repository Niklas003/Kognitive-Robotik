# A simple open loop controller generating walking behavior 
# on a humanoid robot NAO.
#
# We use the asumption of 'parallel kinematics', i.e., feet are 
# kept parallel to the ground, to simplify kinematic calculations.
# The motion dynamics is generated with sin/cos based oscillations.


from controller import Robot
import math

class Sprinter(Robot):
    """Make the NAO robot run as fast as possible."""

    def initialize(self):
        
        """Get device pointers, enable sensors and set robot initial pose."""
        
        # This is the time step (ms)
        self.timeStep = int(self.getBasicTimeStep())
        
        # Get pointers to the shoulder motors.
        self.RShoulderPitch = self.getDevice('RShoulderPitch')
        self.LShoulderPitch = self.getDevice('LShoulderPitch')
        
        # Get pointers to the 12 motors of the legs
        self.RHipYawPitch = self.getDevice('RHipYawPitch')
        self.LHipYawPitch = self.getDevice('LHipYawPitch')
        self.RHipRoll     = self.getDevice('RHipRoll')
        self.LHipRoll     = self.getDevice('LHipRoll')
        self.RHipPitch    = self.getDevice('RHipPitch')
        self.LHipPitch    = self.getDevice('LHipPitch')
        self.RKneePitch   = self.getDevice('RKneePitch')
        self.LKneePitch   = self.getDevice('LKneePitch')
        self.RAnklePitch  = self.getDevice('RAnklePitch')
        self.LAnklePitch  = self.getDevice('LAnklePitch')
        self.RAnkleRoll   = self.getDevice('RAnkleRoll')
        self.LAnkleRoll   = self.getDevice('LAnkleRoll')
        
        
    # move the left foot (keep the foot paralell to the ground)
    def left(self, x, y, z):
        # x, z 
        self.LKneePitch.setPosition ( z      )
        self.LHipPitch.setPosition  (-z/2 + x)
        self.LAnklePitch.setPosition(-z/2 - x)
        
        # y
        self.LHipRoll.setPosition  ( y)
        self.LAnkleRoll.setPosition(-y)
    
    
    # move the right foot (keep the foot paralell to the ground)
    def right(self, x, y, z):
        # x, z
        self.RKneePitch.setPosition ( z      )
        self.RHipPitch.setPosition  (-z/2 + x)
        self.RAnklePitch.setPosition(-z/2 - x)
        
        # y
        self.RHipRoll.setPosition  ( y)
        self.RAnkleRoll.setPosition(-y)
        
        
    def run(self):
        
        # Parameters defining the geometry and dynamic of the walk.
        
        ## 1. slow and steady
        f            = 4
        robot_height = 0.5
        shift_y      = 0.3
        step_height  = 0.4
        step_length  = 0.2
        arm_swing    = 2.0 
        
        while self.step(self.timeStep) != -1:
            
            # scale the time to modulate the frequency of the walk
            t = self.getTime()*f
            
            # y
            yLeftRight = math.sin(t)*shift_y
            
            # z
            zLeft  = (math.sin(t)           + 1.0) / 2.0 * step_height + robot_height
            zRight = (math.sin(t + math.pi) + 1.0) / 2.0 * step_height + robot_height

            # x
            # math.sin(t + math.pi/2) = math.cos(t)
            xLeft  = math.cos(t          )*step_length
            xRight = math.cos(t + math.pi)*step_length
            
            # apply
            self.left(  xLeft, yLeftRight, zLeft )
            self.right(xRight, yLeftRight, zRight)
            
            # move shoulders to stabilize steps
            self.RShoulderPitch.setPosition(arm_swing*xLeft  + math.pi/2 - 0.1)
            self.LShoulderPitch.setPosition(arm_swing*xRight + math.pi/2 - 0.1)
        
        
controller = Sprinter()
controller.initialize()
controller.run()
