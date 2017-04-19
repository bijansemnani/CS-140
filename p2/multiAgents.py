# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util
from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPosition = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    foodList = oldFood.asList()
    foodDistance = [manhattanDistance(food, newPosition) for food in foodList]
    ghostPositions = successorGameState.getGhostPositions()
    ghostDistance = [manhattanDistance(newPosition, ghost) for ghost in ghostPositions]
    maxScared = max(newScaredTimes)
    minfood = min(foodDistance)
    minGhost = min(ghostDistance)
    newMin = 0

    "*** YOUR CODE HERE ***"
    if action == 'Stop':#check if action is stop if so return bad val
        return float("-inf")-1
    if minGhost < 2:#if pacman near ghost run away
        return float("-inf")
    if minfood > 7:#if food distance is greater than 7 return bad val
        return -1
    if minfood > 0:#go for closest food
        newMin = .5*(1/minfood)
    if maxScared > 0:#go for longest scared time ghost
        newMin = 1/minGhost
    return newMin + successorGameState.getScore()



def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.treeDepth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.treeDepth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"

    def minimax(state, depth, ghost, maxPlayer):
        if state.isWin() or state.isLose(): #check if terminal node
            return state.getScore()
        #Max Player
        if maxPlayer:
            bestValue = float("-inf") #initialize v to -infinity
            actions = state.getLegalActions(0)#get legal actions list
            bestAction = Directions.STOP #initialize best action to stop
            for action in actions: #look through actions
                nextState = state.generateSuccessor(0, action) #get next state
                score = minimax(nextState, depth, 1, False) #get score depends on min player
                if (score > bestValue): #update score
                    bestValue = score
                    bestAction = action
            if depth == 0:
                return bestAction
            return bestValue

        #Min Player
        else:
            bestValue = float("inf") #initialize to infinity
            actions = state.getLegalActions(ghost)
            nextGhost = ghost + 1 #increment to next ghost
            if ghost == state.getNumAgents() -1: #if last ghost then next turn is pacman
                nextGhost = 0
            for action in actions:
                nextState = state.generateSuccessor(ghost, action)
                if nextGhost == 0: #if pacman's turn
                    if depth == self.treeDepth -1: #if terminal return eval
                        score = self.evaluationFunction(nextState)
                    else:#else score depends on pacman's turn
                        score = minimax(nextState, depth+1, 0, True)
                else: #else score depends on nextGhost turn
                    score = minimax(nextState, depth, nextGhost, False)
                bestValue = min(bestValue, score)
            return bestValue
    return minimax(gameState, 0, 0, True)
    util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """

  def getAction(self, gameState):
    """
      Returns the minimax action using self.treeDepth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"

    def minimax(state, depth, ghost, maxPlayer, alpha, beta):
        if state.isWin() or state.isLose():
            return state.getScore()
        if maxPlayer:
            bestValue = float("-inf")
            actions = state.getLegalActions(0)
            bestAction = Directions.STOP
            for action in actions:
                nextState = state.generateSuccessor(0, action)
                score = minimax(nextState, depth, 1, False, alpha, beta)
                if (score > bestValue):
                    bestValue = score
                    bestAction = action
                if bestValue > beta: #check if v is greater than beta if so prune
                    return bestValue
                alpha = max(alpha, score) #update alpha if score is better than curr alpha
            if depth == 0:
                return bestAction
            return bestValue

        else:
            bestValue = float("inf")
            actions = state.getLegalActions(ghost)
            nextGhost = ghost + 1
            if ghost == state.getNumAgents() -1:
                nextGhost = 0
            for action in actions:
                nextState = state.generateSuccessor(ghost, action)
                if nextGhost == 0:
                    if depth == self.treeDepth -1:
                        score = self.evaluationFunction(nextState)
                    else:
                        score = minimax(nextState, depth+1, 0, True, alpha, beta)
                else:
                    score = minimax(nextState, depth, nextGhost, False, alpha, beta)
                bestValue = min(bestValue, score)
                if bestValue < alpha:#if v is smaller than alpha then prune
                    return bestValue
                beta = min(beta, bestValue)
            return bestValue
    return minimax(gameState, 0, 0, True, float("-inf"), float("inf"))

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.treeDepth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"

    def minimax(state, depth, ghost, maxPlayer):
        if state.isWin() or state.isLose():
            return state.getScore()
        if maxPlayer:
            bestValue = float("-inf")
            actions = state.getLegalActions(0)
            bestAction = Directions.STOP
            for action in actions:
                nextState = state.generateSuccessor(0, action)
                score = minimax(nextState, depth, 1, False)
                if (score > bestValue):
                    bestValue = score
                    bestAction = action
            if depth == 0:
                return bestAction
            return bestValue

        else:
            bestValue = float("inf")
            actions = state.getLegalActions(ghost)
            nextGhost = ghost + 1
            probability = 1.0/len(actions) #probability of each action
            if ghost == state.getNumAgents() -1:
                nextGhost = 0
            for action in actions:
                nextState = state.generateSuccessor(ghost, action)
                if nextGhost == 0:
                    if depth == self.treeDepth -1:
                        score = self.evaluationFunction(nextState)
                        score += probability * score #update score with the probability
                    else:
                        score = minimax(nextState, depth+1, 0, True)
                        score += probability * score #update score with the probability
                else:
                    score = minimax(nextState, depth, nextGhost, False)
                    score += probability * score #update score with the probability
                bestValue = score #return score
            return bestValue
    return minimax(gameState, 0, 0, True)

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: I was unable to get pacman to win 
  """
  "*** YOUR CODE HERE ***"

  pacman = currentGameState.getPacmanPosition()
  score = currentGameState.getScore()
  oldFood = currentGameState.getFood()
  foodList = oldFood.asList()
  newGhostStates = currentGameState.getGhostStates()
  ghostPositions = currentGameState.getGhostPositions()
  newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
  capsules = currentGameState.getCapsules()

  foodDist = []
  ghostDist = []
  scaredGhost = []
  capDist = []

  closeFood = 0
  closeGhost = 0
  scared = 0

  for ghost in ghostPositions:
      for pos in newGhostStates:
          if pos.scaredTimer > 0:
            scaredGhost.append(manhattanDistance(ghost, pacman))
            scared = min(scaredGhost)
      ghostDist.append(manhattanDistance(ghost, pacman))
      closeGhost = min(ghostDist)

  for food in foodList:
      foodDist.append(1.0/manhattanDistance(food, pacman))
      closeFood = min(foodDist)

  for capsule in capsules:
       capDist.append(1.0/manhattanDistance(capsule, pacman))
       cap = min(capDist)

  if scared < closeFood:
      score = score * .5
  if capDist < closeFood:
      score += score * .35
  if closeFood < closeGhost:
      score += score * .25
  else:
      score += -2 * score

  return score
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
