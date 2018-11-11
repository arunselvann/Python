class BruteForce:
    def __init__(self, text, pattern):
        self.text = text
        self.pattern = pattern

    def pattern_search(self):
        n = len(self.text)
        m = len(self.pattern)
        for i in range(n-m+1):
            j = 0
            while j < m and self.text[i+j] == self.pattern[j]:
                j += 1
            if j == m:
                return i
        return -1


p = BruteForce('abcdefghijk', 'gi')
print(p.pattern_search())