import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pretty_midi
import librosa


class Ingester:
    def __init__(self):
        pass

    def ingest_csv(self, path, header=False, sep=",", datatype="pd"):
        df = pd.read_csv(path, header=header, sep=sep)
        self.data = df.to_numpy()
        if datatype == "pd":
            output = df
        elif datatype == "np":
            output = self.data
        else:
            raise ValueError("type must be either pd or np")

        return output

    def ingest_midi(self, path):
        self.midiObject = pretty_midi.PrettyMIDI(path)
        return self.midiObject

    def ingest_audio_for_neural_net2(self, path, block_size=1000):
        # Path is a directory containing wav files
        trainingFiles = os.listdir(path)
        if ".DS_Store" in trainingFiles:
            trainingFiles.remove(".DS_Store")

        trainingFiles = [path + file for file in trainingFiles]
        # Remove .DS_Store from the list if it is there

        inputArray = np.array([])
        outputArray = np.array([])
        for i in range(len(trainingFiles)):
            print(f"File No. {i + 1} of {len(trainingFiles)}")

            self.audio, self.sr = librosa.load(trainingFiles[i])
            self.delayedAudio = np.roll(self.audio, -block_size)
            # remove first block_size samples from both self.audio and self.delayed_audio
            self.audio = self.audio[block_size:]
            self.delayedAudio = self.delayedAudio[block_size:]
            # remove last block_size samples from both self.audio and self.delayed_audio
            self.audio = self.audio[:-block_size]
            self.delayedAudio = self.delayedAudio[:-block_size]

            # reshape input and output to be 2D arrays of shape (n, block_size)
            # batches of block_size samples each
            n = len(self.audio) // block_size
            currentInput = self.audio[: n * block_size]
            currentOutput = self.delayedAudio[: n * block_size]
            currentInput = currentInput.reshape(n, block_size)
            currentOutput = currentOutput.reshape(n, block_size)

            if i == 0:
                inputArray = currentInput
                outputArray = currentOutput
            else:
                inputArray = np.concatenate((inputArray, currentInput), axis=0)
                outputArray = np.concatenate((outputArray, currentOutput), axis=0)

        print(inputArray.shape)
        print(outputArray.shape)

        return inputArray, outputArray, self.sr
