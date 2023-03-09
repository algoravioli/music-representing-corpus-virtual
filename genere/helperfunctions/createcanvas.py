# %%
from PIL import Image, ImageDraw
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import papersizefunctions
import numpy as np


def returnCanvas(paper_size, orientation, saveRawCanvas=False):
    width, height = papersizefunctions.getPaperSize(paper_size, orientation)
    canvas = Image.new("RGB", (width, height), "white")
    canvas, staffLinesCoords = drawmanuscriptlines.DrawStaffLines(canvas)
    # Following is for debugging is PIL is messing up or not
    if saveRawCanvas:
        canvas.save("staffLinesOnly.png")

    # Also needs to return a dictionary of (x,y) coordinates for the staff boundaries
    # This comes from dml.DrawStaffLines
    return canvas, staffLinesCoords
