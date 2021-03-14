class BinarySearch(object):
    def __init__(self, n, array):
        self.n = n
        self.array = array

    def binary_search(self, x):
        left = 1
        right = len(self.array)

        while right > left:
            middle = (left + right) // 2
            if self.array[middle] >= x:
                right = middle
            else:
                left = middle + 1

        if self.array[left] == x:
            return left
        else:
            return -1
