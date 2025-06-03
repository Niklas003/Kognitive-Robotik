from controller import Robot
import csv
import os

if os.path.exists('../lidar_data.csv'):
    os.remove('../lidar_data.csv')

robot = Robot()
timestep = int(robot.getBasicTimeStep())

lidar = robot.getDevice('lidar')
lidar.enable(timestep)

leftMotor = robot.getDevice("motor.left")
rightMotor = robot.getDevice("motor.right")
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))

leftMotor.setVelocity(5)
rightMotor.setVelocity(-5)

allRanges = []

print("Starting Lidar data collection...")
num_layers = lidar.getNumberOfLayers()
num_rays = lidar.getHorizontalResolution()
print(f"layers: {num_layers}")
print(f"horizontal resolution: {num_rays}")
print(f"fov: {lidar.getFov()}")
print(f"vertical fov: {lidar.getVerticalFov()}")
print(f"min range: {lidar.getMinRange()}")
print(f"max range: {lidar.getMaxRange()}")

time = 0.0
while robot.step(timestep) != -1:
    ranges = lidar.getRangeImageArray()
    if len(ranges) == num_layers and all(len(row) == num_rays for row in ranges):
        allRanges.append((time, ranges))
    else:
        print(f"Warning: Skipped malformed scan at t={time:.2f}")
    time += timestep

with open('../lidar_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestep'] + [f'Range {i}' for i in range(num_layers * num_rays)])
    for entry in allRanges:
        flat_ranges = [item for sublist in entry[1] for item in sublist]
        writer.writerow([entry[0]] + flat_ranges)