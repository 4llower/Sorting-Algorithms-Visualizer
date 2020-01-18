def quickSorting(Visual, left, right):
    if (left >= right):
        return

    middle = Visual.array[(left + right) // 2]

    pos_left = left
    pos_right = right

    while (pos_left <= pos_right):

        while (Visual.array[pos_left] < middle):
            pos_left += 1

        while (Visual.array[pos_right] > middle):
            pos_right -= 1

        if (pos_left >= pos_right):
            break

        Visual.visualize_swap(pos_left, pos_right)
        pos_left += 1
        pos_right -= 1

    quickSorting(Visual, left, pos_right)
    quickSorting(Visual, pos_right + 1, right)