#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 08:55:26 2019

@author: jsam
"""

import sys
sys.path.append("/home/jsam/GitHub/AphrosLearn")
from state import State

class optimalAgent:
    
    def __init__(self, learningRate, discount, xLength, yLength):
        self.learningRate = learningRate
        self.discount = discount

    def update(self, oldState, nextState, reward, action):
        pass
    
    def get_next_action(self, state):
        if state.y < 0:
            return 'up'
        elif state.y > 0:
            return 'down'
        elif state.x < 0:
            return 'right'
        else:
            return 'left'