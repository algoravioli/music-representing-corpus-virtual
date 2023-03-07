# %%
from PIL import Image, ImageDraw
import numpy as np

import helperfunctions.papersizefunctions as psf
import helperfunctions.drawmanuscriptlines as dml

# setup the image size and canvas
width, height = psf.getPaperSize("A3", "portrait")
canvas = Image.new("RGB", (width, height), "white")

canvas = dml.DrawStaffLines(canvas)

# export the canvas
canvas.save("test.png")

# %%
