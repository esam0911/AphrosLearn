# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 17:17:40 2019

@author: josia
"""

from state import State
from simulation import gridSimulation as sim
from randomAgent import randomAgent
import random
import csv
import argparse

def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--agent', type=str, default='RANDOM', help='Which agent to use')
    parser.add_argument('--learning_rate', type=float, default=0.1, help='How quickly the algorithm tries to learn')
    parser.add_argument('--discount', type=float, default=0.95, help='Discount for estimated future action')
    parser.add_argument('--iterations', type=int, default=2000, help='Iteration count')
    parser.add_argument('--xlength', type=int, default=10, help='X dimension of the grid')
    parser.add_argument('--ylength', type=int, default=10, help='Y dimenstion of the grid')
    parser.add_argument('--sessionLength', type=int, default=25, help='Number of moves allowed per round')
    parser.add_argument('--goalReward', type=int, default=200, help='Reward given when AI reaches the goal')
    parser.add_argument('--stepReward', type=int, default=5, help='Reward given when AI moves closer to goal')
    parser.add_argument('--stepPunishment', type=int, default=-5, help='Punishment given when AI moves further from goal')

    FLAGS, unparsed = parser.parse_known_args()

    
    # select agent
    if FLAGS.agent == 'RANDOM':
        agent = randomAgent()
    else:
        print("Invalid selection. Please try again.")
        return

    # setup simulation
    dungeon = sim(FLAGS.goalReward, FLAGS.stepReward, FLAGS.stepPunishment, FLAGS.xlength, FLAGS.ylength)

    total_global_reward = 0
    # main loop for episodes
    for i in range(FLAGS.iterations):
        # main loop for sessions in each episode
        dungeon.reset()
        total_reward = 0 # Score keeping
        for j in range(FLAGS.sessionLength):
            old_state = dungeon.state # Store current state
            action = agent.get_next_action(old_state) # Query agent for the next action
            reward, new_state = dungeon.update(action, old_state) # Take action, get new state and reward
            if reward == None or new_state == None:
                print("There was an error with one of the actions chosen.")
                return
            agent.update(old_state, new_state, action, reward) # Let the agent update internals
    
            total_reward += reward # Keep score
            
            if reward == FLAGS.goalReward:
                print("We made it to the goal on episode "+str(i)+" and session "+str(j))
                break
        print("The total reward for episode "+str(i)+" session "+str(j)+" is "+str(total_reward))
        total_global_reward += total_reward
    print("The training is over! The total global reward is "+str(total_global_reward))
    
if __name__ == "__main__":
    main()
