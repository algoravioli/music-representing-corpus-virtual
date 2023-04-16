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

activations_list = ["tanh", "relu", "sigmoid", "linear"]
activation = activations_list[
    0  # change this from 0 - 3 to change the activation function
]
MEMORY = 8
model = Creator().createModelForNeuralNet3(4, MEMORY, activation=activation, scaler=2)
inputArray, outputArray = Ingester().ingest_audio_for_neural_net3(
    "../saxophone_audiodata/ordinaire/", memory=MEMORY
)
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

save_model(model, "saved_models_json/neural_net3.json")
print("Model Weights Loaded!")


