# Autonomous Pacman Agent
Assignment for AI Planning for Autonomy (COMP90054). The Pacman agent designed finds paths through his maze world, both to reach a particular location and to collect food efficiently. The project is based on The University of California, Berkeley's Pacman search project (<a href="https://inst.eecs.berkeley.edu/~cs188/sp21/project1/">link</a>).

### Usage
Follow the project link for detailed explanation of each file.

- To visualise the Pacman agent following the A* algorithm with Manhattan distance as heuristic function, run
`python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar, heuristic=manhattanHeuristic`

- To visualise the Pacman agent following Recursive BFS as search function, run
`python pacman.py -l tinyMaze -p SearchAgent -a fn=rebfs`

- To check the performance of the A* algorithm, run
`python pacman.py -l task3Search -p AStarFoodSearchAgent`

-To visualise the Pacman agent following a Deceptive search strategy, run
`python pacman.py --layout deceptiveMap --pacman DeceptiveSearchAgentpi2` and `python pacman.py --layout deceptiveMap --pacman DeceptiveSearchAgentpi3`
