from pprint import pprint


def returnPositionDictionary():
    dictionary = {
        "-Cb": [(240 - 141) / (189 - 141), "flat", 4, "below"],
        "-C": [(240 - 141) / (189 - 141), "natural", 4, "below"],
        "-C#": [(240 - 141) / (189 - 141), "sharp", 4, "below"],
        "-Db": [(234 - 141) / (189 - 141), "flat", 4, "below"],
        "-D": [(234 - 141) / (189 - 141), "natural", 4, "below"],
        "-D#": [(234 - 141) / (189 - 141), "sharp", 4, "below"],
        "-Eb": [(228 - 141) / (189 - 141), "flat", 3, "below"],
        "-E": [(228 - 141) / (189 - 141), "natural", 3, "below"],
        "-E#": [(228 - 141) / (189 - 141), "sharp", 3, "below"],
        "-Fb": [(222 - 141) / (189 - 141), "flat", 3, "below"],
        "-F": [(222 - 141) / (189 - 141), "natural", 3, "below"],
        "-F#": [(222 - 141) / (189 - 141), "sharp", 3, "below"],
        "-Gb": [(216 - 141) / (189 - 141), "flat", 2, "below"],
        "-G": [(216 - 141) / (189 - 141), "natural", 2, "below"],
        "-G#": [(216 - 141) / (189 - 141), "sharp", 2, "below"],
        "-Ab": [(208 - 141) / (189 - 141), "flat", 2, "below"],
        "-A": [(208 - 141) / (189 - 141), "natural", 2, "below"],
        "-A#": [(208 - 141) / (189 - 141), "sharp", 2, "below"],
        "-Bb": [(202 - 141) / (189 - 141), "flat", 1, "below"],
        "-B": [(202 - 141) / (189 - 141), "natural", 1, "below"],
        "-B#": [(202 - 141) / (189 - 141), "sharp", 1, "below"],
        "Cb": [(196 - 141) / (189 - 141), "flat", 1, "below"],
        "C": [(196 - 141) / (189 - 141), "natural", 1, "below"],
        "C#": [(196 - 141) / (189 - 141), "sharp", 1, "below"],
        "Db": [(191 - 141) / (189 - 141), "flat", 0],
        "D": [(191 - 141) / (189 - 141), "natural", 0],
        "D#": [(191 - 141) / (189 - 141), "sharp", 0],
        "Eb": [(184 - 141) / (189 - 141), "flat", 0],
        "E": [(184 - 141) / (189 - 141), "natural", 0],
        "E#": [(184 - 141) / (189 - 141), "sharp", 0],
        "Fb": [(178 - 141) / (189 - 141), "flat", 0],
        "F": [(178 - 141) / (189 - 141), "natural", 0],
        "F#": [(178 - 141) / (189 - 141), "sharp", 0],
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
        "+Ab": [(124 - 141) / (189 - 141), "flat", 1, "above"],
        "+A": [(124 - 141) / (189 - 141), "natural", 1, "above"],
        "+A#": [(124 - 141) / (189 - 141), "sharp", 1, "above"],
        "+Bb": [(118 - 141) / (189 - 141), "flat", 1, "above"],
        "+B": [(118 - 141) / (189 - 141), "natural", 1, "above"],
        "+B#": [(118 - 141) / (189 - 141), "sharp", 1, "above"],
        "++Cb": [(112 - 141) / (189 - 141), "flat", 2, "above"],
        "++C": [(112 - 141) / (189 - 141), "natural", 2, "above"],
        "++C#": [(112 - 141) / (189 - 141), "sharp", 2, "above"],
        "++Db": [(106 - 141) / (189 - 141), "flat", 2, "above"],
        "++D": [(106 - 141) / (189 - 141), "natural", 2, "above"],
        "++D#": [(106 - 141) / (189 - 141), "sharp", 2, "above"],
        "++Eb": [(100 - 141) / (189 - 141), "flat", 3, "above"],
        "++E": [(100 - 141) / (189 - 141), "natural", 3, "above"],
        "++E#": [(100 - 141) / (189 - 141), "sharp", 3, "above"],
        "++Fb": [(94 - 141) / (189 - 141), "flat", 3, "above"],
        "++F": [(94 - 141) / (189 - 141), "natural", 3, "above"],
        "++F#": [(94 - 141) / (189 - 141), "sharp", 3, "above"],
        "++Gb": [(88 - 141) / (189 - 141), "flat", 4, "above"],
        "++G": [(88 - 141) / (189 - 141), "natural", 4, "above"],
        "++G#": [(88 - 141) / (189 - 141), "sharp", 4, "above"],
    }
    return dictionary


def returnHeightOfNote(
    systemY_start, systemY_end, note_height, correctionOffsetForNotehead=0
):
    outputValue = (note_height - systemY_start) / (
        systemY_end - systemY_start
    ) + correctionOffsetForNotehead
    return outputValue


def generateNotationHelperDictionaryFromGlobalMargins(
    canvas,
    GLOBAL_MARGINS,
    GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS,
    GLOBAL_LINE_THICKNESS,
    GLOBAL_STAFF_MARGINS,
    correctionOffsetForNotehead=-0.1,
):
    width, height = canvas.size

    systemX = GLOBAL_MARGINS[0] * width
    systemY = GLOBAL_MARGINS[1] * height

    systemY_end = systemY + (4 * GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS)

    # print("start_y: " + str(systemY) + " end_y: " + str(systemY_end))

    # we know that E is at systemY_end
    # so if we count downwards from E, we can find the height of the lowest note

    knownE = systemY_end
    lowestNoteHeight = knownE + (9 * (GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS / 2))
    dictionary = {}
    # for note "-C" for midi number 48
    arrayOfPitchNames = ["C", "D", "E", "F", "G", "A", "B"]
    arrayOfAccidentals = ["b", "", "#"]
    arrayOfAccidentalsWords = ["flat", "natural", "sharp"]
    arrayOfOctaves = ["--", "-", "", "+", "++"]
    arrayOfLedgerLines = ["below", "", "above"]
    arrayOfLedgerLinesPosition = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    currentPitchNameIdx = 0
    currentAccidentalIdx = 0
    currentAccidentalsWordsIdx = 0
    currentOctaveIdx = 1
    currentLedgerLineIdx = 0
    currentLedgerLinePositionIdx = 4
    counterLedgerLinesProxyCheck = 0  # to see how many ledger lines required as some notes are not ON the ledger lines
    createDictionaryFlag = True
    currentMidiNumber = 47
    midiNumberLedgerLineArrayCheck = [
        62,
        79,
    ]  # B below treble clef, A above treble clef

    currentNoteHeight = lowestNoteHeight
    counterNoteHeight = 0
    while createDictionaryFlag == True:
        currentMVCnote = str(
            arrayOfOctaves[currentOctaveIdx]
            + arrayOfPitchNames[currentPitchNameIdx]
            + arrayOfAccidentals[currentAccidentalIdx]
        )

        if "Fb" in currentMVCnote:
            currentMidiNumber = currentMidiNumber - 1

        if "Cb" in currentMVCnote:
            if currentMVCnote != "-Cb":
                currentMidiNumber = currentMidiNumber - 1

        dictionary[currentMVCnote] = [
            returnHeightOfNote(
                systemY, systemY_end, currentNoteHeight, correctionOffsetForNotehead
            ),
            arrayOfAccidentalsWords[currentAccidentalsWordsIdx],
            arrayOfLedgerLinesPosition[currentLedgerLinePositionIdx],
            arrayOfLedgerLines[currentLedgerLineIdx],
            currentMidiNumber,
        ]
        if arrayOfAccidentalsWords[currentAccidentalsWordsIdx] == "flat":
            oldMidiNumber = currentMidiNumber
            currentMidiNumber += 1
        elif arrayOfAccidentalsWords[currentAccidentalsWordsIdx] == "sharp":
            currentMidiNumber = currentMidiNumber
        elif arrayOfAccidentalsWords[currentAccidentalsWordsIdx] == "natural":
            oldMidiNumber = currentMidiNumber
            currentMidiNumber += 1

        currentAccidentalIdx += 1
        currentAccidentalsWordsIdx += 1
        counterLedgerLinesProxyCheck += 1
        counterNoteHeight += 1

        if counterNoteHeight == 3:
            counterNoteHeight = 0
            currentNoteHeight = currentNoteHeight - (
                GLOBAL_STAFF_INBETWEEN_SPACING_IN_PIXELS / 2
            )

        if currentMidiNumber <= midiNumberLedgerLineArrayCheck[0]:
            currentLedgerLineIdx = 0
        elif (
            currentMidiNumber >= midiNumberLedgerLineArrayCheck[1]
            and currentMVCnote == "+G#"
        ):
            currentLedgerLineIdx = 2
        elif currentMidiNumber > midiNumberLedgerLineArrayCheck[1] + 1:
            currentLedgerLineIdx = 2

        else:
            currentLedgerLineIdx = 1

        if currentMVCnote == "+G#":
            counterLedgerLinesProxyCheck = 0
            currentLedgerLinePositionIdx = 1

        if counterLedgerLinesProxyCheck == 6:
            counterLedgerLinesProxyCheck = 0
            if currentMidiNumber < midiNumberLedgerLineArrayCheck[0]:
                direction = -1
            elif currentMidiNumber > midiNumberLedgerLineArrayCheck[1]:
                direction = 1
            elif (
                currentMidiNumber > midiNumberLedgerLineArrayCheck[0]
                and currentMidiNumber < midiNumberLedgerLineArrayCheck[1]
            ):
                direction = 0
            currentLedgerLinePositionIdx = currentLedgerLinePositionIdx + direction
        if currentAccidentalIdx == 3:
            currentAccidentalIdx = 0
            currentAccidentalsWordsIdx = 0
            currentPitchNameIdx += 1

            if currentPitchNameIdx == 7:
                currentPitchNameIdx = 0
                currentOctaveIdx += 1
                if currentOctaveIdx == 5:
                    createDictionaryFlag = False

    # pprint(dictionary, sort_dicts=False)
    return dictionary


# 47, 48, 49, 49, 50, 51, 51, 52, 53, 53
