# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

INFINITY = float("inf")

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def expand(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (child,
        action, stepCost), where 'child' is a child to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that child.
        """
        util.raiseNotDefined()

    def getActions(self, state):
        """
          state: Search state

        For a given state, this should return a list of possible actions.
        """
        util.raiseNotDefined()

    def getActionCost(self, state, action, next_state):
        """
          state: Search state
          action: action taken at state.
          next_state: next Search state after taking action.

        For a given state, this should return the cost of the (s, a, s') transition.
        """
        util.raiseNotDefined()

    def getNextState(self, state, action):
        """
          state: Search state
          action: action taken at state

        For a given state, this should return the next state after taking action from state.
        """
        util.raiseNotDefined()

    def getCostOfActionSequence(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    mystack = util.Stack()
    startNode = (problem.getStartState(), '', 0, [])
    mystack.push(startNode)
    visited = set()
    while mystack :
        node = mystack.pop()
        state, action, cost, path = node
        if state not in visited:
            visited.add(state)
            if problem.isGoalState(state):
                path = path + [(state, action)]
                break
            succNodes = problem.expand(state)
            for succNode in succNodes:
                succState, succAction, succCost = succNode
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                mystack.push(newNode)
    actions = [action[1] for action in path]
    del actions[0]
    return actions

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    myqueue = util.Queue()
    startNode = (problem.getStartState(), '', 0, [])
    myqueue.push(startNode)
    visited = set()
    while myqueue:
        node = myqueue.pop()
        state, action, cost, path = node
        if state not in visited:
            visited.add(state)
            if problem.isGoalState(state):
                path = path + [(state, action)]
                break
            succNodes = problem.expand(state)
            for succNode in succNodes:
                succState, succAction, succCost = succNode
                newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                myqueue.push(newNode)
    actions = [action[1] for action in path]
    del actions[0]
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    #COMP90054 Task 1, Implement your A Star search algorithm here
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    openList = util.PriorityQueue() # priority is f = g + h
    initialState = problem.getStartState()
    initialNode = (initialState, "", 0, [])
    openList.push(initialNode, initialNode[2] + heuristic(initialState, problem))
    closedList = set()
    bestG = dict()  # maps each state to their corresponding best g

    while openList:
        node = openList.pop()
        state, action, cost, path = node

        # initiate an infinite g for unvisited states
        if state not in bestG:
            bestG[state] = INFINITY

        # when state is unvisited or re-open if there is a better g for state
        if state not in closedList or cost < bestG[state]:
            closedList.add(state)
            bestG[state] = cost # update state's best G

            # when goal is reached, break loop to return path
            if problem.isGoalState(state):
                path = path + [(state, action)]
                break

            # explore state's children
            succNodes = problem.expand(state)
            for succNode in succNodes:
                succState, succAction, succCost = succNode

                # if goal is reachable from succState, push to priority queue
                if heuristic(succState, problem) < INFINITY:
                    newNode = (succState, succAction, cost + succCost, path + [(state, action)])
                    openList.push(newNode, newNode[2] + heuristic(succState, problem))

    actions = [action[1] for action in path]
    del actions[0]

    return actions


def recursivebfs(problem, heuristic=nullHeuristic) :
    #COMP90054 Task 2, Implement your Recursive Best First Search algorithm here
    "*** YOUR CODE HERE ***"

    initialState = problem.getStartState()
    initialNode = [initialState, "", 0, [], heuristic(initialState, problem)]  # [state, action, g, path, f]

    path = rbfsExplore(problem, initialNode, INFINITY, heuristic)[0]
    actions = [action[1] for action in path]
    del actions[0]

    return actions

def rbfsExplore(problem, node, limit, heuristic):

    state = node[0]
    action = node[1]
    cost = node[2]
    path = node[3]

    # when goal state is reached, return path
    if problem.isGoalState(state):
        return path + [(state, action)], None

    succNodes = problem.expand(state)

    # when state has no children, return an empty list as signal for failure
    if not succNodes:
        return [], INFINITY

    # create list of corresponding nodes for state's children
    nodeList = []
    for succNode in succNodes:
        succState, succAction, succCost = succNode
        succFValue = cost + succCost + heuristic(succState, problem)
        newNode = [succState, succAction, cost + succCost, path + [(state, action)], succFValue]
        nodeList.append(newNode)

    while True:
        nodeList.sort(key=lambda x: x[4])   # sort nodes in ascending order of f
        bestNode = nodeList[0]  # node with lowest f

        # when lowest f is  greater than the f limit, return an empty list as signal for failure
        if bestNode[4] > limit:
            return [], bestNode[4]

        # get second lowest f (if it exists)
        try:
            secondBestF = nodeList[1][4]
        except:
            secondBestF = INFINITY

        result = rbfsExplore(problem, bestNode, min(limit, secondBestF), heuristic)
        bestNode[4] = result[1] # set appropriate f for best node

        # if result is not an empty list (not a failure) return the path
        if result[0]:
            return result

    
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
rebfs = recursivebfs
