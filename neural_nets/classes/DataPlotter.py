import librosa.display
import librosa
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pretty_midi


class Plotter:
    def __init__(self):
        pass

    def plotPianoRoll(self, pm, start_pitch, end_pitch, fs=100):
        # Use librosa's specshow function for displaying the piano roll
        librosa.display.specshow(
            pm.get_piano_roll(fs)[start_pitch:end_pitch],
            hop_length=1,
            sr=fs,
            x_axis="time",
            y_axis="cqt_note",
            fmin=pretty_midi.note_number_to_hz(start_pitch),
        )
