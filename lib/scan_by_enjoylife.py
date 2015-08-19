#implementation of SCAN by user enjoylife from github


from collections import deque
import numpy as np
from scipy.sparse import csr_matrix
 
def struct_similarity(vcols, wcols):
    """ Compute the similartiy normalized on geometric mean of vertices"""
    # count the similar rows for unioning edges
    count = [index for index in wcols if (index in vcols)]
    # geomean
    #need to account for vertex itself, add 2(1 for each vertex)
    ans = (len(count) +2) / (((vcols.size+1)*(wcols.size+1)) ** .5)
    return ans
 
def neighborhood(G, vertex_v, eps):
    """ Returns the neighbors, as well as all the connected vertices """
    N = deque()
    vcols = vertex_v.tocoo().col
    #check the similarity for each connected vertex
    for index in vcols:
        wcols = G[index,:].tocoo().col
        if struct_similarity(vcols, wcols)> eps:
            N.append(index)
    return N, vcols
 
def scan_by_enjoylife_algo(G, eps=0.7, mu=2):
    """
    Vertex Structure = sum of row + itself(1)
    Structural Similarity is the geometric mean of the 2Vertex size of structure
    """
    
    c = 0
    v = G.shape[0]
    # All vertices are labeled as unclassified(-1)
    vertex_labels = -np.ones(v).astype(int)
    # start with a neg core(every new core we incr by 1)
    cluster_id = -1
    for vertex in xrange(v):
        N ,vcols = neighborhood(G, G[vertex,:],eps)
        # must include vertex itself
        N.appendleft(vertex)
        if len(N) >= mu:
            #print "we have a cluster at: %d ,with length %d " % (vertex, len(N))
            # gen a new cluster id (0 indexed)
            cluster_id +=1
            while N:
                 y = N.pop()
                 R , ycols = neighborhood(G, G[y,:], eps)
                 # include itself
                 R.appendleft(y)
                 # (struct reachable) check core and if y is connected to vertex
                 if len(R) >= mu and y in vcols:
                     #print "we have a structure Reachable at: %d ,with length %d " % (y, len(R))
                     while R:
                         r = R.pop()
                         label = vertex_labels[r]
                         # if unclassified or non-member
                         if (label == -1) or (label==0): 
                             vertex_labels[r] =  cluster_id
                         # unclassified ??
                         if label == -1:
                             N.appendleft(r)
        else:
            vertex_labels[vertex] = 0
    if cluster_id  <= 0:
        clusters = []
        labels = xrange(v)
        for i in xrange(v):
            clusters.append(set([i]))
        return [labels, clusters]

    labels = [-1]*v
    new_clusters_id = [-1]*(cluster_id+1)
    new_clusters_id[0] = 0
    index = 1
    for vertex in xrange(v):
        if new_clusters_id[vertex_labels[vertex]] == -1:
            new_clusters_id[vertex_labels[vertex]] = index
            index = index+1
        labels[vertex] = new_clusters_id[vertex_labels[vertex]]

    clusters = [0]*(index-1)
    for i in xrange(1, index):
        clusters[i-1] = set(vertex for vertex in xrange(v) if labels[vertex] == i)

    #classify non-members
    for index in xrange(v):
        if labels[index] == 0:
            ncols= G[index,:].tocoo().col
            if len(ncols) >=2:
                ## mark as a hub
                labels[index] = -2 
                for j in xrange(len(ncols)):
                    if labels[ncols[j]] > 0:
                        clusters[labels[ncols[j]]-1].add(index)
                continue
                
            else:
                ## mark as outlier
                labels[index] = -3
                continue

    return [labels, clusters]