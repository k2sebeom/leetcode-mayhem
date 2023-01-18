

# Generate all subsets of the given set
def all_subsets(L):
    if len(L) == 0:
        return [[]]
    elif len(L) == 1:
        return [[], L]
    
    subset = all_subsets(L[1:])
    subset2 = [[L[0]] + s for s in subset]
    return subset + subset2

# Generate all permutations
def all_perm(L):
    if len(L) <= 1:
        return [L]
    
    result = []
    perms = all_perm(L[1:])
    s = L[0]
    for p in perms:
        for i in range(len(p) + 1):
            result.append(p[:i] + s + p[i:])
    return result


if __name__ == "__main__":
    print(all_subsets([1, 2, 3,4 ,5]))
    print(all_perm('absd'))