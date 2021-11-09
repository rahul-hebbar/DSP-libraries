import numpy as np

def aud_norm(aud):
    return aud*(1/max(aud))

def Win(aud, choice = "ham"):
    aud = aud_norm(aud)
    if choice == "ham":
        win = np.hamming(max(1,len(aud)//50))
        win = win/len(win)
    if choice == "rect":
        win = np.ones(max(1,len(aud)//50))
        win = win/len(win)
    return win

def sgn(x):
  y = np.zeros_like(x)
  y[np.where(x >= 0)] = 1.0
  y[np.where(x < 0)] = -1.0
  return y

def Zero_Crossing(aud,window):
    aud = aud_norm(aud)
    aud_shift = np.roll(aud, 1)
    aud_shift[0] = 0.0
    abs_diff = np.abs(sgn(aud) - sgn(aud_shift))
    zc = (1/(2*len(aud)))*(np.convolve(abs_diff, window, mode="same"))
    return zc

def Short_Time_Mag(aud,window):
    aud = aud_norm(aud)
    return np.convolve(np.abs(aud),window,mode = "same")

def Norm_Short_Time_Mag(aud,window):
    aud = aud_norm(aud)
    mag = np.convolve(np.abs(aud),window,mode = "same")
    mag = mag*(1/max(mag))
    return mag

def Short_Time_Energ(aud,window):
    aud = aud_norm(aud)
    return np.convolve(np.square(aud),np.square(window),mode = "same")

def Norm_Short_Time_Energ(aud,window):
    aud = aud_norm(aud)
    eng = np.convolve(np.square(aud),np.square(window),mode = "same")
    eng = eng*(1/max(eng))
    return eng


