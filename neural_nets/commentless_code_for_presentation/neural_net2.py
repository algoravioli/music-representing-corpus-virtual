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
from classes.InstrumentCreator import DecentSamplerAudioExporter
from RTNeuralutils.modelutils import *

# %%
# Setup the Model

BLOCK_SIZE = 10
model = Creator().createDenseModelForNeuralNet2(2, 32, BLOCK_SIZE, "tanh")
inputArray, outputArray, Fs = Ingester().ingest_audio_for_neural_net2(
    "../saxophone_audiodata/multiphonics/", block_size=BLOCK_SIZE
)
early_stopping = Creator().createEarlyStopper()
model.fit(
    inputArray,
    outputArray,
    epochs=200,
    batch_size=1000,
    verbose=1,
    callbacks=[early_stopping],
)
model.save("saved_models_h5/neural_net2.h5")

DecentSamplerAudioExporter().export_audio(
    model,
    num_notes=127,
    block_size=BLOCK_SIZE,
    path_to_save="audio_output/neural_net2_audio",
)
DecentSamplerAudioExporter().create_decent_sampler_xml(
    "audio_output/neural_net2_audio",
    path_to_save="decentsampler_instruments/CreatedInstrument [Decent Sampler]",
)
DecentSamplerAudioExporter().export_audio_from_train_data(
    model,
    inputArray,
    block_size=BLOCK_SIZE,
    num_samples=1,
    path_to_save="audio_output/neural_net2_audio_traindata",
)
DecentSamplerAudioExporter().create_decent_sampler_xml_from_1_sample(
    "audio_output/neural_net2_audio_traindata",
    path_to_save="decentsampler_instruments/CreatedInstrument TD [Decent Sampler]",
)
