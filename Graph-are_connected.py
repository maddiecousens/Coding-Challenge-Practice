# Cracking the Coding Interview
# Question 4.1

## Uses ideas from HB Coding Challenge Friends Problem
# Learned:
"""
Sets are created like this "set()" if empty but with curly braces if you
are creating AND adding something {'hi'}

Adjacency Lists in Graphs are best as sets

Instantiate the Node with a list, but set default to None then say
ajacent = adjacent or [], this will create a NEW empty list for each instance
if someone didn't add any adjacent nodes

Initialize Graphs with a nodes set

*** DFS using recursion, I found the implementation confusing... revist after
more Recursion Practice

BFS - use Queue but just import from deque - methods are append and popleft

""" 

from collections import deque

class Node(object):
    """Node class, to be used in a directed Graph"""

    def __init__(self, data, adjacent=None):
        self.data = data
        adjacent = adjacent or []
        assert isinstance(adjacent, list), "adjacent must be a list!"
        self.adjacent = set(adjacent)

    def __repr__(self):
        return 'Node.data: {}'.format(self.data)

class Graph(object):
    """Graph to contain nodes"""

    def __init__(self):
        """Create an empty graph, we will keep a set of all the nodes"""
        # Can also use a dictionary which maps data to nodes
        self.nodes = set()

    def __repr__(self):
        return 'nodes: {}'.format([n.data for n in self.nodes])

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes.add(node)

    def add_adjacent(self, node, adjacent_nodes):
        """
        If not already added to node, can add to adj set
        """

        for adj in adjacent_nodes:
            node.adjacent.add(adj)

    # def are_connected_DFS(self, node_a, node_b):
    #     """
    #     Returns True if two nodes are connected
    #     Returns False if not connected

    #     Uses DFS (recursion)
    #     """

    #     def _are_connected_DFS(node_a, node_b, seen):

    #         # print '\n',node_a,node_b,'\n'
    #         if node_a.data == node_b.data:
    #             return True

    #         seen.add(node_a)

    #         # print '\n', node_a.adjacent, '\n'
    #         for adj in node_a.adjacent:

    #             if adj in seen:
    #                 continue
    #             # print '\n',adj,node_b,'\n'
    #             if _are_connected_DFS(adj, node_b, seen):
    #                 return True
    #         return False


    #     return _are_connected_DFS(node_a, node_b, set())

    def are_connected_DFS(self, node_a, node_b, seen=None):
        if not seen:
            seen = set()

        if node_a.data == node_b.data:
            return True

        for adj in node_a.adjacent - seen: # set math!
            seen.add(adj)
            if self.are_connected_DFS(adj, node_b, seen):
                return True
        return False

    def are_connected_BFS(self, node_a, node_b):
        """
        Returns True if two nodes are connected
        Returns False if not connected

        Uses BFS (queue)
        """

        queue = deque()
        # print node_a
        queue.append(node_a)
        seen = {node_a}

        while queue:
            curr = queue.popleft()
            if curr.data == node_b.data:
                return True
            # for adj in curr.adjacent:
            #     if adj not in seen:
            for adj in curr.adjacent - seen: #better to use set math!
                seen.add(adj)
                queue.append(adj)
        return False

# Testing - Should Pass

four = Node(4)
five = Node(5)
three = Node(3, [four,five])
two = Node(2, [three])
one = Node(1, [two,three])


directed_graph = Graph()
directed_graph.add_node(one)
directed_graph.add_node(two)
directed_graph.add_node(three)
directed_graph.add_node(four)
directed_graph.add_node(five)

four_b = Node(4)
five_b = Node(5, [four_b])
three_b = Node(3, [four_b])
two_b = Node(2, [three_b])
one_b = Node(1, [two_b,three_b])


directed_graph_b = Graph()
directed_graph_b.add_node(one_b)
directed_graph_b.add_node(two_b)
directed_graph_b.add_node(three_b)
directed_graph_b.add_node(four_b)
directed_graph_b.add_node(five_b)


if directed_graph.are_connected_BFS(one, five):
    print "Test 1 passed"
if not directed_graph_b.are_connected_BFS(one_b, five_b):
    print "Test 2 passed"

if directed_graph.are_connected_DFS(one, five):
    print "Test 3 passed"

if not directed_graph_b.are_connected_DFS(one_b, five_b):
    print "Test 4 passed"





