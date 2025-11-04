
# File: ris_channel.py
# Purpose: Define wireless channel, fading, and RIS reflection logic

import numpy as np
import math
from scipy.constants import speed_of_light
from parameters import freq, noise_power_w, tx_power_w

# Helper Functions 
def path_loss_fspl(d, freq_hz):
    d = np.maximum(d, 1e-6)
    return (4 * np.pi * d * freq_hz / speed_of_light) ** 2

def small_scale_rayleigh(n=1):
    """Complex Rayleigh fading samples"""
    return (np.random.normal(size=n) + 1j * np.random.normal(size=n)) / np.sqrt(2)

def ris_effective_channel(h_tx_ris, h_ris_rx, phase):
    """Combine RIS paths"""
    return np.sum(h_tx_ris * np.exp(1j * phase) * h_ris_rx)

#  Channel Model 
def compute_channel(tx=None, rx=None, elements=None):
    """Return channel between two points or between RIS and node"""
    if elements is None:
        d = np.linalg.norm(tx - rx)
        pl = path_loss_fspl(d, freq)
        return small_scale_rayleigh(1) / np.sqrt(pl)
    elif tx is not None:
        # from TX to each RIS element
        d = np.linalg.norm(elements - tx, axis=1)
        pl = path_loss_fspl(d, freq)
        return small_scale_rayleigh(len(d)) / np.sqrt(pl)
    elif rx is not None:
        # from RIS elements to RX
        d = np.linalg.norm(elements - rx, axis=1)
        pl = path_loss_fspl(d, freq)
        return small_scale_rayleigh(len(d)) / np.sqrt(pl)

# Secrecy Rate 
def secrecy_rate(h_ab, h_ae, h_ar, h_rb, h_re):
    """Compute secrecy rate using co-phase reflection"""
    phase_opt = -np.angle(h_ar * h_rb)
    h_ris_b = ris_effective_channel(h_ar, h_rb, phase_opt)
    h_ris_e = ris_effective_channel(h_ar, h_re, phase_opt)

    H_b = h_ab + h_ris_b
    H_e = h_ae + h_ris_e

    snr_b = tx_power_w * np.abs(H_b) ** 2 / noise_power_w
    snr_e = tx_power_w * np.abs(H_e) ** 2 / noise_power_w

    Rs = max(math.log2(1 + snr_b) - math.log2(1 + snr_e), 0)
    return Rs
