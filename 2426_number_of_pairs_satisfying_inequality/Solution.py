import bisect
from typing import List

# Usando array ordenado com bisect
class Solution:
  def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
    # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
    # Cria um array de chaves para armazenar a diferença entre os elementos de nums1 e nums2
    key = []
    count = 0
    
    # Conta quantos pares satisfazem a condição e adiciona a chave no array
    for i in range(len(nums1)):
      # print(key)
      count += bisect.bisect_right(key, nums1[i] - nums2[i] + diff)
      # if (pairs > 0):
      #   count += pairs + 1
      bisect.insort(key, nums1[i] - nums2[i])
      # print(key, count)
            
    return count

# Força bruta
# class Solution:
#   def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
#     numberPairs = 0
#     for i in range(len(nums1)):
#       for j in range(i+1, len(nums2)):
#         if (nums1[i] - nums1[j]) <= (nums2[i] - nums2[j] + diff):
#           numberPairs += 1
#     return numberPairs
  
# print(Solution().numberOfPairs([3,2,5], [2,2,1], 1))