import numpy as np
import fea
import matplotlib.pyplot as plt

sampleRate = 44100
frequency = 50
length = 1

t = np.linspace(0, length, sampleRate * length)
y = np.sin(frequency * 2 * np.pi * t)
y = np.pad(y,(10000,10000),'constant')

win = fea.Win(y,"ham") # Create Window
eng = fea.Norm_Short_Time_Energ(y,win)
mag = fea.Norm_Short_Time_Mag(y,win)
zrc = fea.Zero_Crossing(y,win)
