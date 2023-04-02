# %%
import os

import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from classes.DataIngester import Ingester
from classes.InstrumentCreator import DecentSamplerAudioExporter
from classes.ModelCreator import Creator
from RTNeuralutils.modelutils import *
from scipy.io.wavfile import write
from tqdm import tqdm

# We will use an arbitrarily long method to determine some arbitrarily medium-ish sized number for BLOCK_SIZE
# We check through all the lengths of the audio files and find the mean length
path_to_files = "../kinderspiel-data/piano/"
BLOCK_SIZE = Ingester().arbitrary_method_for_neural_net4(path_to_files)
print(f"BLOCK_SIZE: {BLOCK_SIZE}")
BLOCK_SIZE = int(BLOCK_SIZE // 40)
# %%
# Get the input and output dataset for our network
inputArray, outputArray = Ingester().ingest_audio_for_neural_net4(
    path_to_files, BLOCK_SIZE
)
# Here, we decide that the input size is the number of columns in the inputArray
input_size = inputArray.shape[1] 

# %%
# Setup the Model
model = Creator().createDenseModelForNeuralNet4(20, 1000, input_size, BLOCK_SIZE)
# %%
# Train the model
early_stopping = Creator().createEarlyStopper()

model.fit(
    inputArray,
    outputArray,
    epochs=200,
    batch_size=20,
    verbose=1,
    callbacks=[early_stopping],
)

# %%
# Here, we use the built in tensorflow save model function to save the model as it is too big for RTNeural anyway
model.save("saved_models_h5/neural_net4.h5")


# %%
# If you have already trained your model, you can load the model weights and skip the training step
model = tf.keras.models.load_model("saved_models_h5/neural_net4.h5")
print("Model Weights Loaded!")

# %%
# This next part is the creation of the DecentSampler instrument.
# We will run inference on the model to create 1 note, with the note being a 8499 second long file (our BLOCK_SIZE, but also, this is the wavetable bit).
# We will then have each file be a 1 second long file by repeating it until it reaches 44100 samples at least.
# We will then run our DecentSampler creator to create the instrument xml file.
# For this demonstration, we will use a random input from our input dataset, but in reality, this can be any input that is the same size as 1 row of our input dataset.
random_value = np.random.randint(0, inputArray.shape[0])
input_to_sample_from = inputArray[random_value]
input_to_sample_from = np.reshape(input_to_sample_from, (1, -1))

# %%
checkOutput = DecentSamplerAudioExporter().create_decent_sampler_xml_for_neural_net_4(
    input_to_sample_from, model
)

# %%
