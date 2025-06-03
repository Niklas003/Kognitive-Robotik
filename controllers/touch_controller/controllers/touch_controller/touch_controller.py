"""touch_controller controller."""

from controller import Robot
import csv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

joint_names = [
    "base","forearm","rotational_wrist","upperarm","wrist"
]
joints = [robot.getDevice(name) for name in joint_names]

#base: 0 - 6.03
#forearm: 0 - 4.21
#rotational_wrist: -5.8 - 0
#upperarm: -2.44 - 0
#wrist: -4.05 - 0

touch_names = [
    "ts0","ts1","ts2","ts3"
]
touchs = [robot.getDevice(name) for name in touch_names]
for touch in touchs:
    touch.enable(timestep)

for joint in joints:
    joint.setPosition(0.0)
    joint.setVelocity(1.0)

target_positions = [0, 2, 0, 0, 0]

for i in range(len(joints)):
    joints[i].setPosition(target_positions[i])

time = 0

while robot.step(timestep) != -1:
    if time % 100 == 0: 
        for i in range(len(touchs)):
            print(f"{touch_names[i]}: {touchs[i].getValue()/10}")
