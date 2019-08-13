# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:39:59 2019

@author: josia
"""


import sys
sys.path.append("/home/jsam/GitHub/AphrosLearn")
from state import State
from enums import *
import random

class randomAgent:
    
    def __init__(self, learningRate, discount, xLength, yLength):
        self.learningRate = learningRate
        self.discount = discount

    def update(self, oldState, nextState, reward, action):
        pass
    
    def get_next_action(self, state):
        x = random.random()
        if x < .25:
            return 'up'
        elif x < .5:
            return 'down'
        elif x < .75:
            return 'left'
        else:
            return 'right'