def LSDsorting(Visual, left, right, rate):

    if (left >= right or rate == 0):
        return

    pos = [[] for i in range(11)]

    for i in range(left, right + 1):
        pos[(Visual.array[i] // rate) % 10].append(i)

    point = int(left)

    for i in range(10):
        pos[i] = sorted(pos[i])
        for j in range(len(pos[i])):
            if ((Visual.array[point] // rate) % 10 == i):
                point += 1
                continue
            else:
                pos[(Visual.array[point] // rate) % 10].remove(point)
                pos[(Visual.array[point] // rate) % 10].append(pos[i][j])
                Visual.visualize_swap(point, pos[i][j])
                point += 1

    last = int(left)

    for i in range(left + 1, right + 1):
        if ((Visual.array[i] // rate) % 10 != (Visual.array[i - 1] // rate) % 10):
            LSDsorting(Visual, last, i - 1, rate // 10)
            last = i

    if (last != right):
        LSDsorting(Visual, last, right, rate // 10)
