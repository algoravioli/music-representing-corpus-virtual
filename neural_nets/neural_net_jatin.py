#%%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import chardet

from classes.DataAccessor import load_data, get_list_of_composers, get_data_for_composer

# %%
main_data = load_data("./data/maestrov3.csv")
midi_data = get_data_for_composer(main_data, ['George Frideric Handel', 'Nikolai Medtner'])
print(midi_data.shape)

# %%
model = tf.keras.Sequential()
model.add(tf.keras.layers.GRU(64, input_dim=1, return_sequences=True))
model.add(tf.keras.layers.GRU(128, return_sequences=True))
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
midi0 = np.reshape(midi_data, (1, len(midi_data), -1))
time_steps = np.reshape(np.arange(midi0.shape[1]), (1, -1, 1))

print(midi0)
print(midi0.shape)
print(time_steps)
print(time_steps.shape)


# %%
model.fit(time_steps, midi0, epochs=5)

# %%
print(model(time_steps))

# %%
