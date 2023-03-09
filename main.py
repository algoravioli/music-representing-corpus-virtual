# %%
from PIL import Image, ImageDraw
import numpy as np

from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import createcanvas
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import notationplacer

# debugging only
from pprint import pprint

# pprint(os.listdir("."))
import os


noter = notationplacer.notationPlacer()

# setup the image size and canvas
canvas, staffLineCoords = createcanvas.returnCanvas(
    "A4", "portrait", saveRawCanvas=False
)

pprint(staffLineCoords)


out = noter.applyNoteheadAtCoord(canvas, 88, 208)
out = noter.drawLedgerLines(out, 85, 201)
out = noter.drawLedgerLines(out, 85, 213)


# what i really want is to be able to do this:
# give some fraction of bar and note intended (eg. F#)
# and it will place the notehead at the correct position

# ledger line will always be 5 pixels below the notehead

# C4 = 196 plus ledger lines
# D4 = 191
# E4 = 184
# F4 = 178
# G4 = 172
# A4 = 166
# B4 = 160
# C5 = 154
# D5 = 148
# E5 = 142
# F5 = 136
# G5 = 130
# A5 = 124


out.save("test.png")
pprint("test.png saved to disk.")

# %%
