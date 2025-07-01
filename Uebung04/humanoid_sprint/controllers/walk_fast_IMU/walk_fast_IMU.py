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

        # Get IMU components
        # Get Gyrometer
        self.gyro = self.getDevice('gyro')
        # Get Accelerometer
        self.accel = self.getDevice('accelerometer')
        # Enable sensors
        self.gyro.enable(self.timeStep)
        self.accel.enable(self.timeStep)

        
        firstGyroValues, firstAccelValues = controller.checkIMU()
        # create short term menmory for gyro values
        self.gyroMemory = (firstGyroValues, firstGyroValues, firstGyroValues, firstGyroValues, firstGyroValues)

    def updateGyroMemory(self, gyroValues):
        # update the gyro memory with the latest gyro value differences (keep only last 5)
        self.gyroMemory = (self.gyroMemory[1], self.gyroMemory[2], self.gyroMemory[3], self.gyroMemory[4], gyroValues)

    def checkIMU(self):
        gyroValues = self.gyro.getValues()
        accelValues = self.accel.getValues()
        
        # print("Gyro: ", gyroValues)
        # print("Accel: ", accelValues)
        
        return gyroValues, accelValues

    def analyseIMU(self, checkedGyroValues, previousGyroValues):
        # get difference between checkedGyroValues and the previousGyroValues
        gyroValueDiff = [checkedGyroValues[i] - previousGyroValues[i] for i in range(len(checkedGyroValues))]
        
        return gyroValueDiff


    
    def useIMUValues(self, checkedAccelValues, arm_swing, xLeft, xRight):
        # check gyro values for turning direction of the robot

        newestGyroValues = self.gyroMemory[4]
        turnShreshhold = 0.05

        if newestGyroValues[0] < -turnShreshhold:  # turning left
            self.RShoulderPitch.setPosition(arm_swing*xLeft  + math.pi/2 - 0.1)
            self.LShoulderPitch.setPosition(arm_swing*xRight + math.pi/2 - 0.1)

        elif newestGyroValues[0] > turnShreshhold: # turning right
            self.RShoulderPitch.setPosition(arm_swing*xLeft  + math.pi/2 - 0.1)
            self.LShoulderPitch.setPosition(arm_swing*xRight + math.pi/2 - 0.1)
         


         
    
        
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
        
        
    def run(self, previousGyroValues, previousAccelValues):
        
        # Parameters defining the geometry and dynamic of the walk.
        # comment out params that should not be used otherwise overwriting of params
        ## 1. slow and steady (01:53:76)
        f            = 4
        robot_height = 0.5
        shift_y      = 0.3
        step_height  = 0.4
        step_length  = 0.2
        arm_swing    = 2.0

        ## 2. break neck speed (01:18:56)
        f            = 6     # frequency of the oscillation
        robot_height = 0.5   # height of the robot (hips)
        shift_y      = 0.3   # hip sway while moving
        step_height  = 0.4   # height of the step
        step_length  = 0.2   # length of the step
        arm_swing    = 2.0   # arm swing
        
        ## 3. params for fast time (00:17:60)
        # found these params by try and error. Nao seems to shift left and right while running but keeps in lane
        f            = 16   
        robot_height = 0.47  
        shift_y      = 0.1547  
        step_height  = 0.96  
        step_length  = 0.59
        arm_swing    = 0.96

        ## 4. params edited from above, for IMU use (00:16:55)
        # found these params by try and error. Nao shifts lanes to the right but stays on the track. Makiing him pass the course
        # stabillity is achieved, but steering is not actively controlled 
        f            = 15   
        robot_height = 0.47  
        shift_y      = 0.17 
        step_height  = 0.85  
        step_length  = 0.65
        arm_swing    = 0.75

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
            # self.RShoulderPitch.setPosition(arm_swing*xLeft  + math.pi/2 - 0.1)
            # self.LShoulderPitch.setPosition(arm_swing*xRight + math.pi/2 - 0.1)

            checkedGyroValues, checkedAccelValues = self.checkIMU()
            gyroValueDiff = self.analyseIMU(checkedGyroValues, previousGyroValues)
            self.updateGyroMemory(gyroValueDiff)
            self.useIMUValues(checkedAccelValues, arm_swing, xLeft, xRight)
            previousAccelValues = checkedAccelValues
            previousGyroValues = checkedGyroValues

        
        
controller = Sprinter()
controller.initialize()
firstGyroValues, firstAccelValues = controller.checkIMU()
controller.run(firstGyroValues, firstAccelValues)
