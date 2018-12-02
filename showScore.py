#xml as input, returns an xml with gct harmonic analysis and comments (for any double gcts for the same chord)
from music21 import *
import os
import glob
import numpy as np
from matplotlib import pyplot as plt
from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer
from matplotlib.mlab import PCA
from sklearn.manifold import TSNE
from copy import deepcopy


def showScore_f(j):
    
    # get all the files in folder with .xml extension
    allDocs = glob.glob(j + os.sep + "*.xml")

    # parse all pieces
    pieceCounts = 0
    for pieceName in allDocs:
        #print("-----Parsing piece: " + pieceName + "... ")
        pieceCounts += 1
    
        # parse piece
        p = converter.parse(pieceName)

        # reduction
        r1 = p.parts[-1]
        r2 = p.parts[-2]
        rc = stream.Score()
        rc.insert(0, r1)
        rc.insert(0, r2)
        rcChordified = rc.chordify()
        rcFlat = rcChordified.flat
        
        # tonality
        tonPart = p.parts[2]
        tonChordified = tonPart.chordify()
        tonFlat = tonChordified.flat
        
        
        # surface
        s1 = p.parts[0]
        s2 = p.parts[1]
        sc = stream.Score()
        sc.insert(0, s1)
        sc.insert(0, s2)
        scChordified = sc.chordify()
        #scChordified.show()
        scFlat = scChordified.flat
        surface = scFlat.getElementsByClass('Chord')
        print([i.pitch.midi for i in surface[3]])
        #for i in surface:
            #for j in i:
            #a = [j.pitch.midi for j in i]
            #b = a[::-1]
            #print(b)
        #print([i.pitch.midi for i in surface[i]])
        #scFlat.show()
        # last surface offset
showScore_f("TestFile")