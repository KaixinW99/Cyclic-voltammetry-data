import numpy as np
import scipy.signal as SciSig
import matplotlib.pyplot as plt
import os, sys

data_file = sys.argv[1]
data_name = os.path.basename(data_file)
data_name_without_extension = os.path.splitext(data_name)[0]

#b, a = SciSig.butter(8,0.125)
b, a = SciSig.ellip(4, 0.01, 120, 0.125)
E, I = np.genfromtxt(data_file, unpack=True, skip_header=1)
y = SciSig.filtfilt(b, a, I, method="gust")
#plt.plot(E, I, label='Original', linewidth=2)
plt.plot(E, y, label='Filtered', linewidth=1)
plt.show()
