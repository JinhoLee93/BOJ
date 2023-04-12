def solution(clothes):
    combs = {}
    for c in clothes:
        combs[c[1]] = combs.get(c[1], [])
        combs[c[1]].append(c[0])
    
    res = 1
    for key in combs:
        l = len(combs[key])
        res *= (l + 1)
        
    return res - 1