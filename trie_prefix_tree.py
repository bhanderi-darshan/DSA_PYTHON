# Day 18: Implement Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        current.end_of_word = True

    def search(self, word):
        current = self.root
        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return current.end_of_word

    def starts_with(self, prefix):
        current = self.root
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True

# Test the Trie
trie = Trie()
trie.insert("apple")
trie.insert("app")
trie.insert("banana")

print(trie.search("apple"))   # True
print(trie.search("app"))     # True
print(trie.search("appl"))    # False
print(trie.starts_with("ban")) # True
