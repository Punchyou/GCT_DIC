from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer
consWeights = [1,0,0,1,1,1,0,1,1,1,0,0] #consonant weights
chords = [[60, 64, 67, 72], [66, 60, 57, 65], [64, 61, 67, 67], [62, 62, 57, 65], [57, 61, 57, 64], [64, 59, 68, 64]]

for chord in chords:
    m = HARM_consonanceChordRecognizer(chord, consWeights)