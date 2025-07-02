from controller import Robot
import math

class Sprinter(Robot):
    def initialize(self):
        self.timeStep = int(self.getBasicTimeStep())

        self.LHipYawPitch = self.getDevice('LHipYawPitch')
        self.RHipYawPitch = self.getDevice('RHipYawPitch')
        self.LHipPitch = self.getDevice('LHipPitch')
        self.LKneePitch = self.getDevice('LKneePitch')
        self.LAnklePitch = self.getDevice('LAnklePitch')
        self.RHipPitch = self.getDevice('RHipPitch')
        self.RKneePitch = self.getDevice('RKneePitch')
        self.RAnklePitch = self.getDevice('RAnklePitch')

    def lift_left_leg(self):
        self.LHipPitch.setPosition(-0.3)
        self.LKneePitch.setPosition(0.6)
        self.LAnklePitch.setPosition(-0.3)

    def lift_right_leg(self):
        self.RHipPitch.setPosition(-0.3)
        self.RKneePitch.setPosition(0.6)
        self.RAnklePitch.setPosition(-0.3)

    def lower_legs(self):
        self.LHipPitch.setPosition(0.0)
        self.LKneePitch.setPosition(0.0)
        self.LAnklePitch.setPosition(0.0)
        self.RHipPitch.setPosition(0.0)
        self.RKneePitch.setPosition(0.0)
        self.RAnklePitch.setPosition(0.0)

    def run(self):
        timer = 0
        state = 0  # 0=lift left, 1=stand, 2=lift right, 3=stand

        while self.step(self.timeStep) != -1:
            timer += 1

            if state == 0:
                # lift left leg and rotate
                self.lift_left_leg()
                self.LHipYawPitch.setPosition(0.3)
                self.RHipYawPitch.setPosition(0.0)
                if timer > 30:
                    timer = 0
                    state = 1

            elif state == 1:
                # place left leg down
                self.lower_legs()
                if timer > 20:
                    timer = 0
                    state = 2

            elif state == 2:
                # lift right leg and rotate
                self.lift_right_leg()
                self.LHipYawPitch.setPosition(0.0)
                self.RHipYawPitch.setPosition(-0.3)
                if timer > 30:
                    timer = 0
                    state = 3

            elif state == 3:
                # place right leg down
                self.lower_legs()
                if timer > 20:
                    timer = 0
                    state = 0  # restart state loop

controller = Sprinter()
controller.initialize()
controller.run()
