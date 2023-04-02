# %%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import chardet

from classes.DataAccessor import load_data, get_list_of_composers, get_data_for_composer

# %%
# Load full dataset and filter data from a set of composers
main_data = load_data("./data/maestrov3.csv")
midi_data = get_data_for_composer(
    main_data, ["George Frideric Handel", "Nikolai Medtner"]
)
print(midi_data.shape)

# %%
# Construct a basic model
model = tf.keras.Sequential()
model.add(tf.keras.layers.GRU(64, input_dim=1, return_sequences=True))
model.add(tf.keras.layers.GRU(128, return_sequences=True))
model.add(tf.keras.layers.Dense(4))
# probably a good idea to have some regularizers here...

opt = tf.keras.optimizers.Adam(learning_rate=0.02)
model.compile(loss="mean_squared_error", optimizer=opt)
model.summary()

# %%
# if your model is already trained, you can load the weights here
model = tf.keras.models.load_model("saved_models_h5/neural_net1.h5")

# %%
# if your model is already trained, you can load the weights here
model = tf.keras.models.load_model("saved_models_h5/neural_net1.h5")

# %%
# Test the model input and output shapes
inputs = tf.random.normal([1, 10, 1])
outputs = model(inputs)

print(inputs)
print(tf.shape(outputs))
print(outputs)

# %%
# Configure MIDI input data for network training
midi0 = np.reshape(midi_data, (1, len(midi_data), -1))
time_steps = np.reshape(np.arange(midi0.shape[1]), (1, -1, 1))

print(midi0)
print(midi0.shape)
print(time_steps)
print(time_steps.shape)


# %%
#Train the network!
# Adjust the number of epochs depending on how long you want to train for.
model.fit(time_steps, midi0, epochs=3000, verbose=1)

# %%
# Print the model output
print(model(time_steps))

# %%
model.save("saved_models_h5/neural_net1.h5")
# %%
