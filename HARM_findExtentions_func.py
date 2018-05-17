import numpy as np
def HARM_findExtentions(m, maxConSubs):
    m = np.array(m)
    chEx = []
    for s in maxConSubs:
       chEx.append(list(m [[not (m[i] in s) for i in range(len(m))]]))
    return chEx