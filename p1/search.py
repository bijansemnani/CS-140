# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).

  You do not need to change anything in this class, ever.
  """

  def startingState(self):
    """
    Returns the start state for the search problem
    """
    util.raiseNotDefined()

  def isGoal(self, state): #isGoal -> isGoal
    """
    state: Search state

    Returns True if and only if the state is a valid goal state
    """
    util.raiseNotDefined()

  def successorStates(self, state): #successorStates -> successorsOf
    """
    state: Search state
     For a given state, this should return a list of triples,
     (successor, action, stepCost), where 'successor' is a
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental
     cost of expanding to that successor
    """
    util.raiseNotDefined()

  def actionsCost(self, actions): #actionsCost -> actionsCost
    """
      actions: A list of actions to take

     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
    """
    util.raiseNotDefined()


def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first [p 85].

  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm [Fig. 3.7].

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())
  """
  print "Start:", problem.startingState()
  print "Is the start a goal?", problem.isGoal(problem.startingState())
  print "Start's successors:", problem.successorStates(problem.startingState())

  stack = util.Stack()
  state = problem.startingState()

  stack.push((state, [], []))
  while stack:
    curr, direction, visit = stack.pop()
    if not curr in visit:
        visit + [curr]
    for position, dir, cost in problem.successorStates(curr):
        if not position in visit:
            if problem.isGoal(position):
                return direction + [dir]
            stack.push((position, direction+[dir], visit +[position]))




def breadthFirstSearch(problem):
  "Search the shallowest nodes in the search tree first. [p 81]"

  frontier = util.Queue()
  state = problem.startingState()

  frontier.push((state, []))
  explored = []
  while frontier:
    parent, actions = frontier.pop()
    for currState, dir, step in problem.successorStates(parent):
        if not currState in explored:
            if problem.isGoal(currState):
                return actions + [dir]
            frontier.push((currState, actions + [dir]))
            explored.append(currState)

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  frontier = util.PriorityQueue()
  state = problem.startingState()

  frontier.push((state, []),0)
  explored = []
  while frontier:
    curr, actions = frontier.pop()
    if problem.isGoal(curr):
        return actions
    explored.append(curr)
    for child, dir, step in problem.successorStates(curr):
        if not child in explored:
            newAct = actions + [dir]
            frontier.push((child, newAct), problem.actionsCost(newAct))
        """elif child in frontier:
            if problem.actionsCost(act) < newAct:
                frontier.push((child, act), problem.actionsCost(act))"""


def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  alist = util.PriorityQueue()
  state = problem.startingState()

  alist.push((state, []),heuristic(state, problem))
  explored = []
  while alist:
    curr, actions = alist.pop()
    if problem.isGoal(curr):
        return actions
    explored.append(curr)
    for currState, dir, step in problem.successorStates(curr):
        "child, act = problem.successorStates(currState)"
        if not currState in explored:
            newAct = actions + [dir]
            fVal = problem.actionsCost(newAct) + heuristic(currState, problem)
            alist.push((currState, newAct), fVal)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
