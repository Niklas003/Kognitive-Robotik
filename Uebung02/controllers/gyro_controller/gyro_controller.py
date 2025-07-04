from controller import Robot
import random

robot = Robot()
timestep = int(robot.getBasicTimeStep())


gyro = robot.getDevice('gyro')
gyro.enable(timestep)

leftMotor = robot.getDevice("motor.left")
rightMotor = robot.getDevice("motor.right")
leftMotor.setPosition(float('inf'))
rightMotor.setPosition(float('inf'))
rightMotor.setVelocity(5.0)
leftMotor.setVelocity(-6.0)

import csv
#clear file before new values come in
f = open('../gyro_data.csv', "w+")
f.close()
with open('../gyro_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Timestep', 'Angular Velocity X', 'Angular Velocity Y', 'Angular Velocity Z'])
    time = 0.0
    while robot.step(timestep) != -1:
        rightMotorVeloc = random.randint(3, 9)
        leftMotorVeloc = random.randint(3, 9)
        motorDirection = random.choice([-1,1])
        
        rightMotor.setVelocity(motorDirection * rightMotorVeloc)
        leftMotor.setVelocity(-motorDirection * leftMotorVeloc)
        
        angular_velocity = gyro.getValues()
        writer.writerow([time, angular_velocity[0], angular_velocity[1], angular_velocity[2]])
        time += timestep
