def bubbleSorting(Visual):
    for i in range(len(Visual.array)):
        for j in range(i + 1, len(Visual.array)):
            if (Visual.array[i] > Visual.array[j]):
                Visual.visualize_swap(i, j)