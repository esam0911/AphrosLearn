# AphrosLearn
Simple reinforcement learning simulator built in python.

GOAL: The goal of this simulator is to test basic concepts in reinforcement learning.

TASK: Create an optimal policy that will go the the origin in the least amount of steps, given its location relative to the origin. 
  This may seem rather pointless as you could programatically solve this easily (which will also be demonstrated as one of the agents) but the goal here is to show how reinforcemnt learning learns this optimal strategy. 
  
  For example, we know that if we are at the point (5, 5) relative to the origin, in order to go to the origin, we must go -5x and -5y. We could easily program this. But how would we solve this if we want the robot to learn? The main learning algorithm we will be exploring is called QLearn. QLearn will seek to create a QTable that represents all possible states and actions and the associated rewards. For example, a row in a Q table for this problem will have the following values 
  
                                       [StateX, StateY, Up, Down, Left, Right]
          
  As learning progresses, the rows will begin to fill out as the AI learns where the rewards are.

METHOD: We will create three basic modules. There will be a simiulator model, which will contain an NxM map of the enviorment as well as any methods necessary for the environment. We will have different agent modules, each with different parameters, different learning algorithms or different strategies. This will allow us to be able to swap out the agent with the same environment for better comparisons and testing. Finally, we will have a connector module that will interact between the agent and the simulation, will graph the results, will set the initial variables, etc. 
