from collections import defaultdict

class Solution:
  def divideString(self, substring: str, k: int) -> int:
    # Se a substring for menor que k, não é possível dividir
    if len(substring) < k:
      return 0
    
    # Conta a frequência de cada caractere na substring
    frequency = defaultdict(int)
    for character in substring:
      frequency[character] += 1
    
    # Se todos os caracteres da substring aparecem pelo menos k vezes, a substring é válida
    # Caso contrário, divide a substring em partes menores
    # A resposta é o máximo entre as divisões
    for i in range(len(substring)):
      if frequency[substring[i]] < k:
        new_start = i + 1
        while new_start < len(substring) and frequency[substring[new_start]] < k:
          new_start += 1
        return max(self.divideString(substring[:i], k),
                    self.divideString(substring[new_start:], k))
      
    # Se todos os caracteres aparecem pelo menos k vezes, a resposta é o tamanho da substring
    return len(substring)

  def longestSubstring(self, s: str, k: int) -> int:
    # Função auxiliar para dividir a string
    return self.divideString(s, k)
        
      
    