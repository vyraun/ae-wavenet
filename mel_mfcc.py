# Functions for extracting Mel and MFCC information from a raw Wave file

# T = time step, F = frame (every ~100 timesteps or so)
# Waveform: shape(T), values (limited range integers)
# MFCC + d + a: shape(F, 13 * 3 see figure 1)
# Output of Layer 1 Conv: shape(F, 39, 768)

# From paper:
# 80 log-mel filterbank features extracted every 10ms from 25ms-long windows
# 13 MFCC features

# From librosa.feature.melspectrogram:
# n_fft (# timesteps in FFT window)
# hop_length (# timesteps between successive window positions)

# From librosa.filters.mel:
# n_fft ("# FFT components" (is this passed on to melspectrogram?)
# n_mels (# mel bands to generate)

# From librosa.feature.mfcc):
# n_mfcc (# of MFCCs to return)

# Workflow
import librosa
import numpy as np

class MfccProcess(Object):
    def __init__(self, sample_rate_sec=16000, window_length_ms=25,
            hop_length_ms=10, n_mels=80, n_mfcc=13):
        self.sample_rate_sec = sample_rate_sec
        self.window_length_ms = window_length_ms
        self.hop_length_ms = hop_length_ms
        self.n_mels = n_mels
        self.n_mfcc = n_mfcc

    def func(file):
        y, _ = librosa.load(self, self.sample_rate_sec)
        n_fft = self.sample_rate_ms * self.window_length_ms
        hop_length = self.sample_rate_ms * self.hop_length_ms
        mfcc = librosa.feature.mfcc(y=y, sr=sample_rate, n_fft=n_fft,
                hop_length=hop_length, n_mels=self.n_mels, n_mfcc=self.n_mfcc)
        mfcc_delta = librosa.feature.delta(mfcc)
        mfcc_delta2 = librosa.feature.delta(mfcc, order=2)
        mfcc_and_derivatives = np.concatenate((mfcc, mfcc_delta, mfcc_delta2), axis=0)
        return mfcc_and_derivatives








sample_rate = 16000 # timestep / second
sample_rate_ms = int(sample_rate / 1000) # timestep / ms 
window_length_ms = 25 # ms
hop_length_ms = 10 # ms
n_mels = 80
n_mfcc = 13

# encoder
in_channels = input.shape[0]
mid_channels = 768
kernel_size = 3

