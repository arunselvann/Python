class CountingSort:
    def __init__(self, data=[]):
        self.data = data

    def sort(self):
        max_value = max(self.data)
        cl = []
        rl = [None]*len(self.data)
        cl += [0 for _ in range(max_value + 1)]
        for i in self.data:
            cl[i] += 1
        for i in range(1,len(cl)):
            cl[i] += cl[i-1]
        for i in reversed(self.data):
            rl[cl[i]-1] = i
            cl[i] -= 1
        return rl

    def sort2(self):
        max_value = max(self.data)
        cl = []
        rl = []
        cl += [0 for _ in range(max_value+1)]
        for i in self.data:
            cl[i] += 1
        for i in range(len(cl)-1,-1,-1):
            if cl[i] != 0:
                rl += [i for _ in range(cl[i])]
        return rl

    def sort3(self):
        max_value = max(self.data)
        min_value = min(self.data)
        cl = []
        rl = [None]*len(self.data)
        cl += [0 for _ in range(min_value,max_value + 1)]
        for i in self.data:
            cl[i-min_value] += 1
        for i in range(1,len(cl)):
            cl[i] += cl[i-1]
        print(cl)
        for i in reversed(self.data):
            rl[cl[i-min_value]-1] = i
            cl[i-min_value] -= 1
        return rl


l = [10,7,0,-2]
print(l)
s = CountingSort(l)
print(s.sort3())

