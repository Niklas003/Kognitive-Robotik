from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())


light_sensor = robot.getDevice('light sensor')
light_sensor.enable(timestep)

leftMotor = robot.getDevice("motor.left")
rightMotor = robot.getDevice("motor.right")
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
rightMotor.setVelocity(0.5)
leftMotor.setVelocity(0.5)

import csv
#clear file before new values come in
f = open('../light_data.csv', "w+")
f.close()
with open('../light_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Time (s)', 'Light Intensity'])
    time = 0.0
    while robot.step(timestep) != -1:
        intensity = light_sensor.getValue()
        writer.writerow([time, intensity])
        time += timestep / 1000.0
