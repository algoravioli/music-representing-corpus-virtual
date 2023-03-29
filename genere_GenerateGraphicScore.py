import numpy as np
import matplotlib.font_manager

from pprint import pprint

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer

GLOBAL_SAVENAME = "graphic_score.png"  # change this to whatever you want

canvas, staffLineCoords = createcanvas.returnCanvas(
    "A4", "portrait", saveRawCanvas=False, indentation=True
)
noter = notationplacer.notationPlacer(canvas, staffLineCoords)
canvas = noter.applyTrebleClef(canvas, 0, on_all=True)
pprint(staffLineCoords)

# system_fonts = matplotlib.font_manager.findSystemFonts(fontpaths=None, fontext="ttf")
# pprint(system_fonts)
# add title for page
canvas = noter.addTitle(canvas, "This Kind of Graphic Score")
canvas = noter.addComposer(
    canvas, "You", pageAlignValue=4.75
)  # adjust this page align value to move the composer name
canvas = noter.addInstrumentTextAtIndent(
    canvas, "Instrument Name   ", staffLineCoords, 0
)

# Instead, best practice is to come up with an array of notes, an array of etc other details, and sort some of them first.

# This is the array of notes to be played, does not need to be sorted
notes = np.random.randint(58, 80, size=45)
# This is the array of sharp or flat, does not need to be sorted
sharpOrFlat = np.random.choice(["sharp", "flat"], size=45)
# This is the array of fractions, this needs to be sorted in a specific way, for example, if we want 5 notes per system.
# We can split the array into 5 groups, and then sort each group in ascending order.
horzPositions = np.random.random_sample(size=45) * 0.8 + 0.1
# sorting this array into 5 groups of 9 elements each, and then sorting each group in ascending order
horzPositions = np.sort(horzPositions.reshape(9, 5), axis=1)
# Since we know that we wil have 5 notes per system, we need to repeat numbers 1-N 5 times each in an array.
arrayOfSystemNumbers = np.repeat(np.arange(0, 9), 5)
# To prove that we have done things correctly, or if we just want to have a look at the generated numbers:
# uncomment the following lines:
# print(notes)
# print(sharpOrFlat)
print(horzPositions)
# print(arrayOfSystemNumbers)

# Now that we have our arrays, we can loop through them and apply the notes to the canvas.
for i in range(len(notes)):
    canvas = noter.applyNoteheadAt(
        canvas,
        arrayOfSystemNumbers[i],
        horzPositions[arrayOfSystemNumbers[i], i % 5],
        int(notes[i]),
        sharp_or_flat=sharpOrFlat[i],
    )

canvas.save(GLOBAL_SAVENAME)
print(f"{GLOBAL_SAVENAME} saved to disk.")
