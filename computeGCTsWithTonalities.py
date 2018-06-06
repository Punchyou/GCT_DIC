from music21 import *
import os
import glob
import numpy as np
import operator
from copy import deepcopy
from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer

def computeGCTsWithTonality():
    currFolder = 'TestFileBachChorales'

    # get all the files in folder with .xml extension
    allDocs = glob.glob(currFolder + os.sep + "*.xml")

    # parse all pieces
    pieceIDX = 0

    for pieceName in allDocs:
        print("-----Parsing piece: " + pieceName + "... ")

        #pieceNames.append(pieceName)
        # parse piece
        p = converter.parse(pieceName)

        # make names
        splitName = pieceName.split(".")
        noExtName = splitName[0]
        finalName = noExtName + ".txt"

        # reduction
        r1 = p.parts[-1]
        r2 = p.parts[-2]
        rc = stream.Score()
        rc.insert(0, r1)
        rc.insert(0, r2)
        rcChordified = rc.chordify()
        rcFlat = rcChordified.flat
        reduction = rcFlat.getElementsByClass('Chord')
        # last reduction offset
        redLastOffset = reduction[-1].offset

        # tonality
        tonPart = p.parts[2]
        tonChordified = tonPart.chordify()
        tonFlat = tonChordified.flat
        tonalities = tonFlat.getElementsByClass('Chord')
        
        # surface
        s1 = p.parts[0]
        s2 = p.parts[1]
        sc = stream.Score()
        sc.insert(0, s1)
        sc.insert(0, s2)
        scChordified = sc.chordify()
        scFlat = scChordified.flat
        surface = scFlat.getElementsByClass('Chord')
        # last surface offset
        surfLastOffset = surface[-1].offset

        consWeights = [1,0,0,1,1,1,0,1,1,1,0,0]
        for i in range(0, len(tonalities)):
            print('i: ', i, ' -- tonalities[i].offset: ', tonalities[i].offset)
            surfCopy = deepcopy(surface)
            if i < (len(tonalities) - 1):
                tmpSurf = surfCopy.getElementsByOffset(tonalities[i].offset, tonalities[i+1].offset)
                notes = []
                pitches = []
                chordsAll = []
                for ch in tmpSurf:
                    chordNotes = ch.pitchNames
                    chord = [c.pitch.midi for c in ch]
                    chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
                    print(chordForm)
                    chordsAll.append(chordForm)
                    for i in chordForm:
                        ch.addLyric(str(i))

            else:
                tmpSurf = surfCopy.getElementsByOffset(tonalities[i].offset, surfLastOffset)
                #print('START surface with tonality: ', [t.midi for t in tonalities[i].pitches])
                notes = []
                pitches = []
                chordsAll = []
                for ch in tmpSurf:
                    chordNotes = ch.pitchNames
                    chord = [c.pitch.midi for c in ch]
                    chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
                    print(chordForm)
                    chordsAll.append(chordForm)
                    for i in chordForm:
                        ch.addLyric(str(i))
        tmpSurf = tmpSurf.transpose(24)
    return tmpSurf
gct = computeGCTsWithTonality()
#gct.show()