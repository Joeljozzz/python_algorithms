#####bfs
graph = {
    'A': set(['C','B']),
    'B': set(['A','E','D']),
    'C': set(['A','F']),
    'D': set(['B']),
    'E': set(['B','F']),
    'F': set(['C','E'])
    }
#####logic of bfs
##def bfs(start):
##    queue = [start]
##    levels = {}
##    levels[start]=0
##    visited= set(start)
##    while queue:
##        node = queue.pop(0)
##        neighbours = graph[node]
##        for n in neighbours:
##            if n not in visited:
##                queue.append(n)
##                visited.add(n)
##                levels[n]= levels[node]+1
##    print(levels)
##    return(visited)
##
##print(str(bfs('A'))) 
##                
##
##def bfs_path(graph,start,goal):
##    queue=[(start,[start])]
##    while queue:
##        (vertex,path)= queue.pop(0)
##        for next in graph[vertex]-set(path):
##            if next == goal:
##                yield path + [next]
##            else:
##                queue.append((next,path+[next]))
##
##result =list(bfs_path(graph,'A','F'))
##print(result)
##
##
##def srt_path(graph,start,goal):
##    try:
##        return(next(bfs_path(graph,start,goal)))
##    except:
##        StopIteration
##        return None
##res1=srt_path(graph,'A','F')
##print(res1)


def bfs(start):
    queue = [start]
    levels={}
    visited= set(start)
    levels[start]=0
    while queue:
        node=queue.pop(0)
        neighbours= graph[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                levels[neighbour]=levels[node]+1
    print(levels)
    return visited
res=bfs('A')
print(str(res))


def bfs_path(graph,start,goal):
    queue=[(start,[start])]
    while queue:
        (vertex,path)= queue.pop(0)
        for next in graph[vertex]-set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next,path+[next]))

result =list(bfs_path(graph,'A','F'))
print(result)


def srt_path(graph,start,goal):
    try:
        return(next(bfs_path(graph,start,goal)))
    except:
        StopIteration
        return None
res1=srt_path(graph,'A','F')
print(res1)


































































    
