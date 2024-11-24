import soundfile as sf
import numpy as np
from os import listdir
from os.path import isfile, join
files = [f for f in listdir("./Tracks - In") if isfile(join("./Tracks - In", f))]

i = 1
for file in files:
    data, samplerate = sf.read(f"./Tracks - In/{file}")
    name = "TRK{:02d}".format(i)
    
    if (data.ndim == 2):
        x, y = data[:,:1], data[:,1:]
        data = (x + y)/2

    sf.write(f"./Tracks - Out/{name}.WAV", data, 48000, subtype='PCM_24')
    i += 1
    
