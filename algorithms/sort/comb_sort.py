"""

https://en.wikipedia.org/wiki/Comb_sort

Worst-case performance: O(N^2)

"""


def comb_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    gap = n
    shrink = 1.3
    done = False
    while not done:
        gap = int(gap / shrink)
        if gap > 1:
            done = False
        else:
            gap = 1
            done = True

        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                swap(i, i + gap)
                done = False
            i = i + 1
    return arr
