class LinearSearch(object):
    def __init__(self, n, array):
        self.n = n
        self.array = array

    def linear_search(self, x):
        for i in range(self.n):
            if self.array[i] == x:
                return i
        return -1

