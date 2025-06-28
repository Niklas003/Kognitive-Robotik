import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import csv
import numpy as np

fov = 1.5708  
v_fov = 0.703125 
num_layers = 6  

times = []
ranges = []

with open('controllers/lidar_data.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        times.append(float(row['Timestep']))
        scan_flat = []
        for i in range(len(row) - 1):
            val = row[f'Range {i}']
            if val == 'inf':
                scan_flat.append(1.0)
            else:
                scan_flat.append(float(val))
        num_rays = int(len(scan_flat) / num_layers)
        scan = np.array(scan_flat).reshape((num_layers, num_rays))
        ranges.append(scan)

scan_idx = 0
scan = ranges[scan_idx]
num_layers, num_rays = scan.shape

h_angles = np.linspace(-fov/2, fov/2, num_rays)
v_angles = np.linspace(-v_fov/2, v_fov/2, num_layers)

H, V = np.meshgrid(h_angles, v_angles)

def get_xyz(scan):
    X = scan * np.cos(V) * np.cos(H)
    Y = scan * np.cos(V) * np.sin(H)
    Z = scan * np.sin(V)
    return X, Y, Z

X, Y, Z = get_xyz(scan)

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)

colors = ['blue'] * (num_layers * num_rays)
sc = ax.scatter(X, Y, Z, s=10, c=colors)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_xlim([0, 1])  
ax.set_ylim([-1, 1]) 
ax.set_zlim([-1, 1]) 
title = ax.set_title(f'Lidar 3D Scan at t={times[scan_idx]:.2f}')
ax.grid(True)

ax_slider = plt.axes([0.2, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, 'Timestep', 0, len(ranges)-1, valinit=0, valstep=1)

def update(val):
    idx = int(slider.val)
    scan = ranges[idx]
    X, Y, Z = get_xyz(scan)
    flat_scan = scan.flatten()
    colors = ['blue' if r == 1.0 else 'red' for r in flat_scan]
    sc._offsets3d = (X.flatten(), Y.flatten(), Z.flatten())
    sc.set_color(colors)
    title.set_text(f'Lidar 3D Scan at t={times[idx]:.2f}')
    fig.canvas.draw_idle()

slider.on_changed(update)
plt.show()