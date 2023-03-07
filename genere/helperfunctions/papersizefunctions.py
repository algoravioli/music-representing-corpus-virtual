# This file holds paper sizes functions.


# always returns in width by height (order)
def getPaperSize(function_name, landscape_or_portrait):
    if function_name == "A4":
        width, height = A4(landscape_or_portrait)
    elif function_name == "A3":
        width, height = A3(landscape_or_portrait)
    elif function_name == "A5":
        width, height = A5(landscape_or_portrait)
    else:
        return None
    return width, height


def A5(landscape_or_portrait):
    L1 = 559
    L2 = 794
    if landscape_or_portrait == "landscape":
        return L2, L1
    elif landscape_or_portrait == "portrait":
        return L1, L2


def A4(landscape_or_portrait):

    L1 = 794
    L2 = 1123
    if landscape_or_portrait == "landscape":
        return L2, L1
    elif landscape_or_portrait == "portrait":
        return L1, L2


def A3(landscape_or_portrait):
    L1 = 1123
    L2 = 1587
    if landscape_or_portrait == "landscape":
        return L2, L1
    elif landscape_or_portrait == "portrait":
        return L1, L2


def getInitialWithMargin(width, height):
    # based on A5 calculations
    # height = 100 from top
    # width = 55 from left
    initials = {
        "start_x": 55 / 559 * width,
        "start_y": 100 / 794 * height,
    }
    return initials
