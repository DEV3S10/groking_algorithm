def fast_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return fast_sort(less) + [pivot] + fast_sort(greater)


print(fast_sort([10, 5, 2, 3]))
