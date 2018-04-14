# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 10:46:24 2018

@author: Maria
"""
#functions that makes a trees of paths
import numpy as np
#from HARM_evaluateToTop_func import HARM_evaluateToTop
from HARM_traverseOrbit_func import HARM_traverseOrbit

class Tree():
    def HARM_traverseOrbit(pOUT, m, grammi,pIN,myDepth):
        pOUT.content = grammi
        pOUT.depth = myDepth
        pOUT.parent = pIN
        pOUT.children = []
        for j in range((grammi+1),np.size(m,2)):
            if m(grammi,j) > 0:
                if not pOUT.parent: #''' | HARM_evaluateToTop(pOUT,m,j)'''
                    p = HARM_traverseOrbit(m,j,pOUT,myDepth+1)
                    pOUT.children.append(p)
        print(pOUT)
'''def HARM_traverseOrbit(m,grammi,pIN,myDepth): #make trees
    pOUT.content = grammi #line of array
    pOUT.depth = myDepth #depth of tree path (Depth is the length of the path to its root)
    pOUT.parent = pIN #tree starts from that number
    pOUT.kids = []  #kids

    for j in range((grammi+1),size(m,2)):
        if m(grammi,j) > 0:
            if (not pOUT.parent | HARM_evaluateToTop(pOUT,m,j)):
                p = HARM_traverseOrbit(m,j,pOUT,myDepth+1)
                pOUT.kids.append(p)
                #pOUT.kids = [pOUT.kids p] in matlab'''