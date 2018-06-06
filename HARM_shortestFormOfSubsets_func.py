import numpy as np
#from collections import deque

def HARM_shortestFormOfSubsets(maxConSubs):
    maxConSubss = list(maxConSubs)
    lastFirstInterval = [] #[[0]*len(maxConSubss)*len(maxConSubss[0])]
    shiftedChords = []

    for i in range(0, len(maxConSubss)):

        shiftedCh = []
        lastFirstInterval1 = []
        n = 0
        while n < len(maxConSubss[i]):
            shiftedCh1 = []

            maxConSubss[i].insert((len(maxConSubss[i])-1), maxConSubss[i].pop(0)) #circlular shifting
            shiftedCh1.extend(maxConSubss[i])#put it in shoftedCh1 array
            lastFirstInt = maxConSubss[i][-1]-maxConSubss[i][0] #find interval between first and last pitch of the max sconsonand chord
            if lastFirstInt<0: #if < 0 add 12 to move it to the next octave
                lastFirstInt = lastFirstInt + 12
            #lastFirstInterval[i][n] = lastFirstInt #put it in lastFirstInterval array
            lastFirstInterval1.append(lastFirstInt)
            shiftedCh.append(shiftedCh1) #put it in shiftesCh array
            n = n+1
        shiftedChords.append(shiftedCh)#put in the shifted chords array for each
        lastFirstInterval.append(lastFirstInterval1)

    #print("Intervals between first and last pitrch (for each max consonant): ", lastFirstInterval)
    
    shortestAll = []
    for i in range(len(lastFirstInterval)):
        shortestChOfEach = []
        shortest = min(lastFirstInterval[i])
        for j in range(len(lastFirstInterval[i])):
            if lastFirstInterval[i][j] == shortest:
                shortestChOfEach.append(shiftedChords[i][j]) #put it in an array
        shortestAll.append(shortestChOfEach) #make array with all shortest chords

    #NEEDS TESTING
    #if the shortest forms are more than one, you have to choose somehow
    for i in range(0, len(shortestAll)):
        for j in range(0, len(shortestAll[i])):
            #for k in range(0, len(shortestAll[i][j])):
            if len(shortestAll[i]) >=2: #if there are more than one shortest forms for one chord
                for j in range(len(shortestAll[i])-1):
                    baseLengthj = shortestAll[i][j][1]- shortestAll[i][j][0] #find the base length (first and second interval) of a shortest form of a chord
                    baseLengthjNext = shortestAll[i][j+1][1] - shortestAll[i][j+1][0] #find the base length of the next shortest form of a chord
                    if baseLengthj < 0:
                        baseLengthj = baseLengthj + 12 #if < 0 move it to the next octave
                    if baseLengthjNext < 0:
                        baseLengthjNext = baseLengthjNext + 12
                    if (baseLengthj) < (baseLengthjNext): #find the shortest form with shortest baselength
                        shortestBaseLength = shortestAll[i][j] #and that's the form I want
                        print("Shortest with minimum baselength:", shortestBaseLength) #NA TO TSEKARW ME POLLA CHORDS
                        #KAI PREPEI NA FTIAKSW ARRAY GIA OLA TA BASELENGTHS
    return shortestAll