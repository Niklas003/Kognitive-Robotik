"""touch_controller controller."""

from controller import Robot
import csv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

joint_names = [
    "base", "forearm", "rotational_wrist", "upperarm", "wrist"
]
joints = [robot.getDevice(name) for name in joint_names]
sensors = []

for joint in joints:
    sensor = joint.getPositionSensor()
    sensor.enable(timestep)
    sensors.append(sensor)

touch_names = ["ts0", "ts1", "ts2", "ts3"]
touchs = [robot.getDevice(name) for name in touch_names]
for touch in touchs:
    touch.enable(timestep)

position_sequence = [
    [0.0001, 2, -0.0001, -2, -0.0001],  # pre_rigid
    [0.0001, 2, -0.0001, -2, -2],       # rigid
    [3, 2, -0.0001, -2, -0.0001],       # pre_slider
    [3, 2, -0.0001, -2, -2]             # slider
]

wait_time_ms = 2000
delay_steps = int(wait_time_ms / timestep)

current_target_index = 0
current_target = position_sequence[current_target_index]

for i in range(len(joints)):
    joints[i].setPosition(current_target[i])
print(f"Moving to position {current_target_index}: {current_target}")

start_step = 0
time_counter = 0

with open('../touch_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestep', 'Force'])

    while robot.step(timestep) != -1:
        force_value = touchs[1].getValue() / 10
        writer.writerow([time_counter, force_value])
        time_counter += 1

        if time_counter - start_step >= delay_steps:
            current_target_index += 1
            if current_target_index < len(position_sequence):
                current_target = position_sequence[current_target_index]
                for i in range(len(joints)):
                    joints[i].setPosition(current_target[i])
                print(f"Moving to position {current_target_index}: {current_target}")
                start_step = time_counter
            else:
                print("All positions reached.")
                break
