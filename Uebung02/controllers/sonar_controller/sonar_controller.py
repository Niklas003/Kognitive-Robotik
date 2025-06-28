from controller import Robot
import random
import csv


robot = Robot()
timestep = int(robot.getBasicTimeStep())


sonar_sensor = robot.getDevice('distance sensor')
sonar_sensor.enable(timestep)

leftMotor = robot.getDevice("motor.left")
rightMotor = robot.getDevice("motor.right")
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
rightMotor.setVelocity(0.5)
leftMotor.setVelocity(0.5)

#clear file before new values come in
f = open('../distance_data.csv', "w+")
f.close()
with open('../distance_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestep', 'Distance'])
    time = 0.0
    while robot.step(timestep) != -1:
        motorVeloc = random.random()
        rightMotor.setVelocity(motorVeloc)
        leftMotor.setVelocity(motorVeloc)
        distance = sonar_sensor.getValue()
        writer.writerow([time, distance])
        print(time, distance)
        time += timestep