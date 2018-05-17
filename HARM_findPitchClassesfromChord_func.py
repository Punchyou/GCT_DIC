def HARM_findPitchClassesfromChord(chord):
    modChord = [i % 12 for i in chord] #modulo 12 to chord list to take the pitch classes
    return modChord
