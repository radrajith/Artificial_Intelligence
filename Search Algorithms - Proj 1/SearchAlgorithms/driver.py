##########################PROJECT 1 - Search Algorithms#######################
# 8-puzzle game is solved using
#   -   breadth first search (BFS)
#   -   depth first search (DFS)
#   -   A* Algorithms
##############################################################################

import sys          #to read the cmd line args
from MyQueue import MyQueue  #import the Queue class located in the same directory.
from Stack import Stack
import math
import time
size = 0
index_0=-1
nodes_expanded = 0
start = time.time();
####################################
# seperate the string of numbers, passed as command line argument, into list for easy reference.
def arrayConv(nums):
    global index_0, size
    temp = []
    temp.append(int(nums[0]))
    for i in range(len(nums)):
        if nums[i] == ',':
            temp.append(int(nums[i + 1]))
    index_0 = temp.index(0);
    size =  int(math.sqrt(len(temp)))
    return temp;
##########################################
# Create a queue. nums(contains the values of the table), empty string
# array(to be used to store path), index_0,
# location of the empty cell/0) are pushed onto the queue.
#until the queue is empty,
def bfs(nums):  #breadth first search
    global index_0, nodes_expanded
    max_search_depth = 0
    frontier = MyQueue()
    past = MyQueue()
    dummy = []
    frontier.enqueue([nums,index_0, -1, 'center'])
    past.enqueue([nums,index_0, -1, 'center'])
    while(frontier.isEmpty() == False):
        parent = frontier.dequeue()
        puzzle = parent[0]
        direction_Parent = parent[3]

        if(puzzle!=-1 and check(puzzle)==True):
            return [[puzzle,index_0,parent,direction], max_search_depth]
        nodes_expanded+=1
        #if the puzzle is not empty, then create its children up, down, left, right
        #create up child and check if the configuration already exists, if not then
        # add 'up' the path and enter it in the queue.
        if(direction_Parent!='down'):
            index_0 = parent[1]

            child = up(puzzle)
            direction = 'up'
            if(child !=-1):
                dummy.append([child, index_0, parent, direction])

        #create down child and check if the configuration already exists, if not then
        # add 'down' the path and enter it in the queue.
        if(direction_Parent!='up'):
            index_0 = parent[1]
            #nodes_expanded+=1
            child = down(puzzle)
            direction = 'down'
            if(child !=-1):
                dummy.append([child, index_0, parent, direction])

        #create left child and check if the configuration already exists, if not then
        # add 'left' the path and enter it in the queue.
        if(direction_Parent!='right'):
            index_0 = parent[1]
            #nodes_expanded+=1
            child = left(puzzle)
            direction = 'left'
            if(child !=-1):
                dummy.append([child, index_0, parent, direction])

        #create right child and check if the configuration already exists, if not then
        # add 'right' the path and enter it in the queue.
        if(direction_Parent!='left'):
            index_0 = parent[1]
            #nodes_expanded+=1
            child = right(puzzle)
            direction = 'right'
            if(child !=-1):
                dummy.append([child, index_0, parent, direction])

        #CHECK FOR DUPLICATES and add the unique ones to the queue past and
        children = pastCheck(past, dummy)
        for k in range(0,len(children)):
            past.enqueue(children[k])
            frontier.enqueue(children[k])
    return [-1, 0]  #if the end is reached take out the next in the queue.
#################################################
# check if the child already exisits in the queue.
def pastCheck(past, child):
    val = past.size()
    for i in range(0,val):
        if(len(child)==0):
            break
        parent = past.dequeue()
        past.enqueue(parent)
        for j in range(0, len(child)):
            if(j<len(child) and child[j][0]==parent[0]):
                child.remove(child[j])
    return child


def dfs(nums):
    global index_0, nodes_expanded
    max_search_depth =0
    count =0
    stack = Stack()
    past = Stack()
    stack.push([nums,index_0, -1,'center', 0])
    while(stack.isEmpty()==False):
        parent = stack.pop()
        count = parent[4]
        past.push(parent)
        puzzle = parent[0]
        #check if the puzzle is not empty and solved
        if(puzzle!=-1 and check(puzzle)==True):
            return [puzzle, max_search_depth]
        #if the puzzle is not empty, then create its children up, down, left, right
        if(puzzle!=-1):
            count+=1
            #create right child and check if the configuration already exists, if not then
            # add 'right' the path and enter it in the queue.
            index_0 = parent[1]
            nodes_expanded+=1
            child = right(puzzle)
            direction = 'right'
            if (child!=-1 and pastCheck(past, child) == False):
                stack.push([child, index_0, parent, direction, count])
            #create left child and check if the configuration already exists, if not then
            # add 'left' the path and enter it in the queue.
            index_0 = parent[1]
            nodes_expanded+=1
            child = left(puzzle)
            direction = 'left'
            if (child!=-1 and pastCheck(past, child) == False):
                stack.push([child, index_0, parent, direction, count])
            #create down child and check if the configuration already exists, if not then
            # add 'down' the path and enter it in the queue.
            index_0 = parent[1]
            nodes_expanded+=1
            child = down(puzzle)
            direction = 'down'
            if (child!=-1 and pastCheck(past, child) == False):
                stack.push([child, index_0, parent, direction, count])
            #create up child and check if the configuration already exists, if not then
            # add 'up' the path and enter it in the queue.
            index_0 = parent[1]
            nodes_expanded+=1
            child = up(puzzle)
            direction = 'up'
            if (child!=-1 and pastCheck(past, child) == False):
                stack.push([child, index_0, parent, direction, count])
        else:
            if(count>max_search_depth):
                max_search_depth = count

    return [-1, 0]  #if the end is reached take out the next in the queue.

def ast(nums):
    return;


def ida(nums):
    return;

def up(puzzle):
    nums = puzzle[:]
    global index_0
    if (index_0)>2:
        temp0 = index_0 -3
        temp = nums[temp0]
        nums[temp0] = 0
        nums[index_0] = temp
        index_0 = temp0;
        return nums
    else:
        return -1
def down(puzzle):
    nums = puzzle[:]
    global index_0
    if (index_0)<6:
        temp0 = index_0+3
        temp = nums[temp0]
        nums[temp0] = 0
        nums[index_0] = temp
        index_0 = temp0;
        return nums
    else:
        return -1
def left(puzzle):
    nums = puzzle[:]
    global index_0
    if (index_0 != 0 and index_0 != 3 and index_0 != 6):
        temp0 = index_0-1
        temp = nums[temp0]
        nums[temp0] = 0
        nums[index_0] = temp
        index_0 = temp0;
        return nums
    else:
        return -1
def right(puzzle):
    nums = puzzle[:]
    global index_0
    if (index_0 != 2 and index_0 != 5 and index_0 != 8):
        temp0 = index_0+1
        temp = nums[temp0]
        nums[temp0] = 0
        nums[index_0] = temp
        index_0 = temp0;
        return nums
    else:
        return -1
############################################
# check if the puzzle is solved by going thorough each cell
# and check for the numerical order ie, 0,1,2,3,4,5,6,7,8
def check(nums):
    for i in range(size*size):
        if (i != nums[i] ):
            return False
    return True
def stat(solution, max_search_depth):
    file = open("output.txt", "w")
    parent = solution[2]
    path = ''
    cost = 0
    while(parent[2] != -1):
        #parent = parent[2]
        path = parent[3] +','+ path
        parent = parent[2]
        cost+=1
    path = path[:-1]
    if(max_search_depth ==0):
        max_search_depth = cost     #for BFS the cost and the search depth are same
    file.write("path_to_goal: %s"%(path))
    file.write("\ncost_of_path: %d"%(cost))
    file.write("\nnodes_expanded: %d"%(nodes_expanded))
    file.write("\nsearch_depth: %d"%(cost))
    file.write("\nmax_search_depth: %d"%(max_search_depth))
    file.write("\nrunning_time: %d"%(time.time()-start))
    #file.write("max_ram_usage: %d"%(max_ram_usage))
#############################################
#arguments from the command line is analyzed and appropriate
# fucntions are called.
args = sys.argv
if len(args)>=2:
    board = arrayConv(args[2]);

    if (args[1]=="bfs"):
        ans = (bfs(board))
        stat(ans[0], ans[1])
    elif (args[1]=="dfs"):
        ans = stat(dfs(board))
        stat(ans[0], ans[1])
    elif (args[1]=="ast"):
        ans = stat(ast(board))
        stat(ans[0], ans[1])
