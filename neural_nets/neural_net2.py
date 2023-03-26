# %%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import librosa
import librosa.display
from tqdm import tqdm
from scipy.io.wavfile import write
from classes.DataIngester import Ingester
from classes.ModelCreator import Creator
from RTNeuralutils.modelutils import *

# Setup the Model
model = Creator().create_model(10, 200, "tanh")
# %%
# Path: ../saxophone_audiodata/multiphonics/ where each file is called multiphonics(N).wav where (N) starts with 01 and ends at 228

inputArray, outputArray, Fs = Ingester().ingest_audio_for_neural_net2(
    "../saxophone_audiodata/multiphonics/"
)
# %%
model.fit(inputArray, outputArray, epochs=50, batch_size=100, verbose=1)

# %%
# use save model from RTNeuralutils
save_model(model, "saved_models_json/neural_net2.json")
# also use built in tensorflow save model
model.save("saved_models_h5/neural_net2.h5")

# %%

# Since each timestep is 16 samples, we will need to have intended length in samples / 16 as the amount of iterations we need.
# We create a random noise buffer of 16 samples * the amount of iterations needed

lengthOfNote = 0.5  # seconds
Fs = 44100
iterations = int(lengthOfNote * Fs / 16)
noiseBuffer = np.random.uniform(-1, 1, 16 * iterations)

# We need to reshape this into a 2D array of shape (iterations, 16)
noiseBuffer = noiseBuffer.reshape(iterations, 16)
# Now we can use this noiseBuffer as the input to our model, and concatenate the outputs to create our intended output
output = np.array([])
for i in tqdm(range(iterations)):
    currentOutput = model.predict(noiseBuffer[i].reshape(1, 16), verbose=0)
    output = np.concatenate((output, currentOutput[0]))

# Check what the output looks like
plt.plot(output[0:10000])
# we can also write this output to a wav file
write("audio_output/neural_net2.wav", Fs, output)

# %%
