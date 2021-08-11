from functools import partial

from Graph import Graph
from Vertex import Vertex
from search import breadth_first_search, depth_first_search, a_star_search, heuristic, cost


if __name__ == "__main__":
  a = Vertex('a')
  b = Vertex('b')
  c = Vertex('ç')
  d = Vertex('d')
  e = Vertex('e')

  g = Graph()
  g.addVertex(a)
  g.addVertex(b)
  g.addVertex(c)
  g.addVertex(d)
  g.addVertex(e)
  g.addDirectedEdge(a, c)
  g.addDirectedEdge(a, d)
  g.addDirectedEdge(a, b)
  g.addDirectedEdge(c, d)
  g.addDirectedEdge(b, d)
  g.addDirectedEdge(d, e)
  g.addDirectedEdge(b, e)

  path_d = depth_first_search(g.vertices[-1], g)
  print(list(map(lambda n: n.value, path_d)))
  path_b = breadth_first_search(g.vertices[-1], g)
  print(list(map(lambda n: n.value, path_b)))
#   path_vals = list(map(lambda n: n.value, path))
#   print(path_vals)

#   h = heuristic("Mombasa")
#   nr_dists = cost("Nairobi")


#   nrb_dists = cost("Nairobi")
#   print(nrb_dists("Kisumu"))
#   print(nrb_dists("Kisumu"))

  # levels = BFS(g.vertices[0], g)
  # for i in range(len(levels)):
  #   print("Level", i, ":")
  #   for j in levels[i]:
  #       print("\t", j)
