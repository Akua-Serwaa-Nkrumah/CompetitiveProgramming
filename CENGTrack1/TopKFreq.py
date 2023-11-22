from heapq import *
from collections import Counter
class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        heap = []
        word_count = Counter(words)

        for key in word_count:
            heap.append(-word_count[key])

        heapify(heap)

        freq = []
        i = 0
        while i < k:
            mx = heappop(heap)
            words = []
            for j in word_count:
                if word_count[j] == -mx and j not in freq:
                    words.append(j)
            freq.extend(sorted(words))
            i += 1
        
        return freq[:k]

        