
# File: parameters.py
# Purpose: Store all system-wide constants and parameters

from scipy.constants import speed_of_light

# Frequency and physical constants
freq = 3e9                        # 3 GHz carrier frequency
wavelength = speed_of_light / freq
bandwidth = 1e6                   # 1 MHz
noise_figure_db = 7.0

# Transmit power
tx_power_dbm = 30                 # 1 Watt
tx_power_w = 10 ** ((tx_power_dbm - 30) / 10)

# Thermal noise calculation
k_b = 1.38064852e-23
T0 = 290.0
noise_power_w = k_b * T0 * bandwidth * 10 ** (noise_figure_db / 10)

# RIS parameters
N_elements = 64                   # 8x8 RIS elements
element_spacing = wavelength / 2  # element spacing

# UAV settings
uav_altitude = 60.0               # meters
