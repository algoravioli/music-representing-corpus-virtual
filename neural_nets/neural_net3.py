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

# %%
# Setup the Model
# For this model, we will need a model with (up to 8 inputs) and 1 output, ideally this can be achieved best with 1 long audio file, but since Github doesn't like it, I have chopped it up into many small bits, while removing silences.
# The main idea is: Given the previous 8 samples, predict the next sample.
# We will call our Model Creator function as such
# Because of realtime limitations, I only allow specifications of layer sizes up to 8, and specifying the activation functions
activations_list = ["tanh", "relu", "sigmoid", "linear"]
activation = activations_list[
    0  # change this from 0 - 3 to change the activation function
]
# We will call the number of inputs: MEMORY # max 8 
MEMORY = 8
model = Creator().createModelForNeuralNet3(4, MEMORY, activation=activation, scaler=2)

# %%
# Path: ../saxophone_audiodata/ordinaire/

inputArray, outputArray = Ingester().ingest_audio_for_neural_net3(
    "../saxophone_audiodata/ordinaire/", memory=MEMORY
)

# %%
# We will use the same early stopping callback as before
early_stopping = Creator().createEarlyStopper()

model.fit(
    inputArray,
    outputArray,
    epochs=200,
    batch_size=50000,
    verbose=1,
    callbacks=[early_stopping],
    validation_split=0.3,
)
# %%
# use save model from RTNeuralutils
save_model(model, "saved_models_json/neural_net3.json")
# %%
# also use built in tensorflow save model
model.save("saved_models_h5/neural_net3.h5")

# %%
# If you have already trained your model, you can load the model weights and skip the training step
model = tf.keras.models.load_model("saved_models_h5/neural_net3.h5")
print("Model Weights Loaded!")
# %%
# Plot the data to see the model performance
# 1000 samples ought to do the job
testArray = np.array([])
trueArray = np.array([])
randomStartPoint = np.random.randint(0, inputArray.shape[0] - 1000)
for i in tqdm(range(1000)):
    testArray = np.append(
        testArray,
        model.predict(inputArray[i + randomStartPoint].reshape(1, MEMORY), verbose=0),
    )
    trueArray = np.append(trueArray, outputArray[i + randomStartPoint])

# %%
plt.close()
plt.plot(testArray, label="Predicted")
plt.plot(trueArray, label="True")
plt.legend()
plt.xlabel("Sample")
plt.ylabel("Amplitude")
plt.show()

# %%
