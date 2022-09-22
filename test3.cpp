#include <iostream>
#include <string>
#include <deque>

using string = std::string;

class Trie {
  private:
    constexpr static int CHAR_NUM = 26;
    Trie* links[CHAR_NUM];
    bool isEnd;
    Trie* searchPrefix(string word) {
      Trie* node = this;
      for (char ch: word) {
        if (node.containsKey(ch)) {
          node = node.get(ch);
        } else {
          return nullptr;
        }
      }
      return node;
    }
  public:
    bool containsKey(char ch) {
      return links[ch - 'a'] != nullptr;
    }
    void put(char ch, Trie* node) {
      links[ch - 'a'] = node;
    }
    void setEnd() {
      isEnd = true;
    }
    void insert(string word) {
      Trie* node = this;
      for (char ch: word) {
        if (!node.containsKey(ch)) {
          node.put(ch, new Trie());
        }
        node = node.get(ch);
      }
      node.setEnd();
    }
    bool search(string word) {
      Trie* node = searchPrefix(word);
      return node != nullptr && node.isEnd();
    }
    bool startsWith(string word) {
      Trie* node = searchPrefix(word);
      return node != nullptr;
    }
    ~Trie() {
      std::deque<Trie*> stack;

    }
};

int main() {
  Trie t;
  return 0;
}