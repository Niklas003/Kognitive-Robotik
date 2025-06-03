"""touch_controller controller."""

from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

joint_names = [
    "base","forearm","rotational_wrist","upperarm","wrist"
]

#base: 0 - 6.03
#forearm: 0 - 4.21
#rotational_wrist: -5.8 - 0
#upperarm: -2.44 - 0
#wrist: -4.05 - 0

joints = [robot.getDevice(name) for name in joint_names]

touch1 = robot.getDevice("ts0")
touch1.enable(timestep)

for joint in joints:
    joint.setPosition(0.0)
    joint.setVelocity(1.0)

target_positions = [1, 1, -1, -1, -1]

for i in range(len(joints)):
    joints[i].setPosition(target_positions[i])

time = 0

while robot.step(timestep) != -1: 
    print(touch1.getValue())
