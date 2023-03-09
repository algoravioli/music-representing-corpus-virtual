#%%
import numpy as np
import pretty_midi
from pprint import pprint


class MarkovModel:
    def __init__(self) -> None:
        pass

    def learnFromMidi(self, path):
        midiObject = pretty_midi.PrettyMIDI(path)
        self.midiObject = midiObject
        self.start_time = np.array([])
        self.end_time = np.array([])
        self.pitch = np.array([])
        self.velocity = np.array([])
        for instrument in midiObject.instruments:
            for note in instrument.notes:
                # each note will have start, end, pitch, velocity
                self.start_time = np.append(self.start_time, note.start)
                self.end_time = np.append(self.end_time, note.end)
                self.pitch = np.append(self.pitch, note.pitch)
                self.velocity = np.append(self.velocity, note.velocity)
        # concatenate all of these arrays into one array with 4 columns
        self.notes = np.column_stack(
            (self.start_time, self.end_time, self.pitch, self.velocity)
        )
        return self.notes


a = MarkovModel()
piano_roll = a.learnFromMidi(
    "C:/Users/Chris/Desktop/GitFiles/MVC/neural_nets/data/2004/MIDI-Unprocessed_SMF_02_R1_2004_01-05_ORIG_MID--AUDIO_02_R1_2004_05_Track05_wav.midi"
)
pprint(piano_roll)

# %%
