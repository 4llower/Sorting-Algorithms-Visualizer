def bubbleSorting(view_window):
    for i in range(len(view_window.array)):
        for j in range(i + 1, len(view_window.array)):
            if (view_window.array[i] > view_window.array[j]):
                view_window.view_windowize_swap(i, j)