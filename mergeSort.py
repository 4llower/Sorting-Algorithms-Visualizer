def mergeSorting(array, left, right):

    if (left == right):
        return

    middle = (left + right) // 2

    mergeSorting(array, left, middle)
    mergeSorting(array, middle + 1, right)


    pos_left = left
    pos_right = middle + 1

    extra_array = []

    while (1):

        if (pos_left > middle and pos_right > right): break

        if (pos_left > middle):
            extra_array.append(array[pos_right])
            pos_right += 1
            continue

        if (pos_right > right):
            extra_array.append(array[pos_left])
            pos_left += 1
            continue

        if (array[pos_left] < array[pos_right]):
            extra_array.append(array[pos_left])
            pos_left += 1
        else:
            extra_array.append(array[pos_right])
            pos_right += 1


    for i in range(left, right + 1):
        array[i] = extra_array[i - left]