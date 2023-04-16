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

main_data = load_data("./data/maestrov3.csv")
composers = get_list_of_composers(main_data)
print(*composers, sep="\n")

midi_data = get_data_for_composer(main_data, ["Handel", "Medtner"])
startTimes = midi_data[:, 0]
endTimes = midi_data[:, 1]
pitches = midi_data[:, 2]
velocities = midi_data[:, 3]
durations = np.round(midi_data[:, 4], 3)

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

model = Creator().createModelForNeuralNet1(MEMORY, params_multiplier=10)

early_stopping = Creator().createEarlyStopper()
model.fit(
    {
        "startTimes": startTimesIn,
        "pitches": pitchesIn,
        "velocities": velocitiesIn,
        "durations": durationsIn,
    },
    {
        "outputStartTimes": startTimesOut,
        "outputPitches": pitchesOut,
        "outputVelocities": velocitiesOut,
        "outputDurations": durationsOut,
    },
    epochs=50,
    batch_size=1000,
)

model.save("saved_models_h5/neural_net1.h5")
outputArray = Generator().continuePieceUsingNeuralNet1(
    model, startTimesIn[-1], pitchesIn[-1], velocitiesIn[-1], durationsIn[-1], 100
)
pathForMidi = "../neural_nets/output_midi/NeuralNet1_output.mid"
Generator().saveArrayAsMidi(outputArray, pathForMidi)