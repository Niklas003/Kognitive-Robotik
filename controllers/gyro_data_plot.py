import matplotlib.pyplot as plt
import csv

times = []
angular_velocity_z = []

with open('gyro_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Timestep']))
        angular_velocity_z.append(float(row['Angular Velocity Z']))
        angular_velocity_x.append(float(row['Angular Velocity X']))

plt.plot(times, angular_velocity_z, angular_velocity_x)
plt.xlabel('Timestep')
plt.ylabel('Winkelgeschwindigkeit Z (rad/s)')
plt.title('Winkelgeschwindigkeit über Timesteps')
plt.grid(True)
plt.show()
