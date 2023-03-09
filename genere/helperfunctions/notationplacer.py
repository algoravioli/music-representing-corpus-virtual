# %%
from PIL import Image, ImageDraw
import numpy as np

# import helper functions
from genere.helperfunctions import papersizefunctions
from genere.helperfunctions import drawmanuscriptlines
from genere.helperfunctions import createcanvas

import os

GLOBAL_MARGINS = [55 / 559, 100 / 794]
GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS = 12
GLOBAL_LINE_THICKNESS = 2  # CAN ONLY BE INTEGERS


class notationPlacer:
    def __init__(self):
        print(os.listdir("."))
        self.notePostiionsVerticalRatios = {
            "-Cb": [(242 - 141) / (189 - 141), "flat", 4],
            "-C": [(242 - 141) / (189 - 141), "natural", 4],
            "-C#": [(242 - 141) / (189 - 141), "sharp", 4],
            "-Db": [(236 - 141) / (189 - 141), "flat", 4],
            "-D": [(236 - 141) / (189 - 141), "natural", 4],
            "-D#": [(236 - 141) / (189 - 141), "sharp", 4],
            "-Eb": [(230 - 141) / (189 - 141), "flat", 3],
            "-E": [(230 - 141) / (189 - 141), "natural", 3],
            "-E#": [(230 - 141) / (189 - 141), "sharp", 3],
            "-Fb": [(224 - 141) / (189 - 141), "flat", 3],
            "-F": [(224 - 141) / (189 - 141), "natural", 3],
            "-F#": [(224 - 141) / (189 - 141), "sharp", 3],
            "-Gb": [(216 - 141) / (189 - 141), "flat", 2],
            "-G": [(216 - 141) / (189 - 141), "natural", 2],
            "-G#": [(216 - 141) / (189 - 141), "sharp", 2],
            "-Ab": [(208 - 141) / (189 - 141), "flat", 2],
            "-A": [(208 - 141) / (189 - 141), "natural", 2],
            "-A#": [(208 - 141) / (189 - 141), "sharp", 2],
            "-Bb": [(202 - 141) / (189 - 141), "flat", 1],
            "-B": [(202 - 141) / (189 - 141), "natural", 1],
            "-B#": [(202 - 141) / (189 - 141), "sharp", 1],
            "Cb": [(196 - 141) / (189 - 141), "flat", 1],
            "C": [(196 - 141) / (189 - 141), "natural", 1],
            "C#": [(196 - 141) / (189 - 141), "sharp", 1],
            "Db": [(191 - 141) / (189 - 141), "flat", 0],
            "D": [(191 - 141) / (189 - 141), "natural", 0],
            "D#": [(191 - 141) / (189 - 141), "sharp", 0],
            "Eb": [(184 - 141) / (189 - 141), "flat", 0],
            "E": [(184 - 141) / (189 - 141), "natural", 0],
            "E#": [(184 - 141) / (189 - 141), "sharp", 0],
            "Fb": [(1141 - 141) / (189 - 141), "flat", 0],
            "F": [(1141 - 141) / (189 - 141), "natural", 0],
            "F#": [(1141 - 141) / (189 - 141), "sharp", 0],
            "Gb": [(172 - 141) / (189 - 141), "flat", 0],
            "G": [(172 - 141) / (189 - 141), "natural", 0],
            "G#": [(172 - 141) / (189 - 141), "sharp", 0],
            "Ab": [(166 - 141) / (189 - 141), "flat", 0],
            "A": [(166 - 141) / (189 - 141), "natural", 0],
            "A#": [(166 - 141) / (189 - 141), "sharp", 0],
            "Bb": [(160 - 141) / (189 - 141), "flat", 0],
            "B": [(160 - 141) / (189 - 141), "natural", 0],
            "B#": [(160 - 141) / (189 - 141), "sharp", 0],
            "+Cb": [(154 - 141) / (189 - 141), "flat", 0],
            "+C": [(154 - 141) / (189 - 141), "natural", 0],
            "+C#": [(154 - 141) / (189 - 141), "sharp", 0],
            "+Db": [(148 - 141) / (189 - 141), "flat", 0],
            "+D": [(148 - 141) / (189 - 141), "natural", 0],
            "+D#": [(148 - 141) / (189 - 141), "sharp", 0],
            "+Eb": [(142 - 141) / (189 - 141), "flat", 0],
            "+E": [(142 - 141) / (189 - 141), "natural", 0],
            "+E#": [(142 - 141) / (189 - 141), "sharp", 0],
            "+Fb": [(136 - 141) / (189 - 141), "flat", 0],
            "+F": [(136 - 141) / (189 - 141), "natural", 0],
            "+F#": [(136 - 141) / (189 - 141), "sharp", 0],
            "+Gb": [(130 - 141) / (189 - 141), "flat", 0],
            "+G": [(130 - 141) / (189 - 141), "natural", 0],
            "+G#": [(130 - 141) / (189 - 141), "sharp", 0],
            "+Ab": [(124 - 141) / (189 - 141), "flat", 1],
            "+A": [(124 - 141) / (189 - 141), "natural", 1],
            "+A#": [(124 - 141) / (189 - 141), "sharp", 1],
            "+Bb": [(118 - 141) / (189 - 141), "flat", 1],
            "+B": [(118 - 141) / (189 - 141), "natural", 1],
            "+B#": [(118 - 141) / (189 - 141), "sharp", 1],
            "++Cb": [(112 - 141) / (189 - 141), "flat", 2],
            "++C": [(112 - 141) / (189 - 141), "natural", 2],
            "++C#": [(112 - 141) / (189 - 141), "sharp", 2],
            "++Db": [(106 - 141) / (189 - 141), "flat", 2],
            "++D": [(106 - 141) / (189 - 141), "natural", 2],
            "++D#": [(106 - 141) / (189 - 141), "sharp", 2],
            "++Eb": [(100 - 141) / (189 - 141), "flat", 3],
            "++E": [(100 - 141) / (189 - 141), "natural", 3],
            "++E#": [(100 - 141) / (189 - 141), "sharp", 3],
            "++Fb": [(94 - 141) / (189 - 141), "flat", 3],
            "++F": [(94 - 141) / (189 - 141), "natural", 3],
            "++F#": [(94 - 141) / (189 - 141), "sharp", 3],
            "++Gb": [(88 - 141) / (189 - 141), "flat", 4],
            "++G": [(88 - 141) / (189 - 141), "natural", 4],
            "++G#": [(88 - 141) / (189 - 141), "sharp", 4],
        }
        self.later = 0

    def applyNoteheadAtCoord(self, canvas, x_left, y_top):
        notehead = Image.open("genere/images/notehead_small.png")
        notehead = notehead.resize((11, 11))
        canvas2 = canvas.copy()
        canvas2.paste(notehead, (x_left, y_top), notehead)
        return canvas2

    def drawLedgerLines(self, canvas, start_x, start_y, ledgerLineLength=17):
        drawer = ImageDraw.Draw(canvas)
        drawer.line(
            (
                start_x,
                start_y,
                start_x + ledgerLineLength,
                start_y,
            ),
            fill=(0, 0, 0),
            width=GLOBAL_LINE_THICKNESS,
        )
        return canvas

    def applyNoteheadAt(canvas, fraction, note):
        pass


# %%
