
'''
Backtracking often comes with
def backtrack(arg, result, sofar):
    if problem is complete:
        result.append(sofar)
        return
    
    if beginning: (or sofar == empty)
        go thru all the possible starts
    else:
        search
'''

# Given 3x3 matrix, select 3 elements without duplicate rows or columns 
# What is the minimum score?


# Backtrack finds all possible scores
def backtrack(L, result, sofar):
    if len(sofar) == 3:
        result.append(sum([L[r][c] for r, c in enumerate(sofar)]))
        return

    for c in range(3):
        if c not in sofar:
            sofar.append(c)
            backtrack(L, result, sofar)
            sofar.pop(-1)


if __name__ == '__main__':
    L = [[1,5,3],[2, 4, 7],[5, 3, 5]]
    print(L)
    result = []
    backtrack(L, result, [])
    print(min(result))