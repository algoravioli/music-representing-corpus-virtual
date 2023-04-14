import numpy as np
import matplotlib.font_manager

from pprint import pprint

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer

for numScore in range(1):
    GLOBAL_SAVENAME = (
        f"Concert-Section 4-(Environment).png"  # change this to whatever you want
    )

    canvas, staffLineCoords = createcanvas.returnCanvas(
        "A4", "portrait", saveRawCanvas=False, indentation=True
    )
    noter = notationplacer.notationPlacer(canvas, staffLineCoords)
    canvas = noter.applyTrebleClef(canvas, 0, on_all=True)
    # pprint(staffLineCoords)

    # system_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
    # pprint(system_fonts)
    # add title for page
    canvas = noter.addTitle(canvas, f"Environment")
    canvas = noter.addComposer(
        canvas, "Chris Clarke", pageAlignValue=4.75
    )  # adjust this page align value to move the composer name
    canvas = noter.addInstrumentTextAtIndent(
        canvas, "Saxophone     ", staffLineCoords, 0
    )

    # Instead, best practice is to come up with an array of notes, an array of etc other details, and sort some of them first.

    # This is the array of notes to be played, does not need to be sorted
    notesArray = np.arange(58, 88)
    # notesArray = np.append(notesArray, np.zeros(50 - (numScore * 5)))
    notes = np.random.choice(notesArray, size=72)
    # This is the array of sharp or flat, does not need to be sorted
    sharpOrFlat = np.random.choice(["sharp", "flat"], size=72)
    # This is the array of fractions, this needs to be sorted in a specific way, for example, if we want 5 notes per system.
    # We can split the array into 5 groups, and then sort each group in ascending order.
    horzPositions = np.random.random_sample(size=72) * 0.8 + 0.1
    # sorting this array into 5 groups of 9 elements each, and then sorting each group in ascending order
    horzPositions = np.sort(horzPositions.reshape(9, 8), axis=1)
    # Since we know that we wil have 5 notes per system, we need to repeat numbers 1-N 5 times each in an array.
    arrayOfSystemNumbers = np.repeat(np.arange(0, 9), 8)
    # To prove that we have done things correctly, or if we just want to have a look at the generated numbers:
    # uncomment the following lines:
    # print(notes)
    # print(sharpOrFlat)
    # print(horzPositions)
    # print(arrayOfSystemNumbers)

    # Now that we have our arrays, we can loop through them and apply the notes to the canvas.
    # for i in range(len(notes)):
    #     if notes[i] == 0:
    #         continue
    #     else:
    #         canvas = noter.applyNoteheadAt(
    #             canvas,
    #             arrayOfSystemNumbers[i],
    #             horzPositions[arrayOfSystemNumbers[i], i % 8],
    #             int(notes[i]),
    #             sharp_or_flat=sharpOrFlat[i],
    #             notehead_type=np.random.choice(
    #                 [
    #                     "normal",
    #                     # "square",
    #                     # "diamond",
    #                     # "diamond_empty",
    #                     # "triangle_empty",
    #                     # "triangle",
    #                     # "smiley",
    #                 ]
    #             ),
    #         )

    # dictionaryOfPlacedNotes, numberOfPlacedNotes = noter.getPlacedNotes()
    # pprint(dictionaryOfPlacedNotes)
    width, height = canvas.size
    canvas = noter.addTextAt(
        canvas, "COOL SOUNDS", width / 3.5 , height / 2, fontsize=50
    )

    width, height = canvas.size
    print(f"Canvas size: {width} x {height} pixels")

    canvas.save(GLOBAL_SAVENAME)
    print(f"{GLOBAL_SAVENAME} saved to disk.")

# %%
