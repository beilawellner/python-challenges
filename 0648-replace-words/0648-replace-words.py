class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True

    def serch_for_prefix(self, word):
        node = self.root
        res = ''
        for c in word:
            if node.is_word:
                return res
            if c not in node.children:
                return ''
            res += c
            node = node.children[c]
        return word if node.is_word else ''


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.add_word(word)
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            new_word = trie.serch_for_prefix(word)
            sentence[i] = new_word if new_word else word
        return " ".join(sentence)
