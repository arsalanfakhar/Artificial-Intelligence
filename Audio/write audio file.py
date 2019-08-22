import numpy as np
import audiofile as af

sampling_rate = 8000
noise = np.random.normal(0, 1, sampling_rate)
noise /= np.amax(np.abs(noise))
af.write('MY.wav', noise, sampling_rate)
af.channels('MY.wav')
af.duration('MY.wav')
sig, fs = af.read('MY.wav')
print(fs)
print(sig)
