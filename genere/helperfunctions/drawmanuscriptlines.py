from PIL import Image, ImageDraw
from pprint import pprint

GLOBAL_MARGINS = [35 / 559, 120 / 794]
GLOBAL_STAFF_MARGINS = 50 / 794
GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS = 8  # best to be even number
GLOBAL_LINE_THICKNESS = 2  # CAN ONLY BE INTEGERS
GLOBAL_INDENTATION_IN_PIXELS = 137 / 559


def OneSetOfLines(canvas, start_x, start_y, count=1, indentation_or_not=False):
    drawer = ImageDraw.Draw(canvas)
    width, height = canvas.size
    # for cleaning the page up and preventing decimal place pixels
    start_y = int(start_y)
    start_x = int(start_x)
    # Return start and end coordinates of staff lines

    for i in range(5):
        indentation = 0
        if count == 0:
            if indentation_or_not:
                indentation = int(GLOBAL_INDENTATION_IN_PIXELS * width)
            else:
                indentation = 0
        coords = [[start_x + indentation, start_y]]
        drawer.line(
            (
                start_x + indentation,
                start_y + (i * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS),
                width - int((GLOBAL_MARGINS[0] * width)),
                start_y + (i * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS),
            ),
            fill=(0, 0, 0),
            width=GLOBAL_LINE_THICKNESS,
        )
        if i == 4:
            coords.append(
                [
                    width - int((GLOBAL_MARGINS[0] * width)),
                    start_y + (i * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS),
                ]
            )

    return canvas, coords


def DrawStaffLines(canvas, staff_margin=GLOBAL_STAFF_MARGINS, indentation=False):
    drawer = ImageDraw.Draw(canvas)
    width, height = canvas.size
    # calculate how many sets of lines, given a staff margin
    calcFlag = True
    start_y_Array = []
    while calcFlag:
        if len(start_y_Array) == 0:
            start_y_Array.append(int(GLOBAL_MARGINS[1] * height))
        else:
            currentEntry = int(
                (
                    start_y_Array[-1]
                    + (4 * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS)
                    + (staff_margin * height)
                )
            )
            if currentEntry > (
                height
                # - (3 * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS)
                - (GLOBAL_MARGINS[1] * height * 0.66)
            ):
                calcFlag = False

            else:
                start_y_Array.append(currentEntry)
    # initialize the dictionary of staff line coordinates
    staffLineCoords = {}
    # draw the staff lines
    for i in range(len(start_y_Array)):
        canvas, coords = OneSetOfLines(
            canvas,
            GLOBAL_MARGINS[0] * width,
            start_y_Array[i],
            count=i,
            indentation_or_not=indentation,
        )
        staffLineCoords[i] = coords
    return canvas, staffLineCoords
    # draw the staff lines
