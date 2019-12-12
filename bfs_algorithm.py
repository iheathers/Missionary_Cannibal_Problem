# Done by Aakash Giree (20)

from queue import Queue
from node import Node, draw_legend
import pydot
import numpy as np
from collections import deque


def bfs(initial_state,mode="bfs"):
    graph = pydot.Dot(graph_type='digraph',label="Missionaries and Cannibals (BFS) - Aakash Giree(20) ",fontsize="30", color="red",
                                                    fontcolor="black",fontname='Impact', fillcolor="black")
    start_node = Node(initial_state, None, None,0)
    if start_node.goal_test():
        return start_node.find_solution()

    q = Queue()
    q.put(start_node)
    explored=[]
    killed=[]
    print("The starting node is \ndepth=%d" % start_node.depth)
    print(str(start_node.state))
    while not(q.empty()):
        node=q.get()
        print("\nthe node selected to expand is\ndepth="+str(node.depth)+"\n"+str(node.state)+"\n")
        explored.append(node.state)
        graph.add_node(node.graph_node)
        if node.parent:
            diff=np.subtract(node.parent.state,node.state)
            if node.parent.state[2]==0:
                diff[0],diff[1]=-diff[0],-diff[1]
            graph.add_edge(pydot.Edge(node.parent.graph_node, node.graph_node,label=str(diff)))
        children=node.generate_child()
        if not node.is_killed():
            print("the children nodes of this node are",end="")
            for child in children:
                if child.state not in explored:
                    print("\ndepth=%d" % child.depth)
                    print(str(child.state))
                    if child.goal_test():
                        print("which is the goal state\n")
                        graph.add_node(child.graph_node)
                        diff = np.subtract(node.parent.state, node.state)
                        if node.parent.state[2] == 0:
                            diff[0], diff[1] = -diff[0], -diff[1]

                        graph.add_edge(pydot.Edge(child.parent.graph_node, child.graph_node,label=str(diff)))

                        # colour all leaves blue
                        leafs = {n.get_name(): True for n in graph.get_nodes()}
                        for e in graph.get_edge_list():
                            leafs[e.get_source()] = False
                        for leaf in leafs:
                            if leafs[leaf] and str(leaf) not in killed and str(leaf)!="\"[0, 0, 0]\"":
                                node = pydot.Node(leaf, style="filled", fillcolor="blue")
                                graph.add_node(node)

                        draw_legend(graph)
                        graph.write_png('BFS_search_tree.png')

                        return child.find_solution()
                    if child.is_valid():
                        q.put(child)
                        explored.append(child.state)

        else:
            print("This node is killed")
            killed.append("\""+str(node.state)+"\"")

    return

