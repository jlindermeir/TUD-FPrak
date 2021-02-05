import numpy as np
import matplotlib.pyplot as plt

# import the A-Scans
load_file = lambda schritt : np.loadtxt(schritt+".txt")
roh = load_file("roh")
apo = load_file("apo")
dechirp = load_file("apo+dechirp")
tukey = load_file("apo+dechirp+tukey")
hann = load_file("apo+dechirp+hann")
rect = load_file("apo+dechirp+rect")
gauss = load_file("apo+dechirp+gauss")

# Pixelbereich des Reflex
reflex = (20, 90)

fig, ax = plt.subplots(figsize=(10,8))
pixels = np.arange(0, 1025, 1)
ind = np.where((reflex[0] < pixels) & (pixels < reflex[1]))
pixels = pixels[ind]
ax.set_xlabel("Pixel")
ax.set_ylabel("dB")
ax.legend()

"""
# Vergleich verschiedener Prozessierungsschritte
ax.plot(pixels, load_file("apo")[ind],label="Apodisation", ls="--", marker="+")
ax.plot(pixels, load_file("apo+dechirp")[ind],
        label="Apodisation + Dechirp", ls="--", marker="x")
ax.plot(pixels, load_file("apo+dechirp+tukey")[ind],
        label="Apodisation + Dechirp + Tukey", ls="--", marker="o")
ax.grid(which="both")
ax.legend()
"""

# Vergleich verschiedener Fensterfunktionen
ax.plot(pixels, load_file("apo+dechirp+hann")[ind],
        label="Apodisation + Dechirp + Hann", ls="--", marker="+")
ax.plot(pixels, load_file("apo+dechirp+gauss")[ind],
        label="Apodisation + Dechirp + Gauss", ls="--", marker="x")
ax.plot(pixels, load_file("apo+dechirp+tukey")[ind],
        label="Apodisation + Dechirp + Tukey", ls="--", marker="o")
ax.plot(pixels, load_file("apo+dechirp+rect")[ind],
        label="Apodisation + Dechirp + Rechteck", ls="--", marker="*")
ax.grid(which="both")
ax.legend()