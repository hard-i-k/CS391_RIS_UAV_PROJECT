
# File: main_simulation.py
# Purpose: Run the RIS-mounted UAV-assisted secure communication simulation

import numpy as np
import os
from parameters import uav_altitude
from environment import tx_station, legit_user, intruder, X, Y, x_vals, y_vals, ris_local
from ris_channel import compute_channel, secrecy_rate
from visualization import plot_heatmap, plot_cross_section, plot_diagram


# Simulation Configuration

np.random.seed(2)                 # Reproducibility
outdir = "plots"
os.makedirs(outdir, exist_ok=True)

# Initialize secrecy rate map and tracking variables
secrecy_map = np.zeros_like(X)
best_rs, best_pos = -1, None

# Main Simulation Loop

for i in range(X.shape[0]):
    for j in range(X.shape[1]):
        # UAV position at this grid point
        uav = np.array([X[i, j], Y[i, j], uav_altitude])
        ris_world = ris_local + uav

        # Channel Computations
        h_tx_legit = compute_channel(tx=tx_station, rx=legit_user)
        h_tx_intr = compute_channel(tx=tx_station, rx=intruder)
        h_tx_ris  = compute_channel(tx=tx_station, elements=ris_world)
        h_ris_legit = compute_channel(rx=legit_user, elements=ris_world)
        h_ris_intr  = compute_channel(rx=intruder, elements=ris_world)

        # Compute Secrecy Rate for this UAV position
        Rs = secrecy_rate(h_tx_legit, h_tx_intr, h_tx_ris, h_ris_legit, h_ris_intr)
        secrecy_map[i, j] = Rs

        # Update best UAV position
        if Rs > best_rs:
            best_rs, best_pos = Rs, uav.copy()


# Visualization

plot_heatmap(X, Y, secrecy_map, tx_station, legit_user, intruder, best_pos, outdir)
plot_cross_section(x_vals, secrecy_map, y_vals, best_pos, best_rs, outdir)
plot_diagram(tx_station, legit_user, intruder, best_pos, outdir)

# Final Results

print("\n Simulation Complete")
print(f"Optimal UAV Position (x, y, z): {best_pos}")
print(f"Maximum Secrecy Rate: {best_rs:.4f} bits/s/Hz")
