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
    pieces = []
    GCTcountsAll = []
    for pieceName in allDocs:
        print("-----Parsing piece: " + pieceName + "... ")
        pieces.append(pieceName)
    
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
            chordsAll.append(chordForm)
            for i in chordForm:
                ch.addLyric(str(i))
        reduction = reduction.transpose(24)

        def countGCTs(chordsAll):
            GCTcounts = [0]*12
            for i in range(len(chordsAll)):
                GCTcounts[chordsAll[i][0][0]] = GCTcounts[chordsAll[i][0][0]] + 1
            maxC = max(GCTcounts)
            GCTcount = [i/maxC for i in GCTcounts]
            return GCTcount
        GCTcoun = countGCTs(chordsAll)
        GCTcountsAll.append(GCTcoun)
    return GCTcountsAll, chordsAll

currFolder = np.array(["TestFileBachChorales", "TestFileEpirotika", "TestFileJazz", "TestFileRebetika", "TestFileModalChoral"])
def prepareGCTarray(currFolder):
    indxs = []
    #these are the normalized GCTs counts:
    GCTsFromAllFiles = []
    GCTsAllChordForms = []
    for i, j in enumerate(currFolder):
        GCTcountsAll, GCTsChordForm = computeGCTsFromFile_f(j)
        GCTsFromAllFiles.extend(GCTcountsAll)
        GCTsAllChordForms.extend(GCTsChordForm)
        indxs.append(len(GCTcountsAll))
    print(GCTsAllChordForms)
    idxs = np.array(indxs)
    toIDX = np.cumsum(idxs)
    fromIDX = np.concatenate((np.zeros(1), toIDX[:len(toIDX)-1]))
    return  GCTsFromAllFiles, idxs, fromIDX, toIDX, GCTsChordForm

GCTsFromAllFiles, idxs, fromIDX, toIDX, GCTsChordForm = prepareGCTarray(currFolder)

def makeGCTsChordFormsADictionary(GCTsChordForm):
    allGCTsDict = {}
    for i in GCTsChordForm:
        allGCTsDict[str(i)] = 0
    print("GCTs DICTIONARY: ", allGCTsDict)
    return allGCTsDict

makeGCTsChordFormsADictionary(GCTsChordForm)


def calculatePCA(GCTsFromAllFiles):
    pca = PCA(np.array(GCTsFromAllFiles), standardize=False)
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

pca = calculatePCA(GCTsFromAllFiles)
pcaPlot = visualizePCA(pca, fromIDX, toIDX)
#fig.savefig('PCAwithColors.png', dpi = 300)