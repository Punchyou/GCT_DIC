from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer
consWeights = [1,0,0,1,1,1,0,1,1,1,0,0] #consonant weights
#chords = [[7, [0, 4, 7], []], [7, [0, 4, 7], []], [0, [0, 4, 7], []], [4, [0, 3, 7], []], [2, [0, 4, 7], []], [7, [0, 4, 7], []], [11, [0, 3, 7], []]]
#chords = [[60, 64, 67, 72], [65, 60, 69], [60, 64, 67, 71], [52, 61, 67, 79], [62, 62, 57, 65], [57, 61, 57, 64], [65, 74, 57, 74], [64, 59, 68, 64], [60, 72, 82], [60, 65, 67], [60, 63, 70], [60, 67], [60, 65], [60, 63, 70], [60,72], [60, 70, 60]]
chords =[[2, 7, 11]]
for chord in chords:
    m = HARM_consonanceChordRecognizer(chord, consWeights)