##########################PROJECT 1 - Search Algorithms#######################
# 8-puzzle game is solved using
#   -   breadth first search (BFS)
#   -   depth first search (DFS)
#   -   A* Algorithms
##############################################################################

import sys          #to read the cmd line args
import Queue
from pythonds.basic.stack import Stack
import math
import copy
size = 0
index_x = -1
index_y = -1
####################################
# seperate the string of numbers, passed as command line argument, into list for easy reference.
def arrayConv(nums):
    global size, index_x, index_y
    temp = [];
    temp.append(int(nums[0]))
    for i in range(len(nums)):
        if nums[i] == ',':
            temp.append(int(nums[i + 1]))
    size = int(math.sqrt(len(temp)))
    index = temp.index(0);
    index_x = int(index/size)
    index_y = int(index%size)
    brd = []
    for i in range(size):
        brd.append(temp[size*i:((size*i)+size)])
    return brd;
##########################################
# Create a queue. nums(contains the values of the table), empty string
# array(to be used to store path), index_x,
# index_y (location of the empty cell/0) are pushed onto the queue.
#until the queue is empty,
def bfs(nums):  #breadth first search
    global index_y, index_x
    path = []
    q = Queue.Queue(maxsize=0)
    past = Queue.Queue(maxsize=0)
    q.put([nums,[],index_x, index_y])
    while(q.empty() == False):
        node = q.get()
        past.put(node)
        ptr = node[0]
        path = node[1]
        #check if the puzzle is not empty and solved
        if(ptr!=-1 and check(ptr)==True):
            return [ptr, path]
        #if the puzzle is not empty, then create its children up, down, left, right
        #create up child and check if the configuration already exists, if not then
        # add 'up' the path and enter it in the queue.
        index_x = node[2]
        index_y = node[3]
        child = up(ptr)
        if (child!=-1 and pastQCheck(past, child) == False):
            path = node[1]+["up"]
            q.put([child, path, index_x, index_y])
        #create down child and check if the configuration already exists, if not then
        # add 'down' the path and enter it in the queue.
        index_x = node[2]
        index_y = node[3]
        child = down(ptr)
        if (child!=-1 and pastQCheck(past, child) == False):
            path = node[1]+["down"]
            q.put([child, path, index_x, index_y])
        #create left child and check if the configuration already exists, if not then
        # add 'left' the path and enter it in the queue.
        index_x = node[2]
        index_y = node[3]
        child = left(ptr)
        if (child!=-1 and pastQCheck(past, child) == False):
            path = node[1]+["left"]
            q.put([child, path, index_x, index_y])
        #create right child and check if the configuration already exists, if not then
        # add 'right' the path and enter it in the queue.
        index_x = node[2]
        index_y = node[3]
        child = right(ptr)
        if (child!=-1 and pastQCheck(past, child) == False):
            path = node[1]+["right"]
            q.put([child, path, index_x, index_y])
    return [-1, 0]  #if the end is reached take out the next in the queue.
#################################################
# check if the child already exisits in the queue.
def pastQCheck(past, child):
    val = past.qsize()
    for i in range(0,val):
        node = past.get()
        past.put(node)
        if(child==node[0]):
            return True
    return False
#chekc if the child already exists in the Stack
def pastSCheck(past, child):
    temp = copy.deepcopy(past)
    while temp.isEmpty() ==False:
        node = temp.pop()
        if(child==node[0]):
            return True
    return False
def dfs(nums):
    global index_y, index_x
    path = []
    stack = Stack()
    past = Stack()
    stack.push([nums,[],index_x, index_y])
    while(stack.isEmpty()==False):
        node = stack.pop()
        past.push(node)
        ptr = node[0]
        path = node[1]
        #check if the puzzle is not empty and solved
        if(ptr!=-1 and check(ptr)==True):
            return [ptr, path]
        #if the puzzle is not empty, then create its children up, down, left, right
        if(ptr!=-1):
            #create right child and check if the configuration already exists, if not then
            # add 'right' the path and enter it in the queue.
            index_x = node[2]
            index_y = node[3]
            child = right(ptr)
            if (child!=-1 and pastSCheck(past, child) == False):
                path = node[1]+["right"]
                stack.push([child, path, index_x, index_y])
            #create left child and check if the configuration already exists, if not then
            # add 'left' the path and enter it in the queue.
            index_x = node[2]
            index_y = node[3]
            child = left(ptr)
            if (child!=-1 and pastSCheck(past, child) == False):
                path = node[1]+["left"]
                stack.push([child, path, index_x, index_y])
            #create down child and check if the configuration already exists, if not then
            # add 'down' the path and enter it in the queue.
            index_x = node[2]
            index_y = node[3]
            child = down(ptr)
            if (child!=-1 and pastSCheck(past, child) == False):
                path = node[1]+["down"]
                stack.push([child, path, index_x, index_y])
            #create up child and check if the configuration already exists, if not then
            # add 'up' the path and enter it in the queue.
            index_x = node[2]
            index_y = node[3]
            child = up(ptr)
            if (child!=-1 and pastSCheck(past, child) == False):
                path = node[1]+["up"]
                stack.push([child, path, index_x, index_y])
    return [-1, 0]  #if the end is reached take out the next in the queue.

def ast(nums):
    return;


def ida(nums):
    return;

def up(brd):
    nums = copy.deepcopy(brd)
    global index_x, index_y
    if (index_x)>0:
        tempx = index_x -1
        tempy = index_y
        temp = nums[tempx][tempy]
        nums[tempx][tempy] = 0
        nums[index_x][index_y] = temp
        index_x = tempx;
        index_y = tempy;
        return nums
    else:
        return -1
def down(brd):
    nums = copy.deepcopy(brd)
    global index_x, index_y
    if (index_x)<size-1:
        tempx = index_x +1
        tempy = index_y
        temp = nums[tempx][tempy]
        nums[tempx][tempy] = 0
        nums[index_x][index_y] = temp
        index_x = tempx;
        index_y = tempy;
        return nums
    else:
        return -1
def left(brd):
    nums = copy.deepcopy(brd)
    global index_x, index_y
    if (index_y )>0:
        tempx = index_x
        tempy = index_y - 1
        temp = nums[tempx][tempy]
        nums[tempx][tempy] = 0
        nums[index_x][index_y] = temp
        index_x = tempx;
        index_y = tempy;
        return nums
    else:
        return -1
def right(brd):
    nums = copy.deepcopy(brd)
    global index_x, index_y
    if (index_y)<size-1:
        tempx = index_x
        tempy = index_y + 1
        temp = nums[tempx][tempy]
        nums[tempx][tempy] = 0
        nums[index_x][index_y] = temp
        index_x = tempx;
        index_y = tempy;
        return nums
    else:
        return -1
############################################
# check if the puzzle is solved by going thorough each cell
# and check for the numerical order.
def check(nums):
    for i in range(size*size):
        if (i != nums[(i / size)][(i % size)] ):
            return False
    return True
#############################################
#arguments from the command line is analyzed and appropriate
# fucntions are called.
args = sys.argv
if len(args)>=2:
    board = arrayConv(args[2]);

    if (args[1]=="bfs"):
        ans = bfs(board)
        print(ans[0])
        print(ans[1])
    elif (args[1]=="dfs"):
        ans = dfs(board)
        print(ans[0])
        print(ans[1])
    elif (args[1]=="ast"):
        ans = ast(board)
    elif (args[1]=="ida"):
        ans = ida(board)
