# %%
from PIL import Image, ImageDraw
import numpy as np
import time

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer

# debugging only
# from pprint import pprint

startTime = time.time()
# setup the image size and canvas
canvas, staffLineCoords = createcanvas.returnCanvas(
    "A4", "portrait", saveRawCanvas=False, indentation=False
)
noter = notationplacer.notationPlacer(canvas, staffLineCoords)
# pprint(staffLineCoords)

# apply treble clef
canvas = noter.applyTrebleClef(canvas, 0, on_all=True)

# This could be how you do it, but it is not good at keeping track of the chronological order of the notes performed.

# for i in range(20):
#     randomNote = np.random.randint(55, 80)
#     randomSharpOrFlat = np.random.choice(["sharp", "flat"])
#     randomFraction = np.random.random_sample() * 0.8 + 0.1
#     randomSystem = np.random.randint(0, len(staffLineCoords))
#     canvas = noter.applyNoteheadAt(
#         canvas,
#         randomSystem,
#         randomFraction,
#         randomNote,
#         sharp_or_flat=randomSharpOrFlat,
#     )

# Instead, best practice is to come up with an array of notes, an array of etc other details, and sort some of them first.

# This is the array of notes to be played, does not need to be sorted
notes = np.random.randint(55, 80, size=45)
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


canvas.save("test.png")
print("test.png saved to disk.")
endTime = time.time()
print(f"Time taken: {endTime - startTime} seconds.")
# %%
