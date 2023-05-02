# %%
import os
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from classes.DataAccessor import get_data_for_composer, get_list_of_composers, load_data
from classes.DataIngester import Ingester
from classes.ModelCreator import Creator
from classes.DataGenerator import Generator

tf.config.run_functions_eagerly(True)
# %%
# In case you don't know which composers are available, you can use this function
main_data = load_data("./data/maestrov3.csv")
composers = get_list_of_composers(main_data)
# uncomment this next line to print the list of composers
# print(*composers, sep="\n")

# %%
# Load full dataset and filter data from a set of composers
midi_data = get_data_for_composer(main_data, ["Medtner"])
startTimes = midi_data[:, 0]
endTimes = midi_data[:, 1]
pitches = midi_data[:, 2]
velocities = midi_data[:, 3]
durations = np.round(midi_data[:, 4], 3)
# %%
# Roll dataset by memory length:
# How this works is, we feed the network a sequence of notes and attributes
# And we ask it to predict the next note and set of attributes
MEMORY = 32
startTimesIn, startTimesOut = Ingester().ingest_midi_for_neural_net1_ROLLFUNCTION(
    startTimes, MEMORY
)
pitchesIn, pitchesOut = Ingester().ingest_midi_for_neural_net1_ROLLFUNCTION(
    pitches, MEMORY
)
velocitiesIn, velocitiesOut = Ingester().ingest_midi_for_neural_net1_ROLLFUNCTION(
    velocities, MEMORY
)
durationsIn, durationsOut = Ingester().ingest_midi_for_neural_net1_ROLLFUNCTION(
    durations, MEMORY
)

# %%
# Construct our neural_net1 model
# model = Creator().createModelForNeuralNet1(MEMORY, params_multiplier=10)

# %%
# The model.fit in this case might look abit scary but it's just a lot of parameters
# The important thing is that we are feeding the model the input and output data
# early_stopping = Creator().createEarlyStopper()
# model.fit(
#     {
#         "startTimes": startTimesIn,
#         "pitches": pitchesIn,
#         "velocities": velocitiesIn,
#         "durations": durationsIn,
#     },
#     {
#         "outputStartTimes": startTimesOut,
#         "outputPitches": pitchesOut,
#         "outputVelocities": velocitiesOut,
#         "outputDurations": durationsOut,
#     },
#     epochs=50,
#     batch_size=1000,
# )
# %%
# We use built in tensorflow save model function as RTNeural is not necessary for this model
# model.save("saved_models_h5/neural_net1.h5")
# %%
# If you have already trained your model, you can load the model weights and skip the training step
model = tf.keras.models.load_model("saved_models_h5/neural_net1.h5")
print("Model Weights Loaded!")

# %%

outputArray = Generator().continuePieceUsingNeuralNet1(
    model, startTimesIn[-1], pitchesIn[-1], velocitiesIn[-1], durationsIn[-1], 100
)
# %%
plt.plot(outputArray[:, 1])
# %%
pathForMidi = "../neural_nets/output_midi/NeuralNet1_output.mid"
Generator().saveArrayAsMidi(outputArray, pathForMidi)


# %%
