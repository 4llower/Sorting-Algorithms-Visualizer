def countSorting(view_window):
    count = [0 for i in range(max(view_window.array) + 1)]
    for i in range(len(view_window.array)):
        count[view_window.array[i]] = i
    pos = 0
    for i in range(1, max(view_window.array)):
        if view_window.array[pos] == i:
            pos += 1
            continue
        posA = count[view_window.array[pos]]
        posB = count[i]
        count[view_window.array[pos]], count[i] = count[i], count[view_window.array[pos]]
        view_window.view_windowize_swap(posA, posB)
        pos += 1