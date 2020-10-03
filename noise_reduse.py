import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import noisereduce as nr
from scipy.io.wavfile import read
from noisereduce.generate_noise import band_limited_noise
from noisereduce.utils import int16_to_float32, float32_to_int16
#accsesing libraries
import librosa

#opening audio file
wav_loc = "v2_s.wav"

#loading wav file
rate, data = read(wav_loc)

#converting into single channel source
data = data[:,0]


#converting into 16 bit int data array
if np.issubdtype(data.dtype, np.integer):
    data = data / np.iinfo(data.dtype).max
plt.plot(data[0:])
maxi=0

for i in (data):
	if maxi<i:
		maxi=i

print("amplitude : ",maxi)

#creating a lag variable to account for the beginning lag in the audio recording
noise_list=[]
lag=0

n=len(data)
for i in data:
	if i>0 :
		break
	else:
		lag=lag+1

cnt = 0
for i in data:
	cnt = cnt+1
	if abs(i) > 0 :
		if cnt < 100000:
			noise_list.append(i)
		else:
			break

#picking up noise clip data from lag+3000 to lag+15000 and creating noise  profile from noise clip

noise_clip=data[lag+3000:lag+15000]

video_len = len(data) / rate

reduced=float32_to_int16(nr.reduce_noise(audio_clip=data, noise_clip=noise_clip, prop_decrease=0.8))

from scipy.io.wavfile import write
write("v1_ss8.wav",rate,reduced)

cmd = 'ffmpeg -y -i v1_ss8.wav  -r 30 -i v1_ss_V_8.h264  -filter:a aresample=async=1 -c:a flac -c:v copy v1_ss_V_8.mkv'
subprocess.call(cmd, shell=True)                                     # "Muxing Done
print('Done')




