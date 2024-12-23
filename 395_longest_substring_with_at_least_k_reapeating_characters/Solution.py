from collections import defaultdict

from collections import defaultdict

class Solution:
    def divideString(self, substring: str, k: int) -> int:
      if len(substring) < k:
        return 0
      
      frequency = defaultdict(int)
      for character in substring:
        frequency[character] += 1
      
      for i in range(len(substring)):
        if frequency[substring[i]] < k:
          new_start = i + 1
          while new_start < len(substring) and frequency[substring[new_start]] < k:
            new_start += 1
          return max(self.divideString(substring[:i], k),
                     self.divideString(substring[new_start:], k))
        
      return len(substring)
  
    def longestSubstring(self, s: str, k: int) -> int:
      return self.divideString(s, k)
        
      
    