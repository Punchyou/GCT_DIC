import itertools
from itertools import combinations
import numpy as np
def HARM_findSubsets(m):
    s = m
    #find all the possible compinations
    subsets = sum(map(lambda r: list(combinations(s, r)), range(1, len(s)+1)), [])
    
    #reversed to bring max length subset first
    subsRev = list(reversed(subsets))
    subs = []
    
    #sort the subsRev
    for i in subsRev:
        subs.append(sorted(i))
    #print("Subsets: ", subs)
    print(subs)
    return subs