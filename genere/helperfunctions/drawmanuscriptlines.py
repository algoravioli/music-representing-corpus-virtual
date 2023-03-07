from PIL import Image, ImageDraw

GLOBAL_MARGINS = [55 / 559, 100 / 794]
GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS = 12
GLOBAL_LINE_THICKNESS = 3  # CAN ONLY BE INTEGERS


def OneSetOfLines(canvas, start_x, start_y):
    drawer = ImageDraw.Draw(canvas)
    width, height = canvas.size
    for i in range(5):
        drawer.line(
            (
                start_x,
                start_y + (i * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS),
                width - int((GLOBAL_MARGINS[0] * width)),
                start_y + (i * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS),
            ),
            fill=(0, 0, 0),
            width=GLOBAL_LINE_THICKNESS,
        )
    return canvas


def DrawStaffLines(canvas, staff_margin=100):
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
                    + staff_margin
                )
            )
            start_y_Array.append(currentEntry)
            if currentEntry > height - 1.5 * (GLOBAL_MARGINS[1] * height):
                calcFlag = False

    print(start_y_Array)
    for i in range(len(start_y_Array)):
        canvas = OneSetOfLines(canvas, GLOBAL_MARGINS[0] * width, start_y_Array[i])
    return canvas
    # draw the staff lines
