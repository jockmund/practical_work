class BinarySearch(object):
    def __init__(self, n, array):
        self.n = n
        self.array = array

    def binary_search(self, x):
        left = -1
        right = len(self.array)

        while right > left + 1:
            middle = (left + right) // 2
            if self.array[middle] >= x:
                right = middle
            else:
                left = middle

        if self.array[right] == x:
            return right
        else:
            return -1
