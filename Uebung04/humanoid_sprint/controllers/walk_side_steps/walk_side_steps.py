from controller import Robot
import math

class Sprinter(Robot):
    """Make the NAO robot walk or side-step."""
    
    def initialize(self):
        self.timeStep = int(self.getBasicTimeStep())

        self.RShoulderPitch = self.getDevice('RShoulderPitch')
        self.LShoulderPitch = self.getDevice('LShoulderPitch')
        self.LShoulderRoll = self.getDevice('LShoulderRoll')
        self.RShoulderRoll = self.getDevice('RShoulderRoll')

        
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

    def left(self, x, y, z):
        self.LKneePitch.setPosition ( z      )
        self.LHipPitch.setPosition  (-z/2 + x)
        self.LAnklePitch.setPosition(-z/2 - x)
        self.LHipRoll.setPosition  ( y)
        self.LAnkleRoll.setPosition(-y)

    def right(self, x, y, z):
        self.RKneePitch.setPosition ( z      )
        self.RHipPitch.setPosition  (-z/2 + x)
        self.RAnklePitch.setPosition(-z/2 - x)
        self.RHipRoll.setPosition  ( y)
        self.RAnkleRoll.setPosition(-y)

    def run(self):
        # Parameters defining the geometry and dynamic of the walk.
        #comment out params that should not be used otherwise overwriting of params
        ## 1. slow and steady (01:53:76)
        f            = 4
        robot_height = 0.45
        shift_y      = 0.3
        step_height  = 0.5
        step_length  = 0.2
        arm_swing    = 2.0
        step_side    = 0.2    # lateral step length negative numbers-> mode left positive -> move right
        mode = 'side_step' # 'forward' or 'side_step'

        while self.step(self.timeStep) != -1:
            t = self.getTime() * f
            
            if mode == 'forward':
                # Forward walk logic
                y = math.sin(t) * shift_y
                zL = (math.sin(t)           + 1.0) / 2.0 * step_height + robot_height
                zR = (math.sin(t + math.pi) + 1.0) / 2.0 * step_height + robot_height
                xL = math.cos(t) * step_length
                xR = math.cos(t + math.pi) * step_length
                self.left(xL, y, zL)
                self.right(xR, y, zR)
                self.RShoulderPitch.setPosition(arm_swing * xL + math.pi/2 - 0.1)
                self.LShoulderPitch.setPosition(arm_swing * xR + math.pi/2 - 0.1)

            elif mode == 'side_step':
                x = math.sin(t)*-0.2  # no forward/backward movement try to walk on y-Axis
                yL = math.sin(t) * step_side 
                yR = math.sin(t + math.pi) * step_side
                zL = (math.cos(t)           + 1.0) / 2.0 * step_height + robot_height
                zR = (math.cos(t + math.pi) + 1.0) / 2.0 * step_height + robot_height
                weight_shift = 0.1 * math.sin(t)

                # Feet move side-to-side with addition to weight
                self.left(x, yL+weight_shift, zL)
                self.right(x, yR+weight_shift, zR)

                # Shoulders can stay fixed or counter-rotate
                self.LShoulderRoll.setPosition(0.2 * math.sin(t)+0.3)
                self.RShoulderRoll.setPosition(0.2 * math.sin(t)-0.3)
                
                self.RShoulderPitch.setPosition(math.pi/2)
                self.LShoulderPitch.setPosition(math.pi/2)

controller = Sprinter()
controller.initialize()
controller.run()
