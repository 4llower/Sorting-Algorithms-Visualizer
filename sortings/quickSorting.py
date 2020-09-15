def quickSorting(view_window, left, right):
    if (left >= right):
        return

    middle = view_window.array[(left + right) // 2]

    pos_left = left
    pos_right = right

    while (pos_left <= pos_right):

        while (view_window.array[pos_left] < middle):
            pos_left += 1

        while (view_window.array[pos_right] > middle):
            pos_right -= 1

        if (pos_left >= pos_right):
            break

        view_window.view_windowize_swap(pos_left, pos_right)
        pos_left += 1
        pos_right -= 1

    quickSorting(view_window, left, pos_right)
    quickSorting(view_window, pos_right + 1, right)