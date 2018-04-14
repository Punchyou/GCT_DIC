from music21 import*

dmaj = chord.Chord(['D', 'F#', 'A'])
dmaj.show()
cNote = note.Note("C")
cNote.show()
print(dmaj.pitches)
print(dmaj.pitchClasses)
names = dmaj.pitchClasses


s = stream.Stream()
s.append(key.Key('D'))
s.append(note.Note('F'))
s.append(key.Key('b-', 'minor'))
s.append(note.Note('F'))
s.show()