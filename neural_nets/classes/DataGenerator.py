#%%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import pretty_midi

from classes.DataIngester import Ingester

ingester = Ingester()


class Generator:
    def __init__(self):
        pass

    def convertMidiToObject(self, path):
        self.midiObject = ingester.ingest_midi(path)
        return self.midiObject

    def returnArrayOfNotes(self, midiObject=None):
        if midiObject is None:
            midiObject = self.midiObject
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


# %%
