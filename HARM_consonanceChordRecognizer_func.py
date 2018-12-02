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
from HARM_relativeToRootExtentions_func import HARM_relativeToRootExtentions
from HARM_findPitchClassesfromChord_func import HARM_findPitchClassesfromChord
from HARM_takeOnlyUniqueValuesfromPitchClasses_func import HARM_takeOnlyUniqueValuesfromPitchClasses


#function that returns the final form of chord
def HARM_consonanceChordRecognizer(chord, consWeights):

    #find the pitch classes from the original chord
    modChord = HARM_findPitchClassesfromChord(chord)

    #take only unique values from the pitch classes array
    m = HARM_takeOnlyUniqueValuesfromPitchClasses(modChord)

    #find subsets/possible combinations between pitches
    subs = HARM_findSubsets(m)
    
    #find consonant intervals between pitches
    consonant = HARM_findConsonantSequencesOfSubsets(consWeights, subs)
    
    #find Maximal Consonant Subsets
    maxConSubs = HARM_findMaximalConsonantSubsets(consonant)
    
    #find chord extentions
    chExtentions = HARM_findExtentions(m, maxConSubs)

    #find shortest form func
    shortest = HARM_shortestFormOfSubsets(maxConSubs)
    
    #chord label
    chordForm, root, chType = HARM_rootExtentionForm(shortest, chExtentions)
    print(chordForm)
    return chordForm

class GCT:
    #id as a static variable maybe?
    def __init__(self, root, chType, chExtentions, chordForm):
        self.root = root
        self.type = chType
        self.extentions = chExtentions
        self.label = chordForm

        #print(self.root)
        #self.allVersions = 

#make a class for printing