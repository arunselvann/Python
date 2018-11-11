class HashMap:
    def __init__(self):
        self.map = [None] * 10

    def getHash(self, key):
        hash = 0
        for i in key:
            hash += ord(i)
        return hash % len(self.map)

    def add(self, key, value):
        hash = self.getHash(key)
        key_value = [key, value]
        if self.map[hash] is None:
            self.map[hash] = list([key_value])
        else:
            for i in self.map[hash]:
                if i[0] == key:
                    i[1] = value
                    return True
            self.map[hash].append(key_value)
            return True

    def get(self, key):
        hash = self.getHash(key)
        if self.map[hash]:
            for i in self.map[hash]:
                if i[0] == key:
                    return i[1]

    def delete(self,key):
        hash = self.getHash(key)
        if self.map[hash]:
            for i in range(len(self.map[hash])):
                if self.map[hash][i][0] == key:
                    self.map[hash].pop(i)
                    return True
        else:
            return False

    def print(self):
        for i in self.map:
            if i:
                print(str(i))


h = HashMap()
h.add('Bob', '567-8888')
h.add('Ming', '293-6753')
h.add('Ming', '333-8233')
h.add('Ankit', '293-8625')
h.add('Aditya', '852-6551')
h.add('Alicia', '632-4123')
h.add('Mike', '567-2188')
h.add('Aditya', '777-8888')
h.print()
h.delete('Bob')
h.print()
print('Ming: ' + h.get('Ming'))
h.print()