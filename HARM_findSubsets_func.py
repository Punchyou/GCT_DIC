import itertools
from itertools import combinations
import numpy as np
def HARM_findSubsets(m):
    s = set(m)
    subsets = sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), []) #find all the possible compinations
    subsRev = list(reversed(subsets)) #reversed to bring max length subset first
    subs = []
    
    #sort the subsRev
    for i in subsRev:
        subs.append(sorted(i))
    #print("Subsets: ", subs)
    return subs