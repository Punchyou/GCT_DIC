import numpy as np
def HARM_findExtentions(m, maxConSubs):
    chEx = []
    for s in maxConSubs:
       chEx.append(list(m [[not (m[i] in s) for i in range(len(m))]]))
    #chEx = np.concatenate(chEx) #works for one. try it with many chords with more extentions!!
    #print('Chord Extentions: ', chEx)
    return chEx