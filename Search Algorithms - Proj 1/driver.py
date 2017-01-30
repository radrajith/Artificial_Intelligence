import sys          #to read the cmd line args
import Queue
import math
import copy
size = 0
index_x = -1
index_y = -1
def arrayConv(nums):  # seperate the string of numbers into list for easy reference.
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

def bfs(nums):
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

        if(ptr!=-1 and check(ptr)==True):
            return [ptr, path]
        if(ptr!=-1):
            index_x = node[2]
            index_y = node[3]
            child = up(ptr)
            if (pastCheck(past, child) == False):
                path = node[1]+["up"]
                q.put([child, path, index_x, index_y])
            index_x = node[2]
            index_y = node[3]
            child = down(ptr)
            if (pastCheck(past, child) == False):
                path = node[1]+["down"]
                q.put([child, path, index_x, index_y])
            index_x = node[2]
            index_y = node[3]
            child = left(ptr)
            if (pastCheck(past, child) == False):
                path = node[1]+["left"]
                q.put([child, path, index_x, index_y])
            index_x = node[2]
            index_y = node[3]
            child = right(ptr)
            if (pastCheck(past, child) == False):
                path = node[1]+["right"]
                q.put([child, path, index_x, index_y])

    return [-1, 0]
def pastCheck(past, child):
    while past.empty() ==False:
        node = past.get()
        if(child==node):
            return True
    return False

def dfs(nums):
    return;


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
def check(nums):
    for i in range(size*size):
        if (i != nums[(i / size)][(i % size)] ):
            return False
    return True

args = sys.argv
if len(args)>=2:
    board = arrayConv(args[2]);

    if (args[1]=="bfs"):
        ans = bfs(board)
        print(ans[0])
        print(ans[1])
    elif (args[1]=="dfs"):
        ans = dfs(board)
    elif (args[1]=="ast"):
        ans = ast(board)
    elif (args[1]=="ida"):
        ans = ida(board)


