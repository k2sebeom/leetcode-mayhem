


def backtrack(L, result, sofar):
    if len(sofar) == len(L):
        result.append(sofar.copy())
        return
    
    if len(sofar) == 0:
        for n in L[0]:
            sofar.append(n)
            backtrack(L, result, sofar)
            sofar.pop(-1)
    else:
        depth = len(sofar)
        for n in L[depth]:
            if n & 1 == 0 and sofar[-1] & 1 == 1:
                sofar.append(n)
                backtrack(L, result, sofar)
                sofar.pop(-1)
            if n & 1 == 1 and sofar[-1] & 1 == 0:
                sofar.append(n)
                backtrack(L, result, sofar)
                sofar.pop(-1)


if __name__ == '__main__':
    L = [[1,2,3],[4,5,6],[7,8,9]]
    print(L)
    result = []
    backtrack(L, result, [])
    print(result)