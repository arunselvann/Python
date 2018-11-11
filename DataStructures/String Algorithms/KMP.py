class KMP:
    def __init__(self, data, pattern):
        self.data = data
        self.pattern = pattern

    def search(self):
        n = len(self.data)
        m = len(self.pattern)
        lps = [0] * m
        i = 0
        j = 0
        self.computeLPSArray(m, lps)
        while i < n:
            if self.pattern[j] == self.data[i]:
                i += 1
                j += 1

            if j == m:
                print(i - j)
                j = lps[j - 1]

            elif i < n and self.pattern[j] != self.data[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

    def computeLPSArray(self, m, lps):
        len = 0
        i = 1
        while i < m:
            if self.pattern[i] == self.pattern[len]:
                len += 1
                lps[i] = len
                i += 1
            else:
                if len != 0:
                    len = lps[len - 1]
                else:
                   lps[i] = 0
                   i += 1

p = KMP('ABCDHGHABCJKL', 'ABC')
p.search()