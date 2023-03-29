import numpy as np
import matplotlib.font_manager

from pprint import pprint

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer
from genere.stochastic_processes import markovmodels

GLOBAL_SAVENAME = "markovmodel_score.png"  # change this to whatever you want

canvas, staffLineCoords = createcanvas.returnCanvas(
    "A4", "portrait", saveRawCanvas=False, indentation=True
)
noter = notationplacer.notationPlacer(canvas, staffLineCoords)
canvas = noter.applyTrebleClef(canvas, 0, on_all=True)
# pprint(staffLineCoords)

# system_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# pprint(system_fonts)
# add title for page
canvas = noter.addTitle(canvas, "Markov Model In Action")
canvas = noter.addComposer(
    canvas, "Composer Name", pageAlignValue=4.75
)  # adjust this page align value to move the composer name
canvas = noter.addInstrumentTextAtIndent(
    canvas, "Instrument Name   ", staffLineCoords, 0
)

markov = markovmodels.MarkovModel()
rhythms, pitch, abspitch, octaves = markov.learnFromMidi(
    "neural_nets/data/2013/ORIG-MIDI_01_7_6_13_Group__MID--AUDIO_01_R1_2013_wav--2.midi"
)
# markov.plotMatrices()  # uncomment this to see the matrices


# we set the starting system to 0, and the starting fraction to 0.1
currentSystem = 0
currentFraction = 0.1
for i in range(
    100
):  # we use a length that is more than we need, see line 65 as we use that to prevent going out of bounds
    # as we go through, we add to the current fraction, and if it gets too big, we move to the next system
    outputPitch, outputRhythm, outputOctave = markov.returnNextPitch()
    currentFraction = currentFraction + (
        outputRhythm / 5
    )  # we can add a scaling value like this /3 operation for the position of the notes
    if i == 0:
        currentFraction = 0.1
    elif currentFraction > 0.9:
        currentSystem = currentSystem + 1
        currentFraction = 0.1

    # we will add safety condition since our max midi number is between 48 and 92
    if outputPitch == 0:
        outputPitch = 12
    if outputPitch * outputOctave > 92:
        while outputPitch * outputOctave > 92:
            outputOctave = outputOctave - 1

    elif outputPitch * outputOctave < 70:
        while outputPitch * outputOctave < 70:
            outputOctave = outputOctave + 1

    if currentSystem < len(staffLineCoords):
        canvas = noter.applyNoteheadAt(
            canvas,
            currentSystem,
            currentFraction,
            outputPitch * outputOctave,
            sharp_or_flat=np.random.choice(["sharp", "flat"]),
        )

canvas.save(GLOBAL_SAVENAME)
print(f"{GLOBAL_SAVENAME} saved to disk.")
