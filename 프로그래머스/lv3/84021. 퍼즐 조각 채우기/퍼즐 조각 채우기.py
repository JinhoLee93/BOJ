def solution(game_board, table):
    N, M = len(game_board), len(table)
    def dfs(board, r, c, d, num, total, is_it_table):                
        if r < 0 or c < 0 or r >= total or c >= total or \
            (r, c) in visited:
            
            return
        
        if is_it_table:
            if board[r][c] == 0:
                
                return
        else:
            if board[r][c] == 1:
                
                return
        
        visited.add((r, c))
        d[num].append((r, c))
        dfs(board, r + 1, c, d, num, total, is_it_table)
        dfs(board, r - 1, c, d, num, total, is_it_table)
        dfs(board, r, c + 1, d, num, total, is_it_table)
        dfs(board, r, c - 1, d, num, total, is_it_table)
    
    def check_if_they_fit(full_block, free_block):
        def turn(full):
            R, C = len(full), len(full[0])
            clone = [[] for _ in range(C)]
            for r in range(R - 1, -1, -1):
                for c in range(C):
                    clone[c].append(full[r][c])
            
            return clone
            
        min_row, min_col = M, M
        for (r, c) in full_block:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
        
        max_row, max_col = -1, -1
        for i in range(len(full_block)):
            new_block = (full_block[i][0] - min_row, full_block[i][1] - min_col)
            full_block[i] = new_block
            max_row = max(max_row, full_block[i][0])
            max_col = max(max_col, full_block[i][1])
        
        full = [[0] * (max_col + 1) for _ in range(max_row + 1)]
        for (r, c) in full_block:
            full[r][c] = 1
        
        min_row, min_col = N, N
        for (r, c) in free_block:
            min_row = min(min_row, r)
            min_col = min(min_col, c)
        
        max_row, max_col = -1, -1
        for i in range(len(free_block)):
            new_block = (free_block[i][0] - min_row, free_block[i][1] - min_col)
            free_block[i] = new_block
            max_row = max(max_row, free_block[i][0])
            max_col = max(max_col, free_block[i][1])
            
        free = [[0] * (max_col + 1) for _ in range(max_row + 1)]
        for (r, c) in free_block:
            free[r][c] = 1
        
        for _ in range(4):
            full = turn(full)
            if full == free:
                
                return True
        
        return False
    
    res = 0
    blocks, t, visited = {}, 0, set()
    for r in range(M):
        for c in range(M):  
            if table[r][c] == 1 and (r, c) not in visited:
                blocks[t] = []
                dfs(table, r, c, blocks, t, M, True)
                t += 1
    
    blocks_to_fill = sorted(list(blocks.values()), key=lambda x:-len(x))
    
    empty, t, visited = {}, 0, set()
    for r in range(N):
        for c in range(N):
            if game_board[r][c] == 0 and (r, c) not in visited:
                empty[t] = []
                dfs(game_board, r, c, empty, t, N, False)
                t += 1
    
    free_blocks = sorted(list(empty.values()), key=lambda x:-len(x))
    
    filled = set()
    for i in range(len(blocks_to_fill)):
        full_block = blocks_to_fill[i]
        for j in range(len(free_blocks)):
            if j in filled:
                continue
            free_block = free_blocks[j]
            if len(full_block) > len(free_block):
                break
            elif len(full_block) < len(free_block):
                continue
            else:
                if check_if_they_fit(full_block, free_block):
                    filled.add(j)
                    res += len(full_block)
                    break
    
    return res