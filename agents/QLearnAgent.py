#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 09:25:29 2019

@author: jsam
"""

import sys
sys.path.append("/home/jsam/GitHub/AphrosLearn")
from state import State
import random

class qLearnAgent:
    
    def __init__(self, learningRate, discount,  xLength, yLength, iterations, explorationRate=1.0):
        self.xLength = xLength
        self.yLength = yLength
        self.qTable = [[[0 for i in range(4)] for j in range(yLength+1)] for q in range(xLength+1)]
        self.learningRate = learningRate
        self.discount = discount
        self.explorationRate = explorationRate
        self.explorationDelta = 1.0/float(iterations)

    def update(self, oldState, nextState, action, reward):
        old_value = self.qTable[int(oldState.x)][int(oldState.y)][int(self.convertActionToInt(action))]
        future_action = self.get_best_action(nextState)
        future_reward = self.qTable[int(nextState.x)][int(nextState.y)][int(self.convertActionToInt(future_action))]
        new_value = old_value + self.learningRate * (reward + self.discount * future_reward - old_value)
        self.qTable[int(oldState.x)][int(oldState.y)][int(self.convertActionToInt(action))] = new_value
        
        if self.explorationRate > 0:
            self.explorationRate -= self.explorationDelta
            
    def get_next_action(self, state):
        if random.random() > self.explorationRate: #Exploit
            return self.get_best_action(state)
        else: #Explore
            return self.get_random_action()
            
    def get_random_action(self):
        x = random.random()
        if x < .25:
            return 'up'
        elif x < .5:
            return 'down'
        elif x < .75:
            return 'left'
        else:
            return 'right'
        
    def get_best_action(self, state):
        best_move = 0
        table_state = self.qTable[int(state.x+(self.xLength/2))][int(state.y+(self.yLength/2))]
        for i in range(len(table_state)):
            if table_state[i] > table_state[best_move]:
                best_move = i
        if table_state[best_move] == 0:
            return self.get_random_action()
        
        if best_move == 0:
            return 'up'
        elif best_move == 1:
            return 'down'
        elif best_move == 2:
            return 'left'
        else:
            return 'right'
        
    def convertActionToInt(self, action):
        if action.lower() == 'up':
            return 0
        elif action.lower() == 'down':
            return 1
        elif action.lower() == 'left':
            return 2
        else:
            return 3