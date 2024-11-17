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
        return self._searchDfs(word, 0, self.root)

    def _searchDfs(self, word: str, index: int, node: TrieNode) -> bool:
        if index == len(word):
            return node.is_end_of_word

        ch = word[index]
        if ch == '.':
            for child in node.children.values():
                if self._searchDfs(word, index + 1, child):
                    return True
            return False
        elif ch in node.children:
            return self._searchDfs(word, index + 1, node.children[ch])
        else:
            return False



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)