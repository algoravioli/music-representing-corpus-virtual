# %%
from PIL import Image, ImageDraw
import numpy as np
import time

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer

canvas, staffLineCoords = createcanvas.returnCanvas(
    "A4", "portrait", saveRawCanvas=False, indentation=False
)
noter = notationplacer.notationPlacer(canvas, staffLineCoords)
canvas = noter.applyTrebleClef(canvas, 0, on_all=True)
notes = np.random.randint(55, 80, size=45)
sharpOrFlat = np.random.choice(["sharp", "flat"], size=45)
horzPositions = np.random.random_sample(size=45) * 0.8 + 0.1
horzPositions = np.sort(horzPositions.reshape(9, 5), axis=1)
arrayOfSystemNumbers = np.repeat(np.arange(0, 9), 5)
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
# %%
