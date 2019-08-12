# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 21:48:09 2019

@author: josia
"""
from state import State
import random as rand

class gridSimulation:
    
    def __init__(self, goalReward, stepReward, stepPunishment, xLength, yLength):
        self.goalR = goalReward
        self.stepR = stepReward
        self.stepP = stepPunishment
        self.xSize = xLength
        self.ySize = yLength
        
    def update(self, action, state):
        if action.lower() == "up":
            reward = self.up(state)
        elif action.lower() == "down":
            reward = self.down(state)
        elif action.lower() == "right":
            reward = self.right(state)
        elif action.lower() == "left":
            reward = self.left(state)
        else:
            print("Invalid action!!! Returning None.")
            return None, None
        self.checkcurrentState()
        print("Reward:", reward)
        print("State:", self.currentState.x, self.currentState.y)
        return reward, self.currentState
    
    def right(self, state):
        self.currentState = State((state.x+1), state.y)
        if self.currentState.x == 0 and self.currentState.y == 0:
            return self.goalR
        elif abs(self.currentState.x) < abs(state.x):
            return self.stepR
        else:
            return self.stepP
        
    def left(self, state):
        self.currentState = State((state.x-1), state.y)
        if self.currentState.x == 0 and self.currentState.y == 0:
            return self.goalR
        elif abs(self.currentState.x) < abs(state.x):
            return self.stepR
        else:
            return self.stepP
        
    def up(self, state):
        self.currentState = State(state.x, (state.y+1))
        if self.currentState.x == 0 and self.currentState.y == 0:
            return self.goalR
        if abs(self.currentState.y) < abs(state.y):
            return self.stepR
        else:
            return self.stepP
        
    def down(self, state):
        self.currentState = State(state.x, (state.y-1))
        if self.currentState.x == 0 and self.currentState.y == 0:
            return self.goalR
        if abs(self.currentState.y) < abs(state.y):
            return self.stepR
        else:
            return self.stepP
    
    def checkcurrentState(self):
        if(self.currentState.x<(-self.xSize/2)):
            self.currentState.setX(-self.xSize/2)
        elif(self.currentState.x>(self.xSize/2)):
            self.currentState.setX(self.xSize/2)
            
        if(self.currentState.y<(-self.ySize/2)):
            self.currentState.setY(-self.ySize/2)
        elif(self.currentState.y>(self.ySize/2)):
            self.currentState.setY(self.ySize/2)
        
    def reset(self):
        self.currentState = State((rand.randint(-self.xSize/2, self.xSize/2)), rand.randint(-self.ySize/2, self.ySize/2))
        return self.currentState
    
    def getState(self):
        return self.currentState