import numpy as np



#find consonant intervals between pitches
def HARM_findConsonantSequencesOfSubsets(consWeights, subs):
    cons = [] #empty list
    for s in subs:
        d = [[0]*len(s)]*(len(s)) #make a 2d list of zeros
        dBin = np.array([[0]*len(s)]*(len(s))) #make a second 2d list of zeros for appending ones. This is going to be the 2d array with the distances of notes of the chord
        for i in range(0, len(s)):
            for j in range(0, len(s)):
                d[i][j]= abs(s[j]- s[i]) #find the distance between two pitches of the subset
                while d[i][j] < 0: #if the distance is negative, add 12
                    d[i][j] = d[i][j] + 12 
                if consWeights[d[i][j]]==1: #if the consWeight is consonant
                    dBin[i][j] = 1 #put an 1 into the dBin list
        if np.all(dBin)==1: # all values of the list equals one, the pitch sequence is consonant
            cons.append(s)
    #print("Consonant: ", cons)
    return cons