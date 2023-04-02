import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pretty_midi
import librosa
from tqdm import tqdm


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

    def ingest_midi_for_neural_net1_ROLLFUNCTION(self, inputArray, memory):
        # this produces an input and output dataset
        newInputArray = np.array([])
        for i in range(memory):
            if i == 0:
                newInputArray = np.roll(inputArray, -i)
            else:
                newInputArray = np.column_stack(
                    (newInputArray, np.roll(inputArray, -i))
                )

        outputArray = inputArray
        # delete the last MEMORY rows
        newInputArray = newInputArray[:-memory]
        outputArray = outputArray[memory:]
        return newInputArray, outputArray

    def ingest_audio_for_neural_net2(self, path, block_size=1000):
        # Path is a directory containing wav files
        trainingFiles = os.listdir(path)
        # Remove .DS_Store from the list if it is there
        if ".DS_Store" in trainingFiles:
            trainingFiles.remove(".DS_Store")

        trainingFiles = [path + file for file in trainingFiles]

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

    def ingest_audio_for_neural_net3(self, path_to_files, memory=8):
        trainingFiles = os.listdir(path_to_files)
        if ".DS_Store" in trainingFiles:
            trainingFiles.remove(".DS_Store")
        trainingFiles = [path_to_files + file for file in trainingFiles]
        inputArray = np.array([])
        outputArray = np.array([])
        for i in tqdm(range(len(trainingFiles))):
            # Load the audio file and append to inputArray as 1D array
            y, Fs = librosa.load(trainingFiles[i])
            # Convert to mono
            y = librosa.to_mono(y)
            outputArray = np.append(outputArray, y)

        # Need to shift the inputArray by memory times
        for i in range(memory):
            shiftedInputArray = np.roll(outputArray, -i)
            shiftedInputArray[-1] = 0
            if i == 0:
                inputArray = shiftedInputArray
            else:
                inputArray = np.vstack((inputArray, shiftedInputArray))

        inputArray = inputArray.T

        # delete last memory rows of inputArray and outputArray
        inputArray = inputArray[:-memory]
        outputArray = outputArray[memory:]

        return inputArray, outputArray

    def arbitrary_method_for_neural_net4(self, path_to_files):
        trainingFiles = os.listdir(path_to_files)
        if ".DS_Store" in trainingFiles:
            trainingFiles.remove(".DS_Store")
        trainingFiles = [path_to_files + file for file in trainingFiles]
        outputLengthArray = np.array([])

        for i in tqdm(range(len(trainingFiles))):
            # Load the audio file
            y, Fs = librosa.load(trainingFiles[i])
            # Convert to mono
            y = librosa.to_mono(y)
            outputLengthArray = np.append(outputLengthArray, len(y))

        return int(np.mean(outputLengthArray))

    def ingest_audio_for_neural_net4(self, path_to_files, BLOCK_SIZE=1000):
        trainingFiles = os.listdir(path_to_files)
        if ".DS_Store" in trainingFiles:
            trainingFiles.remove(".DS_Store")

        trainingFiles = [path_to_files + file for file in trainingFiles]
        inputArray = np.array([])
        outputArray = np.array([])
        for i in range(len(trainingFiles)):
            print(f"File No. {i + 1} of {len(trainingFiles)}")
            # Load the audio file
            y, Fs = librosa.load(trainingFiles[i])
            # Convert to mono
            y = librosa.to_mono(y)
            # Extract MFCC
            mfcc = librosa.feature.mfcc(y=y, sr=Fs, n_mels=512, fmax=16000)
            # sum the rows of mfcc
            mfcc = np.sum(mfcc, axis=-1)
            # reshape mfcc to be a 2D array of shape (1, n)
            mfcc = mfcc.reshape(1, len(mfcc))
            # Append to inputArray
            if len(y) < BLOCK_SIZE:
                y = np.pad(y, (0, BLOCK_SIZE - len(y)), "constant")

            if i == 0:
                inputArray = mfcc
                outputArray = y[0:BLOCK_SIZE]
            else:
                inputArray = np.concatenate((inputArray, mfcc), axis=0)
                # np.vstack outputArray
                outputArray = np.vstack((outputArray, y[0:BLOCK_SIZE]))

        print(inputArray.shape)
        print(outputArray.shape)

        return inputArray, outputArray
