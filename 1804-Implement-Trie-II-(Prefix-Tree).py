class TrieNode:
    def __init__(self):
        self.links = {}
        self.ends = 0
        self.starts = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Helper function to traverse the Trie
    def _traverse(self, string: str) -> TrieNode:
        node = self.root
        for w in string:
            if w not in node.links:
                return None
            node = node.links[w]
        return node

    def insert(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.links:
                node.links[w] = TrieNode()
            node = node.links[w]
            node.starts += 1
        node.ends += 1

    def countWordsEqualTo(self, word: str) -> int:
        node = self._traverse(word)
        if not node:
            return 0
        return node.ends

    def countWordsStartingWith(self, prefix: str) -> int:
        node = self._traverse(prefix)
        if not node:
            return 0
        return node.starts

    def erase(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.links[w]
            node.starts -= 1
        node.ends -= 1
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)