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

canvas.save(GLOBAL_SAVENAME)
print(f"{GLOBAL_SAVENAME} saved to disk.")
