import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import csv
import numpy as np

# Lidar parameters (set these according to your Webots Lidar settings)
fov = 1.5708 # np.pi/2     

times = []
ranges = []

with open('controllers/lidar_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Timestep']))
        ranges.append([float(row[f'Range {i}']) for i in range(len(row) - 1)])



# Initial scan
scan_idx = 0
scan = ranges[scan_idx]

num_rays = len(scan)  # Ensure num_rays matches the number of ranges in the scan

angles = np.linspace(-fov/2, fov/2, num_rays)

x = [r * np.cos(a) for r, a in zip(scan, angles)]
y = [r * np.sin(a) for r, a in zip(scan, angles)]
colors = ['blue'] * num_rays  # First scan: all blue

fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(bottom=0.2)
sc = ax.scatter(x, y, s=10, c=colors)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
title = ax.set_title(f'Lidar Scan at t={times[scan_idx]:.2f}')
ax.axis('equal')
ax.grid(True)

# Slider
ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, 'Timestep', 0, len(ranges)-1, valinit=0, valstep=1)

def update(val):
    idx = int(slider.val)
    scan = ranges[idx]
    x = [r * np.cos(a) for r, a in zip(scan, angles)]
    y = [r * np.sin(a) for r, a in zip(scan, angles)]
    if idx > 0:
        prev_scan = ranges[idx-1]
        # Use a small epsilon to avoid floating point issues
        epsilon = 1e-6
        colors = ['red' if abs(scan[i] - prev_scan[i]) > epsilon else 'blue' for i in range(num_rays)]
    else:
        colors = ['blue'] * num_rays
    sc.set_offsets(np.c_[x, y])
    sc.set_color(colors)
    title.set_text(f'Lidar Scan at t={times[idx]:.2f}')
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()