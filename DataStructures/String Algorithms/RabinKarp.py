class RabinKarp:
    def __init__(self, data, pattern):
        self.data = data
        self.pattern = pattern
        self.q = 101
        self.d = 256

    def search(self):
        n = len(self.data)
        m = len(self.pattern)
        h = pow(self.d, m-1) % self.q
        t = 0
        p = 0
        for i in range(m):
            t = (self.d * t + ord(self.data[i])) % self.q
            p = (self.d * p + ord(self.pattern[i])) % self.q
        for i in range(n-m+1):
            if p == t:
                for j in range(m):
                    if self.data[i+j] != self.pattern[j]:
                        break
                if j == m-1:
                    print(i)
            if i < n-m:
                t = (self.d*(t-(ord(self.data[i])*h)) + ord(self.data[i+m])) % self.q


p = RabinKarp('Arunselvan Natesan', 'van')
p.search()