import numpy as np
import pretty_midi
import matplotlib.pyplot as plt
import pandas as pd
from pprint import pprint


class MarkovModel:
    def __init__(self) -> None:
        self.previousPitch = None
        self.previousRhythm = None
        self.previousOctave = None

    def transitionMatrix(self, transitions):
        unique, counts = np.unique(transitions, return_counts=True)
        n = len(np.unique(transitions))  # number of states

        M = [[0] * n for _ in range(n)]

        for i, j in zip(transitions, transitions[1:]):
            index_i = np.where(unique == i)[0][0]
            index_j = np.where(unique == j)[0][0]
            M[index_i][index_j] += 1

        # now convert to probabilities:
        for row in M:
            s = sum(row)
            if s > 0:
                row[:] = [f / s for f in row]
        return M

    def learnFromMidi(self, path):
        midiObject = pretty_midi.PrettyMIDI(path)
        self.midiObject = midiObject
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

        # now we need to find the transition matrix for the rhythm
        self.arrayOfDifferences = np.diff(np.sort(self.start_time))
        # remove entries that are 0 in the array
        self.arrayOfDifferences = np.around(self.arrayOfDifferences, 1)
        self.arrayOfDifferences = self.arrayOfDifferences[self.arrayOfDifferences != 0]
        self.arrayOfDifferences = self.arrayOfDifferences[self.arrayOfDifferences > 0.2]

        self.rhythmMatrix = self.transitionMatrix(self.arrayOfDifferences)

        # now we need to find the transition matrix for the pitch
        # convert midi number to pitch class (0-11)
        pitchMatrixInputs = self.pitch % 12
        self.pitchMatrix = self.transitionMatrix(pitchMatrixInputs)

        self.absolutePitchMatrix = self.transitionMatrix(self.pitch)

        # we also need an octave matrix
        self.octaves = self.pitch % 12
        self.octaveMatrix = self.transitionMatrix(self.octaves)

        return (
            self.rhythmMatrix,
            self.pitchMatrix,
            self.absolutePitchMatrix,
            self.octaveMatrix,
        )

    def returnPianoRoll(self):
        return self.notes

    def plotMatrices(self):
        fig, axs = plt.subplots(2, 2, figsize=(8, 8))

        fig.suptitle("Matrices of Markov Model")
        arrayOfMatrices = [
            self.rhythmMatrix,
            self.pitchMatrix,
            self.absolutePitchMatrix,
            self.octaveMatrix,
        ]
        arrayOfNames = ["Rhythm", "Pitch", "Absolute Pitch", "Octaves"]
        subplotArray = [[0, 0], [0, 1], [1, 0], [1, 1]]
        for i in range(len(arrayOfMatrices)):
            plot_mat = arrayOfMatrices[i]
            plot_df = pd.DataFrame(data=plot_mat)
            im = axs[subplotArray[i][0], subplotArray[i][1]].matshow(plot_df)
            axs[subplotArray[i][0], subplotArray[i][1]].set_title(f"{arrayOfNames[i]}")
            plt.colorbar(im, ax=axs[subplotArray[i][0], subplotArray[i][1]])

        plt.show()

    def returnNextPitch(self):
        if self.previousPitch == None:
            self.previousPitch = int(np.random.choice(self.pitch))
            self.previousRhythm = np.random.choice(self.arrayOfDifferences)
            self.previousOctave = int(np.random.choice(self.octaves))

            outputPitch = self.previousPitch
            outputRhythm = self.previousRhythm
            outputOctave = self.previousOctave
        else:
            outputPitch = int(
                np.random.choice(
                    np.arange(0, len(self.pitchMatrix[0])),
                    p=self.pitchMatrix[self.previousPitch % 12],
                )
            )
            self.previousPitch = outputPitch

            rhythmUnique = np.unique(self.arrayOfDifferences)
            rhythmIndex = np.where(np.isclose(rhythmUnique, self.previousRhythm))
            outputRhythmIndex = np.random.choice(
                np.arange(0, len(rhythmUnique)),
                p=self.rhythmMatrix[rhythmIndex[0][0]],
            )
            self.previousRhythm = rhythmUnique[outputRhythmIndex]
            outputRhythm = self.previousRhythm

            outputOctave = int(
                np.random.choice(
                    np.arange(0, len(self.octaveMatrix[0])),
                    p=self.octaveMatrix[self.previousOctave],
                )
            )
            self.previousOctave = outputOctave

        return outputPitch, outputRhythm, outputOctave
