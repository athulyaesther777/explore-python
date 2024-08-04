import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


# Function to draw a single rose petal
def draw_petal(ax, center, size, angle):
    t = np.linspace(0, 2 * np.pi, 100)
    x_vals = size * (16 * np.sin(t) ** 3)
    y_vals = size * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))

    # Rotate and translate the petal
    x_rot = np.cos(angle) * x_vals - np.sin(angle) * y_vals
    y_rot = np.sin(angle) * x_vals + np.cos(angle) * y_vals

    x_final = x_rot + center[0]
    y_final = y_rot + center[1]

    ax.fill(x_final, y_final, color='red', alpha=0.8)


# Function to draw a complete rose
def draw_rose(ax, center, petal_size, petal_count):
    for i in range(petal_count):
        angle = 2 * np.pi / petal_count * i
        draw_petal(ax, center, petal_size, angle)


# Function to draw the stem
def draw_stem(ax, center, height):
    ax.plot([center[0], center[0]], [center[1] - height, center[1]], color='green', lw=2)


# Function to draw the leaves
def draw_leaf(ax, center, size, angle_offset):
    t = np.linspace(0, 2 * np.pi, 100)
    x_vals = size * (2 * np.sin(t))
    y_vals = size * (np.cos(t) - 1)

    # Rotate and translate the leaf
    x_rot = np.cos(angle_offset) * x_vals - np.sin(angle_offset) * y_vals
    y_rot = np.sin(angle_offset) * x_vals + np.cos(angle_offset) * y_vals

    x_final = x_rot + center[0]
    y_final = y_rot + center[1]

    ax.fill(x_final, y_final, color='green', alpha=0.8)


# Initialize the plot
fig, ax = plt.subplots()
ax.set_xlim(0, 8)
ax.set_ylim(0, 10)
ax.set_facecolor('black')
ax.set_aspect('equal')


# Animation function
def animate(frame):
    ax.clear()
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 10)
    ax.set_facecolor('black')

    # Flower properties
    petal_size = frame / 40  # Smaller petal size for smaller flower
    petal_count = 6  # Number of petals
    center = (4, 5)

    # Draw stem and leaves
    draw_stem(ax, center, 1.5)  # Smaller stem height
    draw_leaf(ax, (center[0] - 0.75, center[1] - 1.5), 0.75, np.pi / 4)  # Left leaf
    draw_leaf(ax, (center[0] + 0.75, center[1] - 1.5), 0.75, -np.pi / 4)  # Right leaf

    # Draw growing rose
    draw_rose(ax, center, petal_size, petal_count)


# Create animation
ani = animation.FuncAnimation(fig, animate, frames=60, interval=200, repeat=False)

# Display the plot
plt.show()
