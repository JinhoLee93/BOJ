def solution(tickets):
    graph = {}
    for t in tickets:
        src, dest = t[0], t[1]
        if src not in graph:
            graph[src] = []
            
        if dest not in graph:
            graph[dest] = []
            
        graph[src].append(dest)
    
    for key in graph:
        graph[key].sort()
    
    res = []
    def backtrack(dest, path):
        nonlocal res
        if not graph[dest]:
            if len(path) == len(tickets) + 1:
                res = path.copy()
                
                return True 
            
            return False
        
        c = graph[dest]
        for i, nei in enumerate(c):
            graph[dest].pop(i)
            path.append(nei)
            if backtrack(nei, path):
                
                return True
            path.pop()
            graph[dest].insert(i, nei)
            
    backtrack("ICN", ["ICN"])
    
    
    return res