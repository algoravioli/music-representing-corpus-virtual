#%%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import chardet


from classes.DataGenerator import Generator
from classes.DataIngester import Ingester
from classes.DataPlotter import Plotter

ingester = Ingester()
plotter = Plotter()
generator = Generator()
os.listdir("./data")
# %%
mainData = "./data/maestrov3.csv"
with open(mainData, "rb") as f:
    result = chardet.detect(f.read())
main_df = pd.read_csv(mainData, encoding=result["encoding"])
#%%
listOfComposers = main_df["canonical_composer"].unique()

composer_df = main_df.query(f"canonical_composer == '{listOfComposers[1]}'")
composerMidiPaths = composer_df["midi_filename"].to_list()
print(composerMidiPaths[0])
#%%
main_df.head()
path = "./data/2018/MIDI-Unprocessed_Chamber2_MID--AUDIO_09_R3_2018_wav--1.midi"

midiObject = generator.convertMidiToObject(path)
notesArray = generator.returnArrayOfNotes(midiObject)
print(notesArray[0:5, :])

# plotter.plotPianoRoll(midiObject, 0, 128, 100)

# %%
