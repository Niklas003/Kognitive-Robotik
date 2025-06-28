
from controller import Robot
import math

class Sprinter(Robot):

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
        
        
    def run(self):
        
        f            = 4
        robot_height = 1.1
        
        while self.step(self.timeStep) != -1:
            
            # scale the time to modulate the frequency of the walk
            t = self.getTime()*f
            
            # y
            z = (math.sin(t) + 1.0) / 2.0 * robot_height
            
            #x = math.sin(t) * 0.1
            y = math.cos(t) * 0.1
            
            #z = 0
            
            x = 0
            
            # z 
            self.LKneePitch.setPosition ( z   )
            self.LHipPitch.setPosition  (-z/2 + x )
            self.LAnklePitch.setPosition(-z/2 - x )
            
            
            # z
            self.RKneePitch.setPosition ( z   )
            self.RHipPitch.setPosition  (-z/2 + x)
            self.RAnklePitch.setPosition(-z/2 - x)
        
        
            #y = 0#0.2
            # y
            self.RHipRoll.setPosition  (y )
            self.RAnkleRoll.setPosition(-y )
            
            self.LHipRoll.setPosition  (y )
            self.LAnkleRoll.setPosition(-y )
            
        
controller = Sprinter()
controller.initialize()
controller.run()
