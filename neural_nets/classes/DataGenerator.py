# %%
import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
import pretty_midi

from classes.DataIngester import Ingester
from tqdm import tqdm
from pretty_midi import PrettyMIDI, Instrument, Note

ingester = Ingester()


class Generator:
    def __init__(self):
        pass

    def convertMidiToObject(self, path):
        self.midiObject = ingester.ingest_midi(path)
        return self.midiObject

    def returnArrayOfNotes(self, midiObject=None):
        if midiObject is None:
            midiObject = self.midiObject
        self.start_time = np.array([])
        self.end_time = np.array([])
        self.pitch = np.array([])
        self.velocity = np.array([])
        for instrument in midiObject.instruments:
            for note in instrument.notes:
                # each note will have start, end, pitch, velocity
                self.start_time = np.append(self.start_time, note.start)
                self.end_time = np.append(self.end_time, note.end)
                self.pitch = np.append(self.pitch, note.pitch)
                self.velocity = np.append(self.velocity, note.velocity)
        # concatenate all of these arrays into one array with 4 columns
        self.notes = np.column_stack(
            (self.start_time, self.end_time, self.pitch, self.velocity)
        )
        return self.notes

    def continuePieceUsingNeuralNet1(
        self,
        model,
        inputStartTime,
        inputPitches,
        inputVelocities,
        inputDurations,
        lengthDesired=100,
    ):
        # inputArray here is 1 row of each of our data points
        # we feed that into the model
        outputArray = model(
            {
                "startTimes": np.reshape(inputStartTime, (1, -1)),
                "pitches": np.reshape(inputPitches, (1, -1)),
                "velocities": np.reshape(inputVelocities, (1, -1)),
                "durations": np.reshape(inputDurations, (1, -1)),
            }
        )

        newST = outputArray[0].numpy()[0]
        newP = outputArray[1].numpy()[0]
        if newP < 20:
            newP = np.random.randint(20, 88)
        newV = outputArray[2].numpy()[0]
        newD = outputArray[3].numpy()[0]

        outputSTArray = np.array([newST])
        outputPArray = np.array([newP])
        outputVArray = np.array([newV])
        outputDArray = np.array([newD])

        # we then append the new data to the input array and remove the first element
        # we then feed that into the model again

        _inputStartTime = np.append(inputStartTime, newST)
        _inputStartTime = np.delete(_inputStartTime, 0)

        _inputPitches = np.append(inputPitches, newP)
        _inputPitches = np.delete(_inputPitches, 0)

        _inputVelocities = np.append(inputVelocities, newV)
        _inputVelocities = np.delete(_inputVelocities, 0)

        _inputDurations = np.append(inputDurations, newD)
        _inputDurations = np.delete(_inputDurations, 0)

        for i in tqdm(range(lengthDesired)):
            outputArray = model(
                {
                    "startTimes": np.reshape(_inputStartTime, (1, -1)),
                    "pitches": np.reshape(_inputPitches, (1, -1)),
                    "velocities": np.reshape(_inputVelocities, (1, -1)),
                    "durations": np.reshape(_inputDurations, (1, -1)),
                }
            )

            newST = outputArray[0].numpy()[0]
            newP = outputArray[1].numpy()[0]
            if newP < 20:
                newP = np.random.randint(20, 88)
            newV = outputArray[2].numpy()[0]
            newD = outputArray[3].numpy()[0]

            outputSTArray = np.append(outputSTArray, newST)
            outputPArray = np.append(outputPArray, newP)
            outputVArray = np.append(outputVArray, newV)
            outputDArray = np.append(outputDArray, newD)

            _inputStartTime = np.append(_inputStartTime, newST)
            _inputStartTime = np.delete(_inputStartTime, 0)

            _inputPitches = np.append(_inputPitches, newP)
            _inputPitches = np.delete(_inputPitches, 0)

            _inputVelocities = np.append(_inputVelocities, newV)
            _inputVelocities = np.delete(_inputVelocities, 0)

            _inputDurations = np.append(_inputDurations, newD)
            _inputDurations = np.delete(_inputDurations, 0)

        finalOutputArray = np.column_stack(
            (
                (outputSTArray - np.min(outputSTArray)),
                outputPArray.astype(int),
                outputVArray,
                outputDArray,
            )
        )
        # sort by first column
        finalOutputArray = finalOutputArray[finalOutputArray[:, 0].argsort()]
        #
        return finalOutputArray

    def saveArrayAsMidi(self, outputArray, path_to_save):
        # Write array to PrettyMidi and then save as midi file
        # Create a PrettyMIDI object
        midi_data = PrettyMIDI()
        midi_data.instruments.append(Instrument(0))
        for i in range(len(outputArray)):
            midi_data.instruments[0].notes.append(
                Note(
                    velocity=int(outputArray[i, 2]),
                    pitch=int(outputArray[i, 1]),
                    start=outputArray[i, 0],
                    end=outputArray[i, 0] + outputArray[i, 3],
                )
            )
        midi_data.write(path_to_save)


# %%
