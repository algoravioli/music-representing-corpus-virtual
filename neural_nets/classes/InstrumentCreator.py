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
        length_of_note=0.5,
        path_to_save="audio_output/neural_net2_audio",
    ):
        num_samples = length_of_note * Fs
        num_iterations = int(num_samples // block_size)
        outputArray = np.array([])
        # Using a for loop for each note, we will run inference on the model to create a 1 second long file
        for i in range(num_notes):
            print(f"Current Note: {i}")
            rng = np.random.default_rng()
            # We will create a random sum of sines as input of block_size samples for input to the model each time the loop runs
            howManyFreqs = np.random.randint(1, 2)
            # cast to array of sines
            for k in range(howManyFreqs):
                t = np.linspace(0, block_size, block_size)
                frequency = (2 ** (i - 69)) / 12 * (440)
                currentSine = np.sin(2 * np.pi * frequency * t / Fs)
                if k == 0:
                    inputArray = currentSine
                else:
                    inputArray = inputArray + currentSine

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

    def export_audio_from_train_data(
        self,
        model,
        inputArray,
        block_size=1000,
        Fs=44100,
        num_samples=1,
        path_to_save="audio_output/neural_net2_audio",
    ):
        outputArray = np.array([])
        num_samples = num_samples
        # We will then write the outputArray to a wav file
        # Some sanity code to check if our file exists:
        # if it does not exist, we will make a new directory called "neural_net2_audio"
        if not os.path.exists(path_to_save):
            os.mkdir(path_to_save)

        for i in tqdm(range(num_samples)):
            print(f"Current Note: {i}")
            outputArray = model.predict(
                np.reshape(inputArray[i], (1, block_size)), verbose=0
            )
            while len(outputArray) < 44100:
                outputArray = np.append(outputArray, outputArray)
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

        # We will then copy the background image to the new directory
        shutil.copyfile(
            "../neural_nets/decentsampler_instruments/background_default.png",
            f"{path_to_save}/Samples/background.png",
        )
        # We will then start with the xml file creation
        listOfAudio = os.listdir(path_to_audio)
        if ".DS_Store" in listOfAudio:
            listOfAudio.remove(".DS_Store")

        print("The audio files chosen are: ", listOfAudio)

        # This is just boilerplate for the xml file
        xmlFile = "<?xml version=" + '"1.0"' + " encoding=" + '"UTF-8"' + "?>" + "\n"
        xmlFile += "<DecentSampler>" + "\n"
        xmlFile += (
            "\t"
            + '<ui bgImage="Samples/background.png" width="812" height="375" layoutMode="relative" bgMode="top_left"> + "\n"'
        )
        xmlFile += "\t\t" + '<tab name="main">' + "\n"
        # ATTACK
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="385" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Attack" type="float" minValue="0.01" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_ATTACK"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # DECAY
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="450" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Decay" type="float" minValue="0.0" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_DECAY"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # SUSTAIN
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="515" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Sustain" type="float" minValue="0.0" maxValue="1.0" value="1.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_SUSTAIN"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # RELEASE
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="580" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Release" type="float" minValue="0.0" maxValue="20.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_RELEASE"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"

        xmlFile += "\t\t" + "</tab>" + "\n"
        xmlFile += "\t" + "</ui>" + "\n"
        xmlFile += (
            "\t" + '<groups attack="0.3" decay="0.5" sustain="1.0" release="2">' + "\n"
        )
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
                # + f'loopStart="0" '
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

    def create_decent_sampler_xml_from_1_sample(
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

        # We will then copy the background image to the new directory
        shutil.copyfile(
            "../neural_nets/decentsampler_instruments/background_default.png",
            f"{path_to_save}/Samples/background.png",
        )
        # We will then start with the xml file creation
        listOfAudio = os.listdir(path_to_audio)
        if ".DS_Store" in listOfAudio:
            listOfAudio.remove(".DS_Store")

        print("The audio files chosen are: ", listOfAudio)

        # This is just boilerplate for the xml file
        xmlFile = "<?xml version=" + '"1.0"' + " encoding=" + '"UTF-8"' + "?>" + "\n"
        xmlFile += "<DecentSampler>" + "\n"
        xmlFile += (
            "\t"
            + '<ui bgImage="Samples/background.png" width="812" height="375" layoutMode="relative" bgMode="top_left"> + "\n"'
        )
        xmlFile += "\t\t" + '<tab name="main">' + "\n"
        # ATTACK
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="385" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Attack" type="float" minValue="0.01" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_ATTACK"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # DECAY
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="450" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Decay" type="float" minValue="0.0" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_DECAY"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # SUSTAIN
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="515" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Sustain" type="float" minValue="0.0" maxValue="1.0" value="1.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_SUSTAIN"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # RELEASE
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="580" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Release" type="float" minValue="0.0" maxValue="20.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_RELEASE"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"

        xmlFile += "\t\t" + "</tab>" + "\n"
        xmlFile += "\t" + "</ui>" + "\n"
        xmlFile += (
            "\t" + '<groups attack="0.3" decay="0.5" sustain="1.0" release="2">' + "\n"
        )
        xmlFile += "\t\t" + "<group>" + "\n"
        for i in range(len(listOfAudio)):
            # We will copy the audio files to the new directory
            shutil.copy2(
                f"{path_to_audio}/{listOfAudio[i]}", f"{path_to_save}/Samples/"
            )
            xmlFile += (
                "\t\t\t"
                + f'<sample rootNote="'
                + f'60" '
                + f'loNote="0" '
                + f'hiNote="127" '
                + f'loopEnabled="True" '
                # + f'loopStart="0" '
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

    def create_decent_sampler_xml_for_neural_net_4(
        self,
        input,
        model,
        path_to_audio="../neural_nets/audio_output/neural_net4_audio",
        path_to_save="decentsampler_instruments/CreatedInstrumentNN4 [Decent Sampler]",
    ):
        # We will first create the directory to save the audio
        if not os.path.exists(path_to_audio):
            os.makedirs(path_to_audio)
        # We will then create the directory to save the instrument
        if not os.path.exists(path_to_save):
            os.makedirs(path_to_save)

        if not os.path.exists(f"{path_to_save}/Samples"):
            os.mkdir(f"{path_to_save}/Samples")

        # We will then copy the background image to the new directory
        shutil.copyfile(
            "../neural_nets/decentsampler_instruments/background_default.png",
            f"{path_to_save}/Samples/background.png",
        )

        outputArray = model(input)
        outputArray = outputArray.numpy()
        outputArray = outputArray[0][0]
        while len(outputArray) < 44100:
            outputArray = np.append(outputArray, outputArray)

        write(
            f"{path_to_audio}/noteNumber_0.wav",
            44100,
            outputArray.astype(np.float32)
            / (np.max(np.abs(outputArray))),  # Normalizing for fun
        )

        listOfAudio = os.listdir(path_to_audio)
        if ".DS_Store" in listOfAudio:
            listOfAudio.remove(".DS_Store")
        # We will then create the instrument
        # This is just boilerplate for the xml file
        xmlFile = "<?xml version=" + '"1.0"' + " encoding=" + '"UTF-8"' + "?>" + "\n"
        xmlFile += "<DecentSampler>" + "\n"
        xmlFile += (
            "\t"
            + '<ui bgImage="Samples/background.png" width="812" height="375" layoutMode="relative" bgMode="top_left"> + "\n"'
        )
        xmlFile += "\t\t" + '<tab name="main">' + "\n"
        # ATTACK
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="385" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Attack" type="float" minValue="0.01" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_ATTACK"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # DECAY
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="450" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Decay" type="float" minValue="0.0" maxValue="4.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_DECAY"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # SUSTAIN
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="515" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Sustain" type="float" minValue="0.0" maxValue="1.0" value="1.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_SUSTAIN"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"
        # RELEASE
        xmlFile += (
            "\t\t\t"
            + '<labeled-knob x="580" y="75" width="90" textSize="16" textColor="AA000000" trackForegroundColor="CC000000" trackBackgroundColor="66999999" label="Release" type="float" minValue="0.0" maxValue="20.0" value="0.0">'
            + "\n"
        )
        xmlFile += (
            "\t\t\t\t"
            + '<binding type="amp" level="instrument" position="0" parameter="ENV_RELEASE"/>'
            + "\n"
        )
        xmlFile += "\t\t\t" + "</labeled-knob>" + "\n"

        xmlFile += "\t\t" + "</tab>" + "\n"
        xmlFile += "\t" + "</ui>" + "\n"
        xmlFile += (
            "\t" + '<groups attack="0.3" decay="0.5" sustain="1.0" release="2">' + "\n"
        )
        xmlFile += "\t\t" + "<group>" + "\n"
        for i in range(len(listOfAudio)):
            # We will copy the audio files to the new directory
            shutil.copy2(
                f"{path_to_audio}/{listOfAudio[i]}", f"{path_to_save}/Samples/"
            )
            xmlFile += (
                "\t\t\t"
                + f'<sample rootNote="'
                + f'60" '
                + f'loNote="0" '
                + f'hiNote="127" '
                + f'loopEnabled="True" '
                # + f'loopStart="0" '
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
            f"{path_to_save}/Created InstrumentNN4 [Decent Sampler].dspreset", "w"
        ) as f:
            f.write(xmlFile)

        return outputArray
