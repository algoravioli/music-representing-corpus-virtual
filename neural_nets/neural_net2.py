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
model = Creator().create_model_dense(2, 16, BLOCK_SIZE, "tanh")
# %%
# Path: ../saxophone_audiodata/multiphonics/ where each file is called multiphonics(N).wav where (N) starts with 01 and ends at 228

inputArray, outputArray, Fs = Ingester().ingest_audio_for_neural_net2(
    "../saxophone_audiodata/multiphonics/", block_size=BLOCK_SIZE
)
# %%
model.fit(
    inputArray,
    outputArray,
    epochs=200,
    batch_size=1000,
    verbose=1,
)

# %%
# use save model from RTNeuralutils
save_model(model, "saved_models_json/neural_net2.json")
# %%
# also use built in tensorflow save model
model.save("saved_models_h5/neural_net2.h5")

# %%
# If you have already trained your model, you can load the model weights and skip the training step
model = tf.keras.models.load_model("saved_models_h5/neural_net2.h5")
print("Model Weights Loaded!")

# %%

# This next part is the creation of the DecentSampler instrument.
# We will run inference on the model to create 127 notes, with each note being a 1 second long file.
# We will then run our DecentSampler creator to create the instrument xml file.

DecentSamplerAudioExporter().export_audio(
    model,
    num_notes=127,
    block_size=BLOCK_SIZE,
    path_to_save="audio_output/neural_net2_audio",
)

# %%
DecentSamplerAudioExporter().create_decent_sampler_xml(
    "audio_output/neural_net2_audio",
    path_to_save="decentsampler_instruments/CreatedInstrument [Decent Sampler]",
)
# %%
# We can also predict the output of the model using the input of the training data
# This gives us a clue what the model thinks its supposed to do
# And also gives us some cool sounds
DecentSamplerAudioExporter().export_audio_from_train_data(
    model,
    inputArray,
    block_size=BLOCK_SIZE,
    num_samples=127,
    path_to_save="audio_output/neural_net2_audio_traindata",
)

# %%
DecentSamplerAudioExporter().create_decent_sampler_xml(
    "audio_output/neural_net2_audio",
    path_to_save="decentsampler_instruments/CreatedInstrument TD [Decent Sampler]",
)


# %%
