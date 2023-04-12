def solution(participant, completion):
    c = {}
    for com in completion:
        c[com] = c.get(com, 0) + 1
    
    for p in participant:
        if p in c:
            c[p] -= 1
            if c[p] < 0:
                return p
        else:
            return p
        