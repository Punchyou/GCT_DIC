#key - finding algorithms
import numpy as np
#namesAll = [] #note names of piece
scales = ['C', 'D-', 'D', 'E-', 'E', 'F', 'G-', 'G', 'A-', 'A', 'B-', 'B']
major = [6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88] #Krumhansl major profiles
minor = [6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17] #minor profile
normMaj = [x / max(major) for x in major] #normalize major profiles to 0-1 range
normMin = [k / max(minor) for k in minor]
def pcp_f(notes, pitches):
    #pitchAll = []

    '''for chord in chords: #extract pitches from chords
        pitches = chord.pitches
        for pitch in pitches:
            pitchAll.append(pitch.midi)'''
    '''for note in notes:
        pitches = note.pitches
        names = note.name
        namesAll.append(names)
        for pitch in pitches:
            pitchAll.append(pitch.midi)'''
    #print(namesAll)
    #calculate pitch classes with modulo 12
    pitchClass = [x % 12 for x in pitches]
    sort = sorted(pitchClass)

    repeats = []
    corrMaj = []
    corrMin = []

    #count repeats
    n = 0
    while n < 12:
        counted = sort.count(n) #count repeats for each pitch class
        repeats.append(counted)
        n = n + 1
    normRep = [x / max(repeats) for x in repeats] #normalize repeats to 0-1 range
    #print('repeats', repeats)

    #find correlations
    n = 0
    while n < 12:
        correlationMaj = np.corrcoef(normRep, normMaj) [1,0] #find correlations between repeats and major profiles
        correlationMin = np.corrcoef(normRep, normMin) [1,0]
        corrMaj.append(correlationMaj) #make a list with correlations
        corrMin.append(correlationMin)
        normRep.insert(11, normRep.pop(0))
        n = n + 1
    print('corrMaj: ', corrMaj)
    print("corrMin: ", corrMin)
    #major or minor?
    if max(corrMaj) > max(corrMin):
        maxCorrelation = max(corrMaj)
        kindOfKey = 'Major'
    else:
        maxCorrelation = max(corrMin)
        kindOfKey = 'Minor'
    #print(pitchAll)
    
    #key name
    if kindOfKey == 'Major':
        for maxPosition, maxCorr in enumerate(corrMaj):
            if maxCorr == max(corrMaj): #find max correlation with major
            #print(maxCorr)
                for notePosition, keyName in enumerate(scales):
                    if notePosition == maxPosition:
                        scaleName = scales[notePosition]
    else:
        for maxPosition, maxCorr in enumerate(corrMin):
            if maxCorr == max(corrMin): #find max correlation with major
            #print(maxCorr)
                for notePosition, keyName in enumerate(scales):
                    if notePosition == maxPosition:
                        scaleName = scales[notePosition]
    #print(namesAll)
    return scaleName, kindOfKey, maxCorrelation, repeats


def dtp_f(notes):
    dtOfEachNote = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #dt of each pitch class
    durationsAll = [] #dt of all notes

    for n in notes:
        dur = n.quarterLength #extract duration info in quarters
        durationsAll.append(dur) #make durations list
    for scalePos, scaleVal in enumerate(scales):
        #print("Scale letter:" + str(scale))
        for ntPos, ntVal in enumerate(notes):
            if ntVal == scaleVal:
                dtOfEachNote[scalePos] += durationsAll[ntPos] #sum all durations for each note with same name
    normDtOfEach = [y / max(dtOfEachNote) for y in dtOfEachNote] #normalize piece durations
    dtCorrelationsMaj = []
    dtCorrelationsMin = []
    #print(namesAll)
    n = 0
    while n < 12:
        corDurMaj = np.corrcoef(normDtOfEach, normMaj) [1,0] # correlations http://benalexkeen.com/correlation-in-python/
        corDurMin = np.corrcoef(normDtOfEach, normMin) [1,0]
        dtCorrelationsMaj.append(corDurMaj) #make a list with correlations
        dtCorrelationsMin.append(corDurMin)
        normDtOfEach.insert(11, normDtOfEach.pop(0))
        n = n + 1
    #print('Duration Correlations from C:', dtCorrelationsMaj, dtCorrelationsMin)

    if max(dtCorrelationsMaj) > max(dtCorrelationsMin):
        maxCorDur = max(dtCorrelationsMaj)
        kindOfKeyD = 'Major'
    else:
        maxCorDur = max(dtCorrelationsMin)
        kindOfKeyD = 'Minor'

    if kindOfKeyD == 'Major':
        for corPos, corVal in enumerate(dtCorrelationsMaj):
            if corVal == max(dtCorrelationsMaj): #find max value from correlations
                scaleNameDur = scales[corPos] #name the scale name with the positions of max correlation
                #print('max correlation scale from durations profile:', scales[corPos])
    else:
        for corPos, corVal in enumerate(dtCorrelationsMin):
            if corVal == max(dtCorrelationsMin): #find max value from correlations
                scaleNameDur = scales[corPos] #name the scale name with the positions of max correlation
                #print('max correlation scale from durations profile:', scales[corPos])
    return scaleNameDur, kindOfKeyD, maxCorDur