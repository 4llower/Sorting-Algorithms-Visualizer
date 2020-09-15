def mergeSorting(view_window, left, right):

    if (left == right):
        return

    middle = (left + right) // 2

    mergeSorting(view_window, left, middle)
    mergeSorting(view_window, middle + 1, right)


    pos_left = left
    pos_right = middle + 1

    extra_array = []

    while (1):

        if (pos_left > middle and pos_right > right): break

        if (pos_left > middle):
            extra_array.append(view_window.array[pos_right])
            pos_right += 1
            continue

        if (pos_right > right):
            extra_array.append(view_window.array[pos_left])
            pos_left += 1
            continue

        if (view_window.array[pos_left] < view_window.array[pos_right]):
            extra_array.append(view_window.array[pos_left])
            pos_left += 1
        else:
            extra_array.append(view_window.array[pos_right])
            pos_right += 1

    pos = 0

    for i in range(left, right + 1):

        if (view_window.array[i] == extra_array[pos]):
            pos += 1
            continue

        for j in range(i + 1, right + 1):
            if (view_window.array[j] == extra_array[pos]):
                view_window.view_windowize_swap(i, j)
                pos += 1
                break
