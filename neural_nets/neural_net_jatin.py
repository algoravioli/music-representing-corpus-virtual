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
handel = listOfComposers[20]

composer_df = main_df.query(f"canonical_composer == '{handel}'")
composerMidiPaths = composer_df["midi_filename"].to_list()
# print(composerMidiPaths)

# %%
midi_data = []
for midi_file in composerMidiPaths:
    midi_data.append(generator.returnArrayOfNotes(generator.convertMidiToObject(f'./data/{midi_file}')))

# %%
model = tf.keras.Sequential()
model.add(tf.keras.layers.GRU(64, input_dim=1, return_sequences=True))
model.add(tf.keras.layers.GRU(128, return_sequences=True))
model.add(tf.keras.layers.GRU(256, return_sequences=True))
model.add(tf.keras.layers.GRU(512, return_sequences=True))
model.add(tf.keras.layers.Dense(4))
# probably a good idea to have some regularizers here...

opt = tf.keras.optimizers.Adam(learning_rate=0.02)
model.compile(loss='mean_squared_error', optimizer=opt)
model.summary()

# %%
inputs = tf.random.normal([1, 10, 1])
outputs = model(inputs)

print(inputs)
print(tf.shape(outputs))
print(outputs)

# %%
midi0 = np.reshape(midi_data[0], (1, len(midi_data[0]), -1))
time_steps = np.reshape(np.arange(midi0.shape[1]), (1, -1, 1))
# How can we structure this for MIDI files with different numbers of timsteps?

print(midi0)
print(midi0.shape)
print(time_steps)
print(time_steps.shape)


# %%
model.fit(time_steps, midi0, epochs=250)

# %%
print(model(time_steps))

# %%
