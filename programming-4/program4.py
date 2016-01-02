"""
Algorithms: Design and Analysis
Programming Assignment 4
DFS and Strongly Connected Components
Name: Tri Minh Cao
Email: trimcao@gmailcom
Date: November 2015
"""
import pickle
from collections import deque
import random

filename = "ex1.txt"
def load_graph(filename):
    """
    Method to load the graph from the provided text file
    """
    f = open(filename, 'r')
    # we build two graphs, one uses incoming edges and one outgoing edges
    outgo_graph = {}
    incom_graph = {}
    for line in f:
        # split the data 
        data = line.split()
        #print data
        num0 = int(data[0])
        num1 = int(data[1])
        # add the edge to outgo_graph
        if (num0 != num1):
            if (num0 in outgo_graph):
                outgo_graph[num0].add(num1)
            else:
                outgo_graph[num0] = set([num1])
            # add the edge to incom_graph
            if (num1 in incom_graph):
                incom_graph[num1].add(num0)
            else:
                incom_graph[num1] = set([num0])
    f.close()
    print "Load Graph Done!"
    return (outgo_graph, incom_graph)

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for key in graph:
        new_graph[key] = []
        for value in graph[key]:
            new_graph[key].append(value)
        
    return new_graph

# test load_graph function
#outgoing, incoming = load_graph("SCC.txt")
#print len(outgoing)
#print outgoing
#print incoming

#pickle.dump(incoming, open("SCC_incoming.p", "wb"))
#pickle.dump(outgoing, open("SCC_outgoing.p", "wb"))

# load data
#incoming = pickle.load(open("SCC_incoming.p", "rb"))
#outgoing = pickle.load(open("SCC_outgoing.p", "rb"))
#print len(incoming)

#outgoing, incoming = load_graph(filename)

def dfs_iter(graph, start_node, visited = None):
    """ 
    Depth-first Search
    Iterative implementation
    """
    # initialize a visited set
    if (visited == None):
        visited = set()
    current_visited = deque()
    # implement the stack using a list
    stack = []
    visited.add(start_node)
    stack.append(start_node)
    while (len(stack) > 0):
        current_node = stack.pop()
        # add current node to visited set
        current_visited.appendleft(current_node)
        if (current_node in graph): 
            for each_neighbor in graph[current_node]:
                if (not each_neighbor in visited):
                    visited.add(each_neighbor)
                    stack.append(each_neighbor)
    return current_visited

def finish_time(graph):
    """
    Helper function to find the finishing time order for the iterative DFS loop
    """
    visited = set()
    finishing_time = deque()
    # start the loop
    node_list = graph.keys()
    random.shuffle(node_list)
    for each_node in node_list:
        if (not each_node in visited):
            #print "Current node: ", each_node
            explored = dfs_iter(graph, each_node, visited)
            #print explored
            # update visited
            visited.update(explored)
            # create a new deque of explored nodes
            # note that we will appendleft to mimic the finishing time of a 
            # recursive function
            #print current_finishing
            # extend (to the right) the current_finishing to the main finishing_time
            finishing_time.extend(explored)
            #print finishing_time
    return list(finishing_time)

def find_scc(outgoing_graph, incoming_graph):
    """
    Kosaraju algorithm to find strongly connected components
    """
    # find finishing time
    finishing_time = finish_time(incoming_graph)
    #print finishing_time
    visited = set()
    scc_sizes = []
    for idx in range(len(finishing_time) - 1, -1, -1):
        current_node = finishing_time[idx]
        if (not current_node in visited):
            explored = dfs_iter(outgoing_graph, current_node, visited)
            # we should get a new scc 
            scc_sizes.append(len(explored))
            visited.update(explored)
    scc_sizes.sort(reverse=True)
    return scc_sizes[:5]

# test dfs_iter
filename = 'SCC.txt' 
outgoing, incoming = load_graph(filename)
#print dfs_iter(outgoing, 4)
#for each in incoming:
#    print each
#print dfs_iter(incoming, 4)
#print finish_time(incoming)
for dummy_idx in range(10):
    print find_scc(outgoing, incoming)
#print outgoing[20]
