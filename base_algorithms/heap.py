from heapq import heapify, heappop, heappush


if __name__ == "__main__":
    q = [1, 5, 4, 6, 2, 3]
    heapify(q) # O(n)
    print(q)
    heappush(q, 15) # O(log n)
    print(q)

    while len(q) > 0:
        print(heappop(q)) # O(log n)

