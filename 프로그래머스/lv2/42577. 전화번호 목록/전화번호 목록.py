def solution(phone_book):
    visited = set()
    phone_book.sort(key=lambda x:len(x))
    for num in phone_book:
        for i in range(1, len(num) + 1):
            compare = num[:i]
            if compare in visited:
                
                return False
        visited.add(num)
    
    return True