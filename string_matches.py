# 1408. String Matching in an Array
# Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
 

# Constraints:

# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.

class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
      substrings = []
      for palabra in words:
        for palabraDos in words:
          if palabra != palabraDos:
            if palabra in palabraDos and palabra not in substrings:
              substrings.append(palabra)
      return substrings
    
    

solucion = Solution()

primerEjemplo = ['mass', 'as','hero','superhero']
print(solucion.stringMatching(primerEjemplo))
segundoEjemplo = ['leetcode','et','code']
print(solucion.stringMatching(segundoEjemplo))
tercerEjemplo = ['blue','green','bu']
print(solucion.stringMatching(tercerEjemplo))
    
  