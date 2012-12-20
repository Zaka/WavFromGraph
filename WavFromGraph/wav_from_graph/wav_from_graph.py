import networkx as nx
import numpy as np
from scipy.io.wavfile import write

def flatten_graph(graph, root):
    if root['type'] == 'concatenation':
        l = []
        for succesor in graph.successors(root):
            l.extend(flatten_graph(graph,succesor))
        return l
    else:
        return [root['value']]
    
def tree_root(graph):
    l = nx.topological_sort(graph)
    return graph.node[l[0]]

def wav(graph):
    music = flatten_graph(graph, tree_root(graph))
    write('test.wav', 44100, music)

#===============================================================================
# Mono sin wave
#===============================================================================
freq = 440.0
frate = 9000.0
amp = 4000.0

seconds = 4.0
start = 0
stop = seconds * 44100.0
step = 1

data = amp * np.sin(2 * np.pi * freq * np.arange(start, stop, step) / frate)
scaled = np.int16(data / np.max(np.abs(data)) * 65536)
#===============================================================================
# write('test.wav', 44100, scaled)
#===============================================================================
