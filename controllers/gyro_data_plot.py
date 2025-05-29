import matplotlib.pyplot as plt
import csv

times = []
angular_velocity_z = []

with open('gyro_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Time (s)']))
        angular_velocity_z.append(float(row['Angular Velocity Z']))

plt.plot(times, angular_velocity_z)
plt.xlabel('Zeit (s)')
plt.ylabel('Winkelgeschwindigkeit Z (rad/s)')
plt.title('Winkelgeschwindigkeit über Zeit')
plt.grid(True)
plt.show()
