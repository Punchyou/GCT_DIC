
import numpy as np
def HARM_rootExtentionForm(shortest, chExtentions):
    firstsPitches = []
    for i in range(len(shortest)):
        for j in range(len(shortest[0])):
            firstsPitches.append(shortest[i][j][0])
            pClList = []
            for k in range(len(shortest[0][0])):
                pCl = shortest[i][j][k] - shortest[i][j][0]
                if pCl <0:
                    pCl = pCl + 12
                pClList.append(pCl)
            shortest[i][j] = pClList
    #move extention relatively to 0
    for i in range(len(chExtentions)):
        for j in range(len(chExtentions[i])):
            chExtentions[i][j] = chExtentions[i][j] - firstsPitches[i]
            if chExtentions[i][j] <0:
                chExtentions[i][j] = chExtentions[i][j]+12
    for i in range(len(shortest)):
        shortest[i].insert(0,firstsPitches[i])
        shortest[i].append(chExtentions[i])
        #for j in range(len(shortest[0][0])):
            #shortest[i].extend()
    #notation = np.array(shortest, dtype=object)

    notation = shortest
    for i in range(len(notation)):
        maxNot = max(notation[i][1])
        for j in range(len(notation[i][2])):
            if notation[i][2][j]<maxNot:
                notation[i][2][j] = notation[i][2][j] + 12
    
    #with np arrays
    '''for i in range(len(notation)):
        notation[i][0] = np.array(notation[1][0])
        notation[i][2] = np.array(notation[i][2])
        notation[i][1] = np.array(notation[i][1])
        j = notation[i][2]< np.max(notation[i][1])
        notation[i][2][j] = notation[i][2][j]+12'''
    
    print("Chord: ", notation)
    return(notation)