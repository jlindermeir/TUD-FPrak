import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# import the A-Scans
load_file = lambda schritt : np.loadtxt("data/FD/"+schritt+".txt")
roh = load_file("roh")
apo = load_file("apo")
dechirp = load_file("apo+dechirp")
tukey = load_file("apo+dechirp+tukey")
hann = load_file("apo+dechirp+hann")
rect = load_file("apo+dechirp+rect")
gauss = load_file("apo+dechirp+gauss")

# Pixelbereich des Reflex
reflex = (20, 90)

pixels = np.arange(0, 1025, 1)
ind = np.where((reflex[0] < pixels) & (pixels < reflex[1]))
pixels = pixels[ind]

# Parabelfit
def parabelfit(y_werte):
    reflex = (20, 90)
    pixels = np.arange(0, 1025, 1)
    ind = np.where((reflex[0] < pixels) & (pixels < reflex[1]))
    pixels = pixels[ind]
    
    parabel = lambda x, a, x0, sigma, c : c + a*np.exp(-(x-x0)**2/(2*sigma**2))  

    params, pcov = curve_fit(parabel, pixels, y_werte[ind], p0=[50, 57,3,-15])
    perr_rel = np.sqrt(np.diag(pcov))/params*100
    print(params)
    print(perr_rel)
    a, x0, sigma, c = params
    
    
    fit = parabel(pixels, a, x0, sigma, c)
    
    return (pixels, fit)

#para_apo = parabelfit(apo)
para_dechirp = parabelfit(dechirp)
para_tukey = parabelfit(tukey)
para_hann = parabelfit(hann)
para_rect = parabelfit(rect)
para_gaus = parabelfit(gauss)

# Vergleich verschiedener Prozessierungsschritte
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel("Pixel")
ax.set_ylabel("dB")
ax.plot(pixels, apo[ind],label="Apodisation", ls="--", marker="+")
ax.plot(pixels, dechirp[ind],
        label="Apodisation + Dechirp", ls="--", marker="x")
ax.plot(pixels, tukey[ind],
        label="Apodisation + Dechirp + Tukey", ls="--", marker="o")
ax.grid(which="both")
ax.legend()


# Vergleich verschiedener Fensterfunktionen
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel("Pixel")
ax.set_ylabel("dB")
ax.plot(pixels, hann[ind],
        label="Apodisation + Dechirp + Hann", ls="--", marker="+")
ax.plot(pixels, gauss[ind],
        label="Apodisation + Dechirp + Gauss", ls="--", marker="x")
ax.plot(pixels, tukey[ind],
        label="Apodisation + Dechirp + Tukey", ls="--", marker="o")
ax.plot(pixels, rect[ind],
        label="Apodisation + Dechirp + Rechteck", ls="--", marker="*")
ax.grid(which="both")
ax.legend()

#Plot parabelfit
fig, ax = plt.subplots(figsize=(10,8))
ax.set_xlabel("Pixel")
ax.set_ylabel("dB")
ax.plot(pixels, dechirp[ind],
        label="dechirp", ls="--", marker="+")
ax.plot(para_dechirp[0], para_hann[1],
        label="Parabelfit: Hann")
