class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self._searchPrefix(word)
        return node.is_end_of_word if node else False

    def startsWith(self, prefix: str) -> bool:
        node = self._searchPrefix(prefix)
        return True if node else False

    def _searchPrefix(self, prefix: str):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return node




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)