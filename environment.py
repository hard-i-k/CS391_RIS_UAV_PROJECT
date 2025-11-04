# ------------------------------------------------------------
# File: environment.py
# Purpose: Define environment layout (Alice, Bob, Eve, UAV grid)
# ------------------------------------------------------------
import numpy as np
from parameters import N_elements, element_spacing, uav_altitude

# Define fixed node positions
alice_pos = np.array([0.0, 0.0, 10.0])     # Base station
bob_pos = np.array([150.0, 0.0, 1.5])      # Legitimate user
eve_pos = np.array([120.0, 40.0, 1.5])     # Eavesdropper

# UAV horizontal grid (search area)
x_vals = np.linspace(20, 260, 61)
y_vals = np.linspace(-80, 80, 41)
X, Y = np.meshgrid(x_vals, y_vals)

# RIS element positions (local coordinates)
side = int(np.sqrt(N_elements))
x_ris = (np.arange(side) - (side - 1) / 2) * element_spacing
y_ris = (np.arange(side) - (side - 1) / 2) * element_spacing
xr, yr = np.meshgrid(x_ris, y_ris)
ris_local = np.stack([xr.ravel(), yr.ravel(), np.zeros(N_elements)], axis=1)
#
# Compatibility aliases expected by other modules (e.g. main_simulation.py).
# The original variable names were alice_pos, bob_pos, eve_pos; older code
# imports tx_station, legit_user, intruder — provide aliases to avoid import errors.
tx_station = alice_pos
legit_user = bob_pos
intruder = eve_pos

# Expose commonly used names in module namespace
__all__ = [
	"tx_station", "legit_user", "intruder",
	"X", "Y", "x_vals", "y_vals", "ris_local",
]
