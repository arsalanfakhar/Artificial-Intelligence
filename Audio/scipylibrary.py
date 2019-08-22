#readaudiofile
from scipy.io import wavfile

thefile = 'MY.wav'

[fs, x] = wavfile.read(thefile)

print(fs) #frequency
print(x)
