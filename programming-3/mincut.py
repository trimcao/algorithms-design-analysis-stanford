"""
Karger Minimum Cut Algo
Name: Tri Minh Cao
Email: trimcao@gmail.com
Date: October 2015
"""
import random

FILE = 'kargerMinCut.txt'
def load_graph(filename):
    """
    Method to load the graph from the provided text file
    """
    f = open(filename, 'r')
    graph = {}
    for line in f:
        # split the data by \tab and remove the \r\n at the end
        data = line.split('\t')[:-1]
        #print data
        graph[data[0]] = data[1:]
    f.close()
    return graph

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


GRAPH1 = {'1': ['2', '3'],
          '2': ['1', '4', '5', '3'],
          '3': ['1', '2'],
          '4': ['2'],
          '5': ['2'],
          }

#print GRAPH1

def edge_contract(graph, tail, head):
    """
    Method to contract an edge in an undirected graph
    tail and head are two endpoins of the edge

    Remember to copy a graph for each trial
    """
    new_node = tail + '_' + head
    # combine the edges of the original tail and head
    new_edges = list(graph[tail])
    new_edges.extend(graph[head])
    graph[new_node] = new_edges
    # remove the nodes tail and head from the graph
    graph.pop(tail, None)
    graph.pop(head, None)
    # change the node name of other edges to the new name
    for each_node in graph:
        edges = graph[each_node]
        for idx in range(len(edges)):
            # remove the edges that has old name, and replace them with
            # new name
            if (edges[idx] == tail) or (edges[idx] == head):
                #print edges[idx]
                edges[idx] = new_node
    
    # check if the new_node has any self-loops and remove them
    # actually build a new list seems faster (although requires more memory)
    old_edges = graph[new_node]
    new_edges = [edge for edge in old_edges if edge != new_node]
    graph[new_node] = new_edges

# test edge_contract:
#edge_contract(GRAPH1, '2', '3')
#print GRAPH1
#edge_contract(GRAPH1, '2_3', '1')
#print GRAPH1
#edge_contract(GRAPH1, '4', '5')
#print GRAPH1
#
def mincut(graph, trials):
    """
    Min Cut Algorithm by Karger
    
    output: the minimum cut value from all trials
    """
    mincut_values = []
    for dummy_idx in range(trials):
        print 'count: ', dummy_idx
        new_graph = copy_graph(graph)
        # test with one trial
        while (len(new_graph) > 2):
            random_key = random.choice(new_graph.keys())
            random_value = random.choice(new_graph[random_key])
            edge_contract(new_graph, random_key, random_value)
        # find the cut value
        cut = len(new_graph.values()[0])
        mincut_values.append(cut)
    return min(mincut_values)
    
# test mincut for one trial

graph = load_graph(FILE)
mincut_value = mincut(graph, 1200)
print mincut_value

