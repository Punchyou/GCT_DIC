import numpy as np

#find consonant intervals between pitches
def HARM_findConsonantSequencesOfSubsets(consWeights, subs):
    cons = [] #empty list
    for s in subs:
        #make a 2d list of zeros
        d = [[0]*len(s)]*(len(s))
        #make a second 2d list of zeros for appending ones
        #This is going to be the 2d array with the distances of notes of the chord
        #I use np to take the any func
        dBin = np.array([[0]*len(s)]*(len(s)))
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                #find the distance between two pitches of the subset
                d[i][j]= abs(s[j]- s[i])
                #if the distance is negative, add 12
                while d[i][j] < 0: 
                    d[i][j] = d[i][j] + 12
                #if the consWeight is consonant
                if consWeights[d[i][j]]==1: 
                    #put an 1 into the dBin list
                    dBin[i][j] = 1
        # all values of the list equals one, the pitch sequence is consonant
        if np.all(dBin)==1:
            cons.append(s)
    return cons