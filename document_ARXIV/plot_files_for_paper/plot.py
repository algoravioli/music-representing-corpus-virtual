# %%
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import mido
import pretty_midi

# Plot noteNumber_16.wav
# y, sr = librosa.load("noteNumber_16.wav")
# plt.figure(figsize=(8, 4))
# plt.plot(y)
# plt.title("Generated Audio of Neural Network 2")
# plt.xlabel("Time (samples)")
# plt.ylabel("Amplitude")


# Plot Midi NeuralNet1_output.mid with pypianoroll
pm = pretty_midi.PrettyMIDI("NeuralNet1_output.mid")
