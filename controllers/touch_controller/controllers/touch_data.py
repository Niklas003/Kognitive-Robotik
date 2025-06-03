import matplotlib.pyplot as plt
import csv

times = []
force = []

with open('controllers/touch_controller/controllers/touch_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Timestep']))
        force.append(float(row['Force']))

plt.plot(times, force)
plt.xlabel('Timestep')
plt.ylabel('Winkelgeschwindigkeit Z (rad/s)')
plt.title('Winkelgeschwindigkeit über Timesteps')
plt.grid(True)
plt.show()