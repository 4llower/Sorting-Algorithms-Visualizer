def countSorting(Visual):
    count = [0 for i in range(max(Visual.array) + 1)]
    for i in range(len(Visual.array)):
        count[Visual.array[i]] = i
    pos = 0
    for i in range(1, max(Visual.array)):
        if Visual.array[pos] == i:
            pos += 1
            continue
        posA = count[Visual.array[pos]]
        posB = count[i]
        count[Visual.array[pos]], count[i] = count[i], count[Visual.array[pos]]
        Visual.visualize_swap(posA, posB)
        pos += 1