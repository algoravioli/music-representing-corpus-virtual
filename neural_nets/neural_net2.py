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

# Since each timestep is 16 samples, we will need to have intended length in samples / 16 as the amount of iterations we need.
# We will also need to have a buffer of 16 samples to start with.
# Lets start with random noise as the input
Fs = 44100
length_of_output = 44100 * 5  # 5 seconds
number_of_predictions = length_of_output // 16
buffer = np.random.rand(16)
output = np.array([])
for i in tqdm(range(number_of_predictions)):
    # Predict the next 16 samples
    prediction = model.predict(buffer.reshape(1, 16))
    # Append the prediction to the output
    output = np.append(output, prediction)
    # Change input buffer to be the last 16 samples of the output
    buffer = output[-16:]

# %%
# use save model from RTNeuralutils
save_model(model, "saved_models_json/neural_net2.json")
# also use built in tensorflow save model
model.save("saved_models_h5/neural_net2.h5")
# %%
plt.plot(output[0:1000])
write("audio_output/neural_net2.wav", Fs, output)

# %%
