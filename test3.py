class Trie:
    CHAR_NUM = 26
    _next_Trie: list['Trie']
    _is_end: bool

    def __init__(self):
        self._next_Trie = [None for _ in range(self.CHAR_NUM)]
        self._is_end = False
    
    def char_order(self, ch: chr) -> int:
        return ord(ch) - ord('a')
    
    def insert(self, word: str) -> None:
        if word == '':
            self._is_end = True
            return
        next_Trie = Trie()
        self._next_Trie[self.char_order(word[0])] = next_Trie
        next_Trie.insert(word[1:])

    def search(self, word: str) -> bool:
        if word == '':
            return self._is_end
        next_Trie = self._next_Trie[self.char_order(word[0])]
        return bool(next_Trie) and next_Trie.search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if prefix == '':
            return True
        next_Trie = self._next_Trie[self.char_order(prefix[0])]
        return bool(next_Trie) and next_Trie.startsWith(prefix[1:])

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

if __name__ == '__main__':
    obj = Trie()
    instr = ["insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
    param = [["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]
    for inst, para in zip(instr, param):
        eval(f'print(obj.{inst}("{para[0]}"))')