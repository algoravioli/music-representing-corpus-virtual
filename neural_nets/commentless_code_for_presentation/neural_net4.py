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

path_to_files = "../kinderspiel-data/piano/"
BLOCK_SIZE = Ingester().arbitrary_method_for_neural_net4(path_to_files)
BLOCK_SIZE = int(BLOCK_SIZE // 40)
inputArray, outputArray = Ingester().ingest_audio_for_neural_net4(
    path_to_files, BLOCK_SIZE
)
input_size = inputArray.shape[1]
model = Creator().createDenseModelForNeuralNet4(20, 1000, input_size, BLOCK_SIZE)
early_stopping = Creator().createEarlyStopper()
model.fit(
    inputArray,
    outputArray,
    epochs=200,
    batch_size=20,
    verbose=1,
    callbacks=[early_stopping],
)
model.save("saved_models_h5/neural_net4.h5")
random_value = np.random.randint(0, inputArray.shape[0])
input_to_sample_from = inputArray[random_value]
input_to_sample_from = np.reshape(input_to_sample_from, (1, -1))
checkOutput = DecentSamplerAudioExporter().create_decent_sampler_xml_for_neural_net_4(
    input_to_sample_from, model
)
