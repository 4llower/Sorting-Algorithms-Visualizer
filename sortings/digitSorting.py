def LSDsorting(view_window, left, right, rate):

    if (left >= right or rate == 0):
        return

    pos = [[] for i in range(11)]

    for i in range(left, right + 1):
        pos[(view_window.array[i] // rate) % 10].append(i)

    point = int(left)

    for i in range(10):
        pos[i] = sorted(pos[i])
        for j in range(len(pos[i])):
            if ((view_window.array[point] // rate) % 10 == i):
                point += 1
                continue
            else:
                pos[(view_window.array[point] // rate) % 10].remove(point)
                pos[(view_window.array[point] // rate) % 10].append(pos[i][j])
                view_window.view_windowize_swap(point, pos[i][j])
                point += 1

    last = int(left)

    for i in range(left + 1, right + 1):
        if ((view_window.array[i] // rate) % 10 != (view_window.array[i - 1] // rate) % 10):
            LSDsorting(view_window, last, i - 1, rate // 10)
            last = i

    if (last != right):
        LSDsorting(view_window, last, right, rate // 10)
