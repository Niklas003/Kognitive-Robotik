from controller import Robot
import csv
import os  

# delete the previous lidar_data.csv file if it exists
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
rightMotor.setVelocity(5)

allRanges = []

time = 0.0
while robot.step(timestep) != -1:
    ranges = lidar.getRangeImage()
    allRanges.append((time,ranges))
    with open('../lidar_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestep'] + [f'Range {i}' for i in range(len(ranges))])
        for entry in allRanges:
            writer.writerow([entry[0]] + list(entry[1]))
    time += timestep

