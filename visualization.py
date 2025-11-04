
# File: visualization.py
# Purpose: Create all plots (heatmap, cross-section, diagram)

import matplotlib.pyplot as plt
import numpy as np

def plot_heatmap(X, Y, secrecy_map, alice, bob, eve, best_pos, outdir="plots"):
    plt.figure(figsize=(8,6))
    plt.contourf(X, Y, secrecy_map, levels=40)
    plt.colorbar(label="Secrecy Rate (bits/s/Hz)")
    plt.scatter(alice[0], alice[1], marker='^', label='Alice (BS)')
    plt.scatter(bob[0], bob[1], marker='o', label='Bob (Legit)')
    plt.scatter(eve[0], eve[1], marker='x', label='Eve (Eavesdropper)')
    plt.scatter(best_pos[0], best_pos[1], marker='s', label='Best UAV')
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title("Secrecy Rate Heatmap for UAV-RIS")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{outdir}/heatmap.png", dpi=150, bbox_inches="tight")
    plt.show()

def plot_cross_section(x_vals, secrecy_map, y_vals, best_pos, best_rs, outdir="plots"):
    mid_row = np.argmin(np.abs(y_vals))
    plt.figure(figsize=(8,4))
    plt.plot(x_vals, secrecy_map[mid_row, :])
    plt.scatter(best_pos[0], best_rs, color='r', label='Best UAV Position')
    plt.title("Secrecy Rate vs UAV X Position")
    plt.xlabel("UAV X (m)")
    plt.ylabel("Secrecy Rate (bits/s/Hz)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{outdir}/cross_section.png", dpi=150, bbox_inches="tight")
    plt.show()

def plot_diagram(alice, bob, eve, best_pos, outdir="plots"):
    plt.figure(figsize=(8,6))
    plt.scatter(alice[0], alice[1], marker='^', label='Alice')
    plt.scatter(bob[0], bob[1], marker='o', label='Bob')
    plt.scatter(eve[0], eve[1], marker='x', label='Eve')
    plt.scatter(best_pos[0], best_pos[1], marker='s', label='UAV (RIS)')
    plt.arrow(alice[0], alice[1], best_pos[0]-alice[0], best_pos[1]-alice[1],
              head_width=3, length_includes_head=True)
    plt.arrow(best_pos[0], best_pos[1], bob[0]-best_pos[0], bob[1]-best_pos[1],
              head_width=3, length_includes_head=True)
    plt.arrow(alice[0], alice[1], bob[0]-alice[0], bob[1]-alice[1],
              head_width=3, linestyle='--', length_includes_head=True)
    plt.xlabel("X (m)")
    plt.ylabel("Y (m)")
    plt.title("Alice → UAV(RIS) → Bob Communication Path")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{outdir}/diagram.png", dpi=150, bbox_inches="tight")
    plt.show()
