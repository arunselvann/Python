class RadixSort:
    def __init__(self, data=[]):
        self.data = data

    def countingSort(self, d):
        n = len(self.data)
        cl = [0] * 11
        rl = [0] * n
        for i in self.data:
            index = i//d
            cl[index % 10] += 1
        for i in range(1, 10):
            cl[i] += cl[i-1]
        for i in reversed(self.data):
            index = i // d
            rl[cl[index % 10] -1 ] = i
            cl[index % 10] -= 1
        return rl

    def sort(self):
        max_value = max(self.data)
        digit = 1
        while max_value//digit > 0:
            self.data = self.countingSort(digit)
            digit *= 10
        return self.data


l = [20, 10, 100, 5]
print(l)
s = RadixSort(l)
print(s.sort())