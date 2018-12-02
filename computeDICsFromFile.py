#xml as input, returns an xml with gct harmonic analysis and comments (for any double gcts for the same chord)
from music21 import *
import os
import glob
import numpy as np
import computeDIC
#from computeGCTsFromFile import calculatePCA
from matplotlib.mlab import PCA
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans


def computeDICsFromFile_f(piecesFolder):
    #weights of consonant (1) and dissonant (0) intervals
    consWeights = [1,0,0,1,1,1,0,1,1,1,0,0]
    
    # get all the files in folder with .xml extension
    allDocs = glob.glob(piecesFolder + os.sep + "*.xml")

    # parse all pieces

    DICsPiecesOfAFolder = []
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
        reduction = rcFlat.getElementsByClass('Chord')
        chordsAll = []
        #print("PIECE")
        for ch in reduction:
            chord = [c.pitch.midi for c in ch]
            chordsAll.append(chord)
        DICsInAPiece = (computeDIC.computeDICsfromChordList(chordsAll))
        DICsPiecesOfAFolder.append(DICsInAPiece.tolist())
    return DICsPiecesOfAFolder, pieceCounts

def allDICsforEachPiece(currFolder):
    # Make a list of lists od DICs in each piece
    DICsInAllFolders = []
    indxs = []
    for piecesFolder in currFolder:
        DICsPiecesOfAFolder, pieceCounts = computeDICsFromFile_f(piecesFolder)
        DICsInAllFolders.append(DICsPiecesOfAFolder)
        indxs.append(pieceCounts)
    return DICsInAllFolders, indxs

def makeADictionaryOfAllDICs(DICsInAllFolders):
    # Make a dictionary of all DICs of all pieces in all folders
    dictOfDICs = {}
    for piecesFolder in DICsInAllFolders:
        for pieces in piecesFolder:
            for DIC in pieces:
                dictOfDICs[str(DIC)] = 0
    return dictOfDICs

def calculateCountsOfDICs(DICsInAllFolders, dictOfDICs):
    # Make a list of 1 and 0 if the DICs exist or not in a piece
    DICsCounts = []
    for piecesFolder in DICsInAllFolders:
        for pieces in piecesFolder:
            dictOfDICsCopy = dictOfDICs.copy()
            for GCT in pieces:
                dictOfDICsCopy[str(GCT)] = 1
            DICsCounts.append(list(dictOfDICsCopy.values()))
    print("DIC binary value: ", DICsCounts)
    print(len(DICsCounts))
    return DICsCounts

def make_From_To_Indeces(indxs):
    # Set each number of pieces as indeces range of the dictionary
    # in which we will apply PCA
    idxs = np.array(indxs)
    toIDX = np.cumsum(idxs)
    fromIDX = np.concatenate((np.zeros(1), toIDX[:len(toIDX)-1]))
    return fromIDX, toIDX

def calculatePCA(GCTsCounts):
    pca = PCA(np.array(GCTsCounts), standardize=False)
    return pca

def visualizePCA(pca, fromIDX, toIDX):
    colors = ["red", "blue", "green", "black", "pink", "yellow"]
    allPlots = []
    fig = plt.gcf()
    for i in range(len(fromIDX)):
        xx, = plt.plot(pca.Y[int(fromIDX[i]):int(toIDX[i]), 0], pca.Y[int(fromIDX[i]):int(toIDX[i]), 1], 'ro', color = colors[i], markersize = 2)
        allPlots.append(xx)
    plt.legend(allPlots, currFolder)
    return plt.show(), fig

def calculateK_meansOfPCA(pca):
    # Calsulate the k_means array
    k_means = KMeans(n_clusters=4)
    pcaY = pca.Y[:, 0:2]
    k_means = k_means.fit(pcaY)
    return k_means.predict(pcaY)


def visualizePCA_K_Means(pca, k_means, fromIDX, toIDX):
    # visualize pca and k_means
    k_means = k_means.tolist()
    colors = ["red", "blue", "green", "black", "pink", "yellow"]
    markers = ['+', ',', '.', '1']
    allPlots = []
    fig = plt.gcf()
    for i in range(len(fromIDX)):
        xx, = plt.plot(pca.Y[int(fromIDX[i]):int(toIDX[i]), 0], pca.Y[int(fromIDX[i]):int(toIDX[i]), 1], color = colors[i], marker = markers[k_means[int(fromIDX[i]):int(toIDX[i])]], linestyle = 'None', markersize=20)
        allPlots.append(xx)
    plt.legend(allPlots, currFolder)
    return plt.show(), fig

currFolder = np.array(["TestFileBachChorales", "TestFileEpirotika"])#, "TestFileJazz", "TestFileModalChoral", "TestFileRebetika"])
DICsInAllFolders, indxs = allDICsforEachPiece(currFolder)
print("All DICs Bach piece: ", DICsInAllFolders[0][0])
print("All DICs Epirus song: ", DICsInAllFolders[1][0])
dictOfDICs = makeADictionaryOfAllDICs(DICsInAllFolders)
DICsCounts = calculateCountsOfDICs(DICsInAllFolders, dictOfDICs)
fromIDX, toIDX = make_From_To_Indeces(indxs)
pca = calculatePCA(DICsCounts)
print("PCA: ", pca)
print("Maria")
#visualizePCA(pca, fromIDX, toIDX)
#k_means = calculateK_meansOfPCA(pca)
#visualizePCA_K_Means(pca, k_means, fromIDX, toIDX)