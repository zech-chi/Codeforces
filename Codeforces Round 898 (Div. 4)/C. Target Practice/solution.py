size = int(input(""))
res = []
for _ in range(size):
    matrix = []
    for _ in range(10):
        matrix.append(input(""))
    
    Sum = 0
    for n in range(5):
        r = n
        for c in range(n, 10 - n):
            if matrix[r][c] == 'X':
                Sum += n + 1
        
        c = n
        for r in range(n + 1, 10 - n):
            if matrix[r][c] == 'X':
                Sum += n + 1
                
        r = 9 - n
        for c in range(n + 1, 10 - n):
            if matrix[r][c] == 'X':
                Sum += n + 1
        
        c = 9 - n
        for r in range(n + 1, 10 - n - 1):
            if matrix[r][c] == 'X':
                Sum += n + 1
        
    res.append(Sum)
 
for s in res:
    print(s)
