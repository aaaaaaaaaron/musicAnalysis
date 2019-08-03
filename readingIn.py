# https://pypi.org/project/SoundFile/
# https://www.youtube.com/watch?v=6n9ybiwnbT8
# https://pysoundfile.readthedocs.io/en/0.9.0/


# or maybe I want to use pyAudio: probably: https://people.csail.mit.edu/hubert/pyaudio/docs/


notesDict = {1: "A",
         2: "A#/ Bb",
         3: "B",
         4: "C",
         5: "C#/ Db",
         6: "D",
         7: "D#/ Eb",
         8: "E",
         9: "F",
         10: "F#/ Gb",
         11: "G",
         12: "G#/ Ab"}

notesList = ["A", "A#/ Bb", "B", "C", "C#/ Db", "D", "D#/ Eb", "E", "F", "F#/ Gb", "G", "G#/ Ab"]

def createScale(base, type):
    """finds notes in major and minor scale. 0 is major, 1 is minor"""
    majorScale = []
    current = notesList.index(base)

    if type == 0:
        intervals = [2, 2, 1, 2, 2, 2, 1]
    elif type == 1:
        intervals = [2,1,2,2,1,2,2]

    for i in intervals:
        majorScale.append(notesList[current])
        current += i
        if current > 11:
            current = current - 12

    return majorScale

def askInput():
    includedNotes = []
    while True:
        new = input("enter a note")
        if new == "break":
            break
        includedNotes.append(new)

    return includedNotes

def whichScale(notes):
    """Creates a list of all the scales, then filters them out based on what you have"""
    viableScales = []
    for baseNote in notesList:
        viableScales.append(createScale(baseNote, 0))

    for scale in viableScales:
        for note in notes:
            if note not in scale:


    return viableScales

if __name__ == "__main__":
    print(createScale("A", 0))
    # print(askInput())
    print(whichScale(["A", 'G#/ Ab', "E"]))
