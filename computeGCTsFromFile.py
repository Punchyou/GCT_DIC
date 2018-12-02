#xml as input, returns an xml with gct harmonic analysis and comments (for any double gcts for the same chord)
from music21 import *
import os
import glob
import numpy as np
import operator
from matplotlib import pyplot as plt
from HARM_consonanceChordRecognizer_func import HARM_consonanceChordRecognizer
import itertools
from matplotlib.mlab import PCA
import matplotlib.cm as cm


def computeGCTsFromFile_f(j):
    #weights of consonant (1) and dissonant (0) intervals
    consWeights = [1,0,0,1,1,1,0,1,1,1,0,0]
    
    # get all the files in folder with .xml extension
    allDocs = glob.glob(j + os.sep + "*.xml")

    # parse all pieces
    pieceCounts = 0
    chordsAllforAllPiecesInAFolder = []
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
        reduction = rcFlat.getElementsByClass('Chord')
        chordsAll = []
        for ch in reduction:
            chord = [c.pitch.midi for c in ch]
            chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
            chordsAll.append(chordForm[0])
            for i in chordForm:
                ch.addLyric(str(i))
        chordsAllforAllPiecesInAFolder.append(chordsAll)
        
        reduction = reduction.transpose(24)
    return chordsAllforAllPiecesInAFolder, pieceCounts

def prepareGCTarray(currFolder):
    indxs = []
    GCTsAllChordForms = []
    GCTsAllChordFormsforEachPiece = []
    for i in currFolder:
        GCTsChordForm, pieceCounts= computeGCTsFromFile_f(i)
        GCTsAllChordForms.extend(GCTsChordForm)
        GCTsAllChordFormsforEachPiece.append(GCTsChordForm)
        indxs.append(pieceCounts)
    idxs = np.array(indxs)
    toIDX = np.cumsum(idxs)
    fromIDX = np.concatenate((np.zeros(1), toIDX[:len(toIDX)-1]))
    return fromIDX, toIDX, GCTsAllChordForms, GCTsAllChordFormsforEachPiece

def makeGCTsChordFormsADictionary(GCTsAllChordForms):
    allGCTsDict = {}
    for i in GCTsAllChordForms:
        for j in i:
            allGCTsDict[str(j)] = 0
    return allGCTsDict


def calculateCountsOfGCTs(allGCTsDICT, GCTsAllChordFochordsrmsforEachPiece):
    # Make a list of tha GCTs, 1 if a GCTs exists, 0 if it doesn't.
    GCTsCounts = []
    for piecesFolder in GCTsAllChordFormsforEachPiece:
        for pieces in piecesFolder:
            allGCTsCopy = allGCTsDICT.copy()
            for GCT in pieces:
                allGCTsCopy[str(GCT)] = 1
            GCTsCounts.append(list(allGCTsCopy.values()))
    return GCTsCounts


def calculatePCA(GCTsCounts):
    pca = PCA(np.array(GCTsCounts), standardize=False)
    return pca

def visualizePCA(pca, fromIDX, toIDX):
    colors = ["red", "blue", "green", "black", "pink", "yellow"]
    allPlots = []
    fig = plt.gcf()
    for i in range(len(fromIDX)):
        xx, = plt.plot(pca.Y[int(fromIDX[i]):int(toIDX[i]), 0], pca.Y[int(fromIDX[i]):int(toIDX[i]), 1], 'ro', color = colors[i])
        allPlots.append(xx)
    plt.legend(allPlots, currFolder)
    return plt.show(), fig


currFolder = np.array(["TestFileBachChorales"])# "TestFileEpirotika"]) #"TestFileJazz","TestFileModalChoral", "TestFileRebetika" ])
fromIDX, toIDX, GCTsAllChordForms, GCTsAllChordFormsforEachPiece = prepareGCTarray(currFolder)
allGCTsDICT = makeGCTsChordFormsADictionary(GCTsAllChordForms)
GCTsCounts = calculateCountsOfGCTs(allGCTsDICT, GCTsAllChordFormsforEachPiece)
pca = calculatePCA(GCTsCounts)
visualizePCA(pca, fromIDX, toIDX)