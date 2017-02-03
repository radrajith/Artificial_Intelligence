# Artifical Intelligence (edx)

## Week 2

### 2.1 Intelligence Agents

**Agents** - an agent is anything that can be viewed as perceiving its environment through sensors and acting upon that environment through actuators. Its made up of Architecture(hardware of the agent) and Program(mind of the program)

**PEAS** - Performance, Environment, Actuators, Sensors

**Environment Types**

![Enironment Types](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/environment_types.PNG?raw=true)
![Enironment Types 2](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/environment_types_2.PNG?raw=true)

**Environment Types examples

![Environment Types example](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/environment_types_example.PNG?raw=true)

**Agent types**

- simple reflex agent -

![simple_reflex_agent](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/simple_reflex_agent.PNG?raw=true)

- model based reflex agent

![model_reflex_agent](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/model_reflex_agent.PNG?raw=true)

- goal based Agents

![goal_agent](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/goal_agent.PNG?raw=true)

- utility based agents

![utility_agent](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/utility_agent.PNG?raw=true)

**Learning agent** - This generalizes all the agents above. Instead of specifying each and every scenario, this will learn.

![learning_agent](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/learning_agent.PNG?raw=true)

Agent internal States can be represented in different ways:

- Atomic representation : each state of the world is a blackbox that has no internal structure. Eg: finding driving route (each state being a city). AI algorithm: markov Chains

- Factored Representation : Each state has some attribute value properties. Eg: GPS location, amount of gas in the tank. AI algorithm: constraint satisfaction, and bayesian networks.

- Structured representation : Relationships between the objects of a state can be explicitly expressed. AI algorithms: first order logic, knowledge based learning, natural language understanding.

### 2.2 Search Agents

#### There are two types of agents

reflex agents - use mapping from states to actions (essentially table look up). lowest level of intelligence

goal based agents - problem solving or planning agents. Agent identifies the action that leads to a goal. Eg: solving a maze.

** Problem solving as search **
![search_solving](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/search_solving.PNG?raw=true)

** Problem Formulation **
![problem_formulation](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/problem_formulation.PNG?raw=true)
* Intelligence Level * (from low to high)
- reflex agent
- state based (search agent)

** Search space ** - an abstract configuration represented by a search tree or graph of possible solutions
![search_space](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/search_space.PNG?raw=true)

### 2.3 Uninformed Search
Breadth first search, depth first search, depth limited search, iterative deepening search, uniform cost search.

#### Breadth-First Search(BFS)

Start from the root, and go to each level. Searching level by level until we reach the target. use queues(FIFO) to explore the tree. Time and space O(b^d). b - breadth, d - depth

![bfs](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/bfs.PNG?raw=true)

![bfs_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/bfs_algo.PNG?raw=true)

#### Depth-First Search(DFS)

Start with the root, traverse depth before looking at the neighbor. Search the depth rather than by level. last in first out, Stack(LIFO) . time O(b^m) [bad if m is much larger than d], space O(bm), m - maximum possibility of search space.

![dfs](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/dfs.PNG?raw=true)

![dfs_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/dfs_algo.PNG?raw=true)

#### Depth-Limited Search(DLS) and Uniform-cost Search(UCS)
DLS is essentially DFS, with iterative search. For each level, repeat the DFS.
UCS uses heap data structure. we use BFS to find the shallowest solution. so BFS is modified to prioritize the cost [expand node n with lowest path cost g(n)]. The cost like going to different cities map. uses priority queue

![dls](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/dls.PNG?raw=true)

![ucs_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/ucs_algo.PNG?raw=true)

***
## Week 3

### 3.1 Heuristics and Greedy Search Algorithm

#### Greedy Search

The search is based on the shortest straight line distance/cost(h(n)) to the goal. The search is based on the cost, might not always be the efficient one.

![greedy_search](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/greedy_search.PNG?raw=true)

![greedy_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/greedy_algo.PNG?raw=true)

### 3.2 A* search
- minimize the total estimated solution cost (f(n))
- combines :
  - g(n)  : cost to reach node n
  - h(n)  : cost to get from n to goal
  - f(n)  : g(n) + h(n) - the estimated cost of the cheapest solution

![a_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/a_algo.PNG?raw=true)

As long as the heuristic is admissible then an optimal solution can be reached.

![admissible_heuristic](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/admissible_heuristic.PNG?raw=true)

### 3.4 Local Search
- Tree climb algorigthm
  climbing a hill and reaching a global peak.
- Genetic algorightm
  finding a solution based on natural selection. Solution chosen from two parents and the result is mutated to obtain the optimal solution.
  ![genetic_algo](https://github.com/radrajith/Artificial_Intelligence/blob/master/images/genetic_algo.PNG?raw=true)

  ***
  
