# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:58:13 2018

@author: Maria
"""

#from HARM_traverseOrbit_func import HARM_traverseOrbit
from HARM_findSubsets_func import HARM_findSubsets
from HARM_findConsonantSequencesOfSubsets_func import HARM_findConsonantSequencesOfSubsets
from HARM_findMaximalConsonantSubsets_func import HARM_findMaximalConsonantSubsets
from HARM_findExtentions_func import HARM_findExtentions
from HARM_shortestFormOfSubsets_func import HARM_shortestFormOfSubsets
from HARM_rootExtentionForm_func import HARM_rootExtentionForm
#from HARM_shortestFormOfSubsets_func import normalOrderInversion
import numpy as np

#HARM_consonanceChordRecognizer(c,consWeights) function

def HARM_consonanceChordRecognizer(chord, consWeights):
    modChord = [i % 12 for i in chord] #modulo 12 to chord list to take the pitch classes
    m = np.unique(modChord) #take only unique values
    #print("Pitches: ", m)
    
    #allPaths = np.size((dBin),0) #number of paths (in the tree)

    #find subsets/possible combinations between pitches
    subs = HARM_findSubsets(m)
    
    #find consonant intervals between pitches
    consonant = HARM_findConsonantSequencesOfSubsets(consWeights, subs)

    #find Maximal Consonant Subsets
    maxConSubs = HARM_findMaximalConsonantSubsets(consonant)

    #find extentions
    chExtentions = HARM_findExtentions(m, maxConSubs)

    #find shortest form func
    shortest = HARM_shortestFormOfSubsets(maxConSubs)

    #normal order invertion function
    #noi = normalOrderInversion(maxConSubs)

    #MAKE HERE A FUNCTIONS FOR CHOOSING THE SHORTEST FORM DEPENDING THE BASELENGTH (code ready in HARM_shortestFormOfSubsets(maxConSubs))

    chordForm = HARM_rootExtentionForm(shortest, chExtentions)

    #PREPEI NA KANW KAI THN SUNARTHSH POU THA VAZW TA EXTENTIONS STO TELOS KAI THA BAZW KAI TO ROOT THS SUGXODIAS STHN ARXH

    return chordForm

#    find max paths of trees
#    for i in range(0, np.size(dBin, 0)):
#        pOUT = HARM_traverseOrbit_func.HARM_traverseOrbit(dBin,i,[],1)
#    return m, dBin, allPaths, pOUT