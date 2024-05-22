import numpy as np
import matplotlib.pyplot as plt

# Inputs
# Cell Characteristics
num_cells = 1  # Number of cells in the battery pack
I = 8.96  # Current in A
R_cell = 0.025  # Internal resistance of a single cell in ohms
C_specific = 1800  # Specific heat capacity of a single cell in J/(kg - C)
m_cell = 0.045  # Mass of a single cell in kg
A_cell = 0.01  # Surface area of a single cell in sq meters
T_ambient = 38  # Ambient temperature in deg C

# Simulation Parameters
# Heat transfer constants
emissivity = 0.9  # Emissivity of the cell surface via radiation (dimensionless)
sigma = 5.67e-8  # Stefan-Boltzmann constant in W/(sq. m - K^4)
h_conv = 5  # Approximate convective heat transfer coefficient in W/(sq. m - C)

# Time step and total simulation time
dt = 1  # Time step in seconds
total_time = 1021  # Total simulation time in seconds

# Simulation
# Heat generated by the battery pack
Q_generated = num_cells * I**2 * R_cell  # Heat generated in W

# Total mass and surface area of the battery pack
m_pack = num_cells * m_cell
A_pack = num_cells * A_cell

# Initial temperature of the battery pack
T_pack = T_ambient

# Arrays to store time and temperature data
time = np.arange(0, total_time + dt, dt)
T_history = np.zeros_like(time)
T_history[0] = T_pack

# Simulation loop
for t in range(1, len(time)):
    # Heat loss due to radiation
    Q_radiation = emissivity * sigma * A_pack * ((T_pack + 273.15)**4 - (T_ambient + 273.15)**4)

    # Heat loss due to convection
    Q_convection = h_conv * A_pack * (T_pack - T_ambient)

    # Net heat flow
    Q_net = Q_generated - (Q_radiation + Q_convection)

    # Temperature change
    delta_T = (Q_net * dt) / (m_pack * C_specific)

    # Update temperature
    T_pack = T_pack + delta_T

    # Store temperature
    T_history[t] = T_pack

# Display the final temperature
print(f"The final temperature of the battery pack after {total_time / 3600:.1f} hours is {T_pack:.2f}°C")

# Plotting the temperature rise
plt.figure()
plt.plot(time / 3600, T_history, linewidth=2)
plt.title('Temperature Rise of Battery Pack Over Time')
plt.xlabel('Time (hours)')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
