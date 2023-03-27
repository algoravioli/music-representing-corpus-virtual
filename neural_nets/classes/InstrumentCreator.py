import tensorflow as tf
import numpy as np
import os
import shutil

from scipy.io.wavfile import write
from tqdm import tqdm


class DecentSamplerAudioExporter:
    def __init__(self) -> None:
        pass

    def export_audio(
        self,
        model,
        num_notes=1,
        Fs=44100,
        block_size=1000,
        length_of_note=1,
        path_to_save="audio_output/neural_net2_audio",
    ):
        num_samples = length_of_note * Fs
        num_iterations = int(num_samples // block_size)
        outputArray = np.array([])
        # Using a for loop for each note, we will run inference on the model to create a 1 second long file
        for i in range(num_notes):
            print(f"Current Note: {i}")
            # We will create a random input of block_size samples for input to the model each time the loop runs
            inputArray = np.random.normal(-1, 1, block_size)
            # Using another for loop, this will create the 1 second long file for each note
            for j in tqdm(range(num_iterations)):
                # The output of the model should get passed back into itself as the input for the next iteration
                outputArray = np.append(
                    outputArray,
                    model.predict(np.reshape(inputArray, (1, block_size)), verbose=0),
                )
                inputArray = outputArray[-block_size:]
            # We will then write the outputArray to a wav file
            # Some sanity code to check if our file exists:
            # if it does not exist, we will make a new directory called "neural_net2_audio"
            if not os.path.exists(path_to_save):
                os.mkdir(path_to_save)
            # We will then write the file to the directory
            write(
                f"{path_to_save}/noteNumber_{i}.wav",
                Fs,
                outputArray.astype(np.float32)
                / (np.max(np.abs(outputArray))),  # Normalizing for fun
            )
            # We will then reset the outputArray to an empty array
            outputArray = np.array([])

        print(f"Files have finished exporting at {path_to_save}")

    def create_decent_sampler_xml(
        self,
        path_to_audio,
        path_to_save="decentsampler_instruments/CreatedInstrument [Decent Sampler]",
    ):
        # path_to_audio is the path to the directory where the audio files are stored
        # in the case of neural_net2, the path_to_audio is "audio_output/neural_net2_audio"
        # path_to_save is the path to the directory where the xml file and new audio files will be saved

        # We will first create a new directory to store the newly created instrument files
        # This will be stored under "decentsampler_instruments"

        if not os.path.exists(path_to_save):
            os.mkdir(path_to_save)

        if not os.path.exists(f"{path_to_save}/Samples"):
            os.mkdir(f"{path_to_save}/Samples")

        # We will then start with the xml file creation
        listOfAudio = os.listdir(path_to_audio)
        if ".DS_Store" in listOfAudio:
            listOfAudio.remove(".DS_Store")

        print("The audio files chosen are: ", listOfAudio)

        # This is just boilerplate for the xml file
        xmlFile = "<?xml version=" + '"1.0"' + " encoding=" + '"UTF-8"' + "?>" + "\n"
        xmlFile += "<DecentSampler>" + "\n"
        xmlFile += "\t" + "<groups>" + "\n"
        xmlFile += "\t\t" + "<group>" + "\n"
        for i in range(len(listOfAudio)):
            # We will copy the audio files to the new directory
            shutil.copy2(
                f"{path_to_audio}/{listOfAudio[i]}", f"{path_to_save}/Samples/"
            )
            xmlFile += (
                "\t\t\t"
                + f'<sample rootNote="'
                + f'{i}" '
                + f'loNote="{i}" '
                + f'hiNote="{i}" '
                + f'loopEnabled="True" '
                + f'path="'
                + f"Samples/{listOfAudio[i]}"
                + '"/>'
                + "\n"
            )
        xmlFile += "\t\t" + "</group>" + "\n"
        xmlFile += "\t" + "</groups>" + "\n"
        xmlFile += "</DecentSampler>" + "\n"

        # We will then write the xml file to the new directory
        with open(
            f"{path_to_save}/Created Instrument [Decent Sampler].dspreset", "w"
        ) as f:
            f.write(xmlFile)
