# qlearningAgents.py
# ------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import *
from learningAgents import ReinforcementAgent
from featureExtractors import *

import random,util,math

class QLearningAgent(ReinforcementAgent):
  """
    Q-Learning Agent

    Functions you should fill in:
      - getQValue
      - getAction
      - getValue
      - getPolicy
      - update

    Instance variables you have access to
      - self.epsilon (exploration prob)
      - self.alpha (learning rate)
      - self.discountRate (discount rate)

    Functions you should use
      - self.getLegalActions(state)
        which returns legal actions
        for a state
  """
  def __init__(self, **args):
    "You can initialize Q-values here..."
    ReinforcementAgent.__init__(self, **args)
    self.qValues = util.Counter()


  def getQValue(self, state, action):
    """
      Returns Q(state,action)
      Should return 0.0 if we never seen
      a state or (state,action) tuple
    """
    """Description: Return a qValue for the given action and state from
    util.Counter
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    return self.qValues[(state,action)]
    util.raiseNotDefined()
    """ END CODE """



  def getValue(self, state):
    """
      Returns max_action Q(state,action)
      where the max is over legal actions.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return a value of 0.0.
    """
    """Description: I make a list to save the q array in  then for all
    legal actions I get the q Value and add it to my qarray and then
    if the qarray is empty then I return 0.0 else I just return the maximum
    q value
    """
    """ YOUR CODE HERE """
    qarray = []
    for action in self.getLegalActions(state):
        qarray.append(self.getQValue(state, action))
    if not qarray:
        return 0.0
    return max(qarray)
    util.raiseNotDefined()
    """ END CODE """

  def getPolicy(self, state):
    """
      Compute the best action to take in a state.  Note that if there
      are no legal actions, which is the case at the terminal state,
      you should return None.
    """
    """Description: Here I am first intializing the max to - infinity.
    Then I get the action from the legal actions list and get the q values
    for each action.  If the q value is greater than the current max I
    replace the current max with the value and I erase the action ActionArray
    and replace it with the current action.  If val and currMax are equal
    I only append the action to the current action array and then I choose
    at random one of the values in the action array and return it. ]
    """
    """ YOUR CODE HERE """

    QVals = self.qValues.copy()
    currVal = None
    currMax = float("-inf")
    ActionArray = []
    actions = self.getLegalActions(state)
    if len(actions) == 0:
        return None
    for action in actions:
        val = self.getQValue(state, action)
        if val > currMax:
            currMax = val
            ActionArray = [action]
        elif val == currMax:
            ActionArray.append(action)

    return random.choice(ActionArray)
    util.raiseNotDefined()
    """ END CODE """

  def getAction(self, state):
    """
      Compute the action to take in the current state.  With
      probability self.epsilon, we should take a random action and
      take the best policy action otherwise.  Note that if there are
      no legal actions, which is the case at the terminal state, you
      should choose None as the action.

      HINT: You might want to use util.flipCoin(prob)
      HINT: To pick randomly from a list, use random.choice(list)
    """

    # Pick Action
    legalActions = self.getLegalActions(state)
    action = None

    if len(legalActions) > 0:
        if util.flipCoin(self.epsilon):
            action = random.choice(legalActions)
        else:
            action = self.getPolicy(state)
    return action


    """Description: I first check if there are any legal actions available.
    If there are then I check if flip coin is true or false.  If its true then the action
    that is returned is random from the legalActions.  Else we return the best policy action.
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """


  def update(self, state, action, nextState, reward):
    """
      The parent class calls this to observe a
      state = action => nextState and reward transition.
      You should do your Q-Value update here

      NOTE: You should never call this function,
      it will be called on your behalf
    """
    """Description: This is where I update the q value using the q value formula.
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    self.qValues[(state, action)] = self.getQValue(state,action) + self.alpha*(reward + self.discountRate * self.getValue(nextState) - self.getQValue(state,action))
    """ END CODE """

class PacmanQAgent(QLearningAgent):
  "Exactly the same as QLearningAgent, but with different default parameters"

  def __init__(self, epsilon=0.05,gamma=0.8,alpha=0.2, numTraining=0, **args):
    """
    These default parameters can be changed from the pacman.py command line.
    For example, to change the exploration rate, try:
        python pacman.py -p PacmanQLearningAgent -a epsilon=0.1

    alpha    - learning rate
    epsilon  - exploration rate
    gamma    - discount factor
    numTraining - number of training episodes, i.e. no learning after these many episodes
    """
    args['epsilon'] = epsilon
    args['gamma'] = gamma
    args['alpha'] = alpha
    args['numTraining'] = numTraining
    self.index = 0  # This is always Pacman
    QLearningAgent.__init__(self, **args)

  def getAction(self, state):
    """
    Simply calls the getAction method of QLearningAgent and then
    informs parent of action for Pacman.  Do not change or remove this
    method.
    """
    action = QLearningAgent.getAction(self,state)
    self.doAction(state,action)
    return action


class ApproximateQAgent(PacmanQAgent):
  """
     ApproximateQLearningAgent

     You should only have to overwrite getQValue
     and update.  All other QLearningAgent functions
     should work as is.
  """
  def __init__(self, extractor='IdentityExtractor', **args):
    self.featExtractor = util.lookup(extractor, globals())()
    PacmanQAgent.__init__(self, **args)

    # You might want to initialize weights here.

  def getQValue(self, state, action):
    """
      Should return Q(state,action) = w * featureVector
      where * is the dotProduct operator
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """

  def update(self, state, action, nextState, reward):
    """
       Should update your weights based on transition
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """

  def final(self, state):
    "Called at the end of each game."
    # call the super-class final method
    PacmanQAgent.final(self, state)

    # did we finish training?
    if self.episodesSoFar == self.numTraining:
      # you might want to print your weights here for debugging
      util.raiseNotDefined()
