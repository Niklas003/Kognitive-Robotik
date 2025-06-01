import matplotlib.pyplot as plt
import csv

times = []
intensities = []

with open('light_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Time (s)']))
        intensities.append(float(row['Light Intensity']))

plt.plot(times, intensities)
plt.xlabel('Zeit (s)')
plt.ylabel('Lichtintensität')
plt.title('Lichtintensität über Zeit')
plt.grid(True)
plt.show()
