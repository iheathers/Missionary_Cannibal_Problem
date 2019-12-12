from time import time
from bfs_algorithm import bfs
from dfs_algorithm import dfs
from node import Node

initial_state= [3,3,1]

Node.num_of_instances=0
t0=time()
solution=bfs(initial_state)
t1=time()-t0
print('BFS Solution:', solution)
print('Space:',Node.num_of_instances)
print('Time for BFS :',t1,'seconds')

t2=time()
solution=dfs(initial_state)
t3=time()-t2
print('DFS Solution:', solution)
print('Space:',Node.num_of_instances)
print('Time for DFS:',t3,'seconds')

print("THE TIME TAKEN BY DFS IS {} and BFS is {} ".format(t3,t1))
