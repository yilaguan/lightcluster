#computes if graph is fully connected

from load_data import download_data as dd
n, edges = dd('protein.txt')
was = [0]*n

#depth-first search
def dfs(x):
  print x
  was[x] = 1
  for i in range(len(edges)):
    if (edges[i][0] == x and was[edges[i][1]] == 0):
      dfs(edges[i][1])
    if (edges[i][1] == x and was[edges[i][0]] == 0):
      dfs(edges[i][0])
  return

#launching dfs
dfs(0)

#checking if all nodes in one connected component
for i in range(n):
  if was[i] == 0
    print 'not fully connected'
  else
    print 'fully connected'
