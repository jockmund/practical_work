class LinearSearch(object):
    def __init__(self, n, array):
        self.n = n
        self.array = array

    def linear_search(self, x):
        for i in range(self.n):
            if self.array[i] == x:
                return i
        return -1
        # i = 0
        # while i < len(self.array) and self.array[i] != x:
        #     i += 1
        # if i < len(self.array):
        #     return i
        # else:
        #     return -1

