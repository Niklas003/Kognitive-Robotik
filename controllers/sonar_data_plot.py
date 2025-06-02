import matplotlib.pyplot as plt
import csv

times = []
distances = []

with open('distance_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Timestep']))
        distances.append(float(row['Distance']))

plt.plot(times, distances)
plt.xlabel('Timesteps')
plt.ylabel('Entfernung (raw)')
plt.title('Entfernungsmessung über Zeit mittels Sonar')
plt.grid(True)
plt.show()
