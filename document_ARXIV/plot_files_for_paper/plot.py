# %%
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import mido
from visual_midi import Plotter
from visual_midi import Preset
import pretty_midi
import libfmp.c1
import IPython.display as ipd
import pandas as pd
from matplotlib import patches
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.collections import PolyCollection
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import numpy as np

# Plot noteNumber_16.wav
# y, sr = librosa.load("noteNumber_16.wav")
# plt.figure(figsize=(8, 4))
# plt.plot(y)
# plt.title("Generated Audio of Neural Network 2")
# plt.xlabel("Time (samples)")
# plt.ylabel("Amplitude")


# Plot Midi NeuralNet1_output.mid with pypianoroll

# midi_data = pretty_midi.PrettyMIDI("output.mid")
# midi_list = []

# for instrument in midi_data.instruments:
#     for note in instrument.notes:
#         print(note)
#         start = note.start
#         end = note.end
#         pitch = note.pitch
#         print(pitch)
#         velocity = note.velocity
#         midi_list.append([start, end, pitch, velocity, instrument.name])

# midi_list = sorted(midi_list, key=lambda x: (x[0], x[2]))

# df = pd.DataFrame(
#     midi_list, columns=["Start", "End", "Pitch", "Velocity", "Instrument"]
# )
# # print(df)


# def midi_to_list(midi):
#     """Convert a midi file to a list of note events

#     Notebook: C1/C1S2_MIDI.ipynb

#     Args:
#         midi (str or pretty_midi.pretty_midi.PrettyMIDI): Either a path to a midi file or PrettyMIDI object

#     Returns:
#         score (list): A list of note events where each note is specified as
#             ``[start, duration, pitch, velocity, label]``
#     """

#     if isinstance(midi, str):
#         midi_data = pretty_midi.pretty_midi.PrettyMIDI(midi)
#     elif isinstance(midi, pretty_midi.pretty_midi.PrettyMIDI):
#         midi_data = midi
#     else:
#         raise RuntimeError(
#             "midi must be a path to a midi file or pretty_midi.PrettyMIDI"
#         )

#     score = []

#     for instrument in midi_data.instruments:
#         for note in instrument.notes:
#             print(note)
#             start = note.start
#             duration = note.end - start
#             pitch = note.pitch
#             velocity = note.velocity / 128.0
#             score.append([start, duration, pitch, velocity, instrument.name])
#     return score


# score = midi_to_list(midi_data)
# libfmp.c1.visualize_piano_roll(score, figsize=(8, 3), velocity_alpha=True)
# Note the blurry section between 1.5s and 2.3s - that's the pitch bending up!
# %%
"""
=============================================
Generate polygons to fill under 3D line graph
=============================================

Demonstrate how to create polygons which fill the space under a line
graph. In this example polygons are semi-transparent, creating a sort
of 'jagged stained glass' effect.
"""

# import document_ARXIV/plot_files_for_paper/Neural_Net_3 (bypass).mp3
# import document_ARXIV/plot_files_for_paper/Neural_Net_3 (on).mp3

# bypass, sr = librosa.load("Neural_Net_3(bypass).mp3", sr=None)
# effected, sr = librosa.load("Neural_Net_3(on).mp3", sr=None)
# normalised_bypass = bypass / np.max(np.abs(bypass))
# normalised_effected = effected / np.max(np.abs(effected))
# # plot transfer function of signal
# plt.figure(figsize=(8, 4))
# plt.plot(normalised_bypass[1300:1350],normalised_effected[1300:1350])
# # plt.plot(, alpha=0.5)
# plt.title("Transfer Function of Neural Network 3")
# plt.xlabel("Time (samples)")
# plt.ylabel("Amplitude")
# plt.legend(["Bypass", "Effected"])
# plt.show()

# return spectrogram in plot
# librosa.display.specshow(
#     librosa.amplitude_to_db(np.abs(librosa.stft(bypass[0:int(len(bypass)*0.2)], n_fft=8192, hop_length=256)), ref=np.max),
#     y_axis="log",
#     x_axis="time",
#     sr=sr,
# )
# # plt.colorbar(format="%+2.0f dB")
# plt.title("Bypass")


# # %%

# librosa.display.specshow(
#     librosa.amplitude_to_db(np.abs(librosa.stft(effected[0:int(len(bypass)*0.2)], n_fft=8192, hop_length=256)), ref=np.max),
#     y_axis="log",
#     x_axis="time",
#     sr=sr,
# )
# # plt.colorbar(format="%+2.0f dB")
# plt.title("Effected")

nn4audio, sr = librosa.load("noteNumber_0.wav", sr=None)
nn4audio = nn4audio / np.max(np.abs(nn4audio))
plt.plot(nn4audio[0:256])
plt.title("Generated Wavetable of Neural Network 4")
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude")

# %%
