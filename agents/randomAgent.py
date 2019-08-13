# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 22:39:59 2019

@author: josia
"""
from state import State

import random

class randomAgent:
    
    def __init__(self, learningRate, discount):
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