import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_cylinder(ax, radius, height, x_offset=0, color='blue', label=None, volume=None, surface_area=None):
    """
    Plots a cylinder in 3D space using matplotlib.
    :param ax: Matplotlib 3D axis.
    :param radius: Radius of the cylinder.
    :param height: Height of the cylinder.
    :param x_offset: Offset along the X-axis for positioning.
    :param color: Color of the cylinder.
    :param label: Label for the cylinder.
    :param volume: Pre-calculated volume of the cylinder.
    :param surface_area: Pre-calculated surface area of the cylinder.
    """
    #mesh grid for the cylinder
    theta = np.linspace(0, 2 * np.pi, 100)
    z = np.linspace(0, height, 100)
    theta, z = np.meshgrid(theta, z)

    #Cylinder coords
    x = radius * np.cos(theta) + x_offset
    y = radius * np.sin(theta)

    #Plot cylindersFace
    ax.plot_surface(x, y, z, color=color, alpha=0.7)

    #Text labels
    ax.text(x_offset, 0, height + 1,
            f"{label}\nRadius = {radius:.2f} cm\nHeight={height:.2f} cm\nVolume ≈ {volume:.2f} cm³\nSurface Area ≈ {surface_area:.2f} cm²",
            color='black', fontsize=10, ha='center')

def visualize_cylinders():
    """
    Visualizes original and optimized cylinders side by side with correct dimensions and surface areas (pre-set values).
    """
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    #Org Cylinder dimensions 
    original_radius = 6 #cm
    original_height = 6.56 #cm
    original_volume = 742.00 #cm³ (ps value)
    original_surface_area = 699.61 # cm² (ps value)

    #Opti cylinder dimensions (fixed lol)
    optimized_radius = 4.91 #cm
    optimized_height = 9.81 #cm
    optimized_volume = 742.00 #cm³ (ps value)
    optimized_surface_area = 604.71 #cm² (ps value)

    #Plot original cylinder (left)
    plot_cylinder(ax,
                  radius=original_radius,
                  height=original_height,
                  x_offset=-10,
                  color='blue',
                  label="Original Cylinder",
                  volume=original_volume,
                  surface_area=original_surface_area)

    #Plot optimized cylinder (right)
    plot_cylinder(ax,
                  radius=optimized_radius,
                  height=optimized_height,
                  x_offset=10,
                  color='green',
                  label="Optimized Cylinder",
                  volume=optimized_volume,
                  surface_area=optimized_surface_area)

    #Labels and Title
    ax.set_title("Cylinder Optimization Comparison", fontsize=16)
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_zlabel("Z-axis")

    #Add annotation for surface area reduction
    surface_area_reduction = (
        (original_surface_area - optimized_surface_area) / original_surface_area * 100
    )
    
    ax.text(0, 0, max(original_height, optimized_height) + 5,
            f"Surface Area Reduction: {surface_area_reduction:.1f}%",
            color='red', fontsize=12, ha='center')

    #Adjust view angle
    ax.view_init(elev=20., azim=-30)

    plt.show()

if __name__ == "__main__":
    visualize_cylinders()
