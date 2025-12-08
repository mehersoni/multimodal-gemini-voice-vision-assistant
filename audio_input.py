#Microphone → Record Audio → Save as WAV

import sounddevice as sd
import scipy.io.wavfile as wav

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("Speak now...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    wav.write(filename, fs, audio)
    print("Audio Recorded")
