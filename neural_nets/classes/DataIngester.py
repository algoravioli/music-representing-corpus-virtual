import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pretty_midi


class Ingester:
    def __init__(self):
        pass

    def ingest_csv(self, path, header=False, sep=",", datatype="pd"):
        df = pd.read_csv(path, header=header, sep=sep)
        self.data = df.to_numpy()
        if datatype == "pd":
            output = df
        elif datatype == "np":
            output = self.data
        else:
            raise ValueError("type must be either pd or np")

        return output

    def ingest_midi(self, path):
        self.midiObject = pretty_midi.PrettyMIDI(path)
        return self.midiObject
