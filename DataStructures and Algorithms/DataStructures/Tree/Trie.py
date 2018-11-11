class Node:
    def __init__(self):
        self.children = [None] * 256
        self.isEndOfTheWord = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, key):
        cur_node = self.root
        l = len(key)
        for i in range(l):
            index = ord(key[i])
            if not cur_node.children[index]:
                cur_node.children[index] = Node()
            cur_node = cur_node.children[index]
        cur_node.isEndOfTheWord = True

    def search(self, key):
        cur_node = self.root
        l = len(key)
        for i in range(l):
            index = ord(key[i])
            if not cur_node.children[index]:
                return False
            cur_node = cur_node.children[index]
        return cur_node.isEndOfTheWord

    def search_pat(self, key):
        cur_node = self.root
        l = len(key)
        for i in range(l):
            index = ord(key[i])
            if not cur_node.children[index]:
                return False
            cur_node = cur_node.children[index]
        return True


t = Trie()
t.insert('ARUNs')
t.insert('ARUNS')
print(t.search('ARUNs'))
print(t.search_pat('ARUNSE'))