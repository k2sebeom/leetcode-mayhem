

def interval_schedule():
    intervals = [
        (1, 3), (2, 5), (3, 9), (6, 8)
    ]

    intervals.sort(key=lambda i: i[1])

    result = [intervals.pop(0)]

    for i in intervals:
        if i[0] > result[-1][1]:
            result.append(i)
    print(result)




if __name__ == '__main__':
    interval_schedule()
