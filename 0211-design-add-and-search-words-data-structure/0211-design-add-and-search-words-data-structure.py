class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        return self._searchWord(word, 0, self.root)

    def _searchWord(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end_of_word

        c = word[index]
        if c == '.':
            # Try all children nodes for the next character
            return any(self._searchWord(word, index + 1, child) for child in node.children.values())
        elif c in node.children:
            # Proceed to the specific child node
            return self._searchWord(word, index + 1, node.children[c])
        else:
            return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)