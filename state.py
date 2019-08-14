# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:02:40 2019

@author: josia
"""

class State:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    
    def setY(self, y):
        self.y = int(y)
    
    def setX(self, x):
        self.x = int(x)