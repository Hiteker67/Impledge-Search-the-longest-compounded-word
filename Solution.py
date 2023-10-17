import Trie as T
from collections import deque
import time

class Solution:
    def __init__(self) -> None:
      self.trie = T.Trie()
      self.queue = deque()

    def buildTrie(self,filePath : str = None) -> None:
        
        try:
            with open(filePath, mode = 'r') as f:
                for line in f:
                    word = line.rstrip('\n')
                    prefixes = self.trie.getPrefixes(word)
                    for prefix in prefixes:
                        self.queue.append((word, word[len(prefix):]))
                    self.trie.insert(word)
        except:
            print("There was some error with the file!")
            exit(0)
    
    def findLongestCompoundWords(self) -> tuple:
        
        longest_word = ''
        longest_length = 0
        second_longest = ''
        
        while self.queue:
            
            word, suffix = self.queue.popleft()
            
            if suffix in self.trie and len(word) > longest_length:
                second_longest = longest_word
                longest_word = word
                longest_length = len(word)
            else:
                prefixes = self.trie.getPrefixes(suffix)
                for prefix in prefixes:
                    self.queue.append((word, suffix[len(prefix):]))

        return (longest_word,second_longest)

if __name__ == "__main__":
    sol = Solution()
    start = time.time()
    sol.buildTrie("Input_02.txt")
    first,second = sol.findLongestCompoundWords()
    end = time.time()
    print("Longest Compound Word:",first)
    print("Second Longest Compound Word:",second)
    print("Time taken: ",str(end - start), "seconds")