
import numpy as np
#keep only consonant subsets with max length
def HARM_findMaximalConsonantSubsets(consonant):
    maxConSubs = []
    for i in consonant:
        if len(i) == len(max(consonant,key=len)):
            maxConSubs.append(i)
    return maxConSubs