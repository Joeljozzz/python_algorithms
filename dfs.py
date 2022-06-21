# graph1 = {
#
##      'A': set (['B','C']),
##      'B': set (['A','D', 'E']),
##      'C': set(['A','F']),
##      'D': set (['B']),
##      'E': set(['B','F']),
##      'F': set(['C','E'])
#     }
#
# def dfs(graph,node,visited):
#     if node not in visited:
#         visited.append(node)
#         for n in graph[node]:
#             dfs(graph, n, visited)
#     return visited
# visited=dfs(graph1,'A',[])
# print(visited)
##graph1 ={
## 'A': set(['B','C']),
## 'B': set(['A','C', 'D']),
## 'C': set(['B','A']),
## 'D': set(['E']),
## 'E': set(['D'])
##}
##
##def dfs(graph, node, visited):
##    if node not in visited:
##           visited.append(node)
##           for n in graph[node]:
##              dfs(graph,n,visited)
##    return visited
##
##vs = dfs(graph1,'A',[])
##print(vs)


##graph1={
##    'A': set(['B','C']),
##    'B': set(['A','D','E']),
##    'C': set(['A','F']),
##    'D': set(['B']),
##    'E': set(['B','F']),
##    'F': set(['C','E'])
##    }
##
##def dfs(graph,node,visited):
##    if node not in visited:
##        visited.append(node)
##        for n in graph[node]:
##            dfs(graph,n,visited)
##    return visited
##res=dfs(graph1,'A',[])
##print(res)


graph1={
    
  'A': set(['C','B']),
  'B': set(['A','E','D']),
  'C': set(['A','F']),
  'D': set(['B']),
  'E': set(['F', 'B']),
  'F': set(['C','E'])
    }
def dfs(graph,node,visited):
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
          dfs(graph,n,visited)
    return visited
a=dfs(graph1,'A',[])
print(a)































































