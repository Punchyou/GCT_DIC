# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 23:38:56 2018

@author: Maria
"""

from HARM_findParentPath_func import HARM_findParentPath #den to exw ksekinhsei akoma auto to script

def HARM_evaluateToTop(tr, pinakas, grammi):
       parentPath = HARM_findParentPath(tr.parent)
       b = 1
       for i in range(0, parentPath):
              if pinakas[grammi][parentPath[i]] == 0:
                     b = 0
                     break
       return b