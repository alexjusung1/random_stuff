from os import path

FILENAME = 'words_alpha.txt'

class Trie:
    __slots__ = ('CHAR_NUM', 'link', 'is_end')
    CHAR_NUM: int
    link: list['None | Trie']
    is_end: bool

    def __init__(self):
        self.CHAR_NUM = 26
        self.link = [None for _ in range(self.CHAR_NUM)]
        self.is_end = False

    def char_index(self, char: str) -> int:
        return ord(char) - ord('a')
    
    def get_next(self, char: str) -> 'None | Trie':
        return self.link[self.char_index(char)]
    
    def add_next(self, char: str, trie: 'Trie'):
        self.link[self.char_index(char)] = trie
    
    def insert(self, word: str):
        word = word.lower()
        cur_trie = self
        for char in word:
            if cur_trie.get_next(char) is None:
                t = Trie()
                cur_trie.add_next(char, t)
            cur_trie = cur_trie.get_next(char)
        cur_trie.is_end = True
    
    def _search_prefix(self, word: str) -> 'None | Trie':
        cur_trie = self
        for char in word:
            if not cur_trie.get_next(char):
                return None
            cur_trie = cur_trie.get_next(char)
        return cur_trie
    
    def search(self, word: str) -> bool:
        word = word.lower()
        result = self._search_prefix(word)
        return result is not None and result.is_end

    def begins_with(self, word: str) -> bool:
        word = word.lower()
        result = self._search_prefix(word)
        return result is not None

txt_file = path.join(path.dirname(__file__), FILENAME)

with open(txt_file, 'r') as f:
    t = Trie()
    for word in f.read().splitlines():
        t.insert(word)
    