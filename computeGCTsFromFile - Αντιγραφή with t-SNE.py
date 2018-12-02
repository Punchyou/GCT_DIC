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
        for i in range(0, len(tonalities)):
            #print('i: ', i, ' -- tonalities[i].offset: ', tonalities[i].offset)
            surfCopy = deepcopy(surface)
            if i < (len(tonalities) - 1):
                tmpSurf = surfCopy.getElementsByOffset(tonalities[i].offset, tonalities[i+1].offset)
                chordsAll = []
                for ch in tmpSurf:
                    chord = [c.pitch.midi for c in ch]
                    chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
                    chordsAll.append(chordForm[0])
            else:
                tmpSurf = surfCopy.getElementsByOffset(tonalities[i].offset, surfLastOffset)
                chordsAll = []
                for ch in tmpSurf:
                    chord = [c.pitch.midi for c in ch]
                    chordForm = HARM_consonanceChordRecognizer(chord,consWeights)
                    chordsAll.append(chordForm[0])
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
    #print("All GCTs:", GCTsAllChordFormsforEachPiece)
    return fromIDX, toIDX, GCTsAllChordForms, GCTsAllChordFormsforEachPiece

def makeGCTsChordFormsADictionary(GCTsAllChordForms):
    allGCTsDict = {}
    for i in GCTsAllChordForms:
        for j in i:
            allGCTsDict[str(j)] = 0
    return allGCTsDict


def calculateCountsOfGCTs(allGCTsDICT, GCTsAllChordFochordsrmsforEachPiece):
    # Make a list: 1 if a GCTs exists, 0 if it doesn't.
    GCTsCounts = []
    for piecesFolder in GCTsAllChordFormsforEachPiece:
        for pieces in piecesFolder:
            allGCTsCopy = allGCTsDICT.copy()
            for GCT in pieces:
                allGCTsCopy[str(GCT)] = 1
            GCTsCounts.append(list(allGCTsCopy.values()))
    #print("All GCTs counts:", GCTsCounts)
    return GCTsCounts


def calculatePCA(GCTsCounts):
    pca = PCA(np.array(GCTsCounts), standardize=False)
    #print("PCAs: ", pca)
    return pca

def calculateT_SNE(GCTsCounts):
    tsne = TSNE(n_components = 2).fit_transform(GCTsCounts)
    return tsne

def visualizePCA(pca, fromIDX, toIDX):
    colors = ["red", "blue", "green", "black", "pink", "yellow"]
    allPlots = []
    fig = plt.gcf()
    for i in range(len(fromIDX)):
        xx, = plt.plot(pca.Y[int(fromIDX[i]):int(toIDX[i]), 0], pca.Y[int(fromIDX[i]):int(toIDX[i]), 1], 'ro', color = colors[i], markersize = 3)
        allPlots.append(xx)
    plt.legend(allPlots, currFolder)
    return plt.show(), fig

def visualizeT_SNE(tsne, fromIDX, toIDX):
    for i in range(len(fromIDX)):
        colors = ["red", "blue", "green", "black", "pink", "yellow"]
        plt.plot(tsne[int(fromIDX[i]):int(toIDX[i])], 'ro', color = colors[i], markersize = 1)
    plt.show()
    return tsne, plt


currFolder = np.array(["TestFileBachChorales", "TestFileEpirotika", "TestFileJazzForGCT", "TestFileModalChoral", "TestFileRebetika"])
fromIDX, toIDX, GCTsAllChordForms, GCTsAllChordFormsforEachPiece = prepareGCTarray(currFolder)
#print(GCTsAllChordForms)
allGCTsDICT = makeGCTsChordFormsADictionary(GCTsAllChordForms)
GCTsCounts = calculateCountsOfGCTs(allGCTsDICT, GCTsAllChordFormsforEachPiece)
#print(GCTsCounts)
pca = calculatePCA(GCTsCounts)
tsne = calculateT_SNE(GCTsCounts)
visualizePCA(pca, fromIDX, toIDX)
visualizeT_SNE(tsne, fromIDX, toIDX)