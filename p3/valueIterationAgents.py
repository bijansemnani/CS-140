# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discountRate = 0.9, iters = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.

      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discountRate = discountRate
    self.iters = iters
    self.values = util.Counter() # A Counter is a dict with default 0

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    currVal = 0
    for i in range(self.iters):
        vals = self.values.copy()
        for state in self.mdp.getStates():
            actions = self.mdp.getPossibleActions(state)
            val = None
            for action in actions:
                currVal = self.getQValue(state,action)
                if val < currVal:
                    val = currVal
            if val == None:
                val = 0
            vals[state]= val
        self.values = vals

    """ END CODE """

  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    util.raiseNotDefined()
    """ END CODE """

  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """
    qVal = 0
    for nextState, prob in self.mdp.getTransitionStatesAndProbs(state, action):
        qVal += prob * (self.mdp.getReward(state,action, nextState) + self.discountRate*self.values[nextState])
    return qVal
    util.raiseNotDefined()
    """ END CODE """

  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """

    """Description:
    [Enter a description of what you did here.]
    """
    """ YOUR CODE HERE """

    actions = self.mdp.getPossibleActions(state)
    if len(actions) == 0:
        return None
    Qval = None
    bestAction = None
    for action in actions:
        currQ = self.getQValue(state,action)
        if currQ > Qval:
            Qval = currQ
            bestAction = action
    return bestAction
    util.raiseNotDefined()
    """ END CODE """

  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
