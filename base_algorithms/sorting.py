import random


def bubble_sort(L): # O(n^2)
    for _ in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]


if __name__ == "__main__":
    A = []
    B = []
    for _ in range(10):
        n = random.randint(0, 100)
        A.append(n)
        B.append(n)
    
    bubble_sort(A)
    B.sort()
    print(A)
    print(B)

    
