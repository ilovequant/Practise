from heapq import *


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """

    def topKFrequentWords(self, words, k):
        # write your code here
        map = {}
        for word in words:
            if word not in map.keys():
                map[word] = -1
            else:
                map[word] -= 1

        def __lt__(self, other):
            return self.intAttribute < other.intAttribute

        temp = []

        for key in map.keys():
            temp.append([map[key], key])

        heap = []

        for item in temp:
            heappush(heap, item)

        res = []

        for i in range(k):
            res.append(heappop(heap)[1])

        return res



#solution2:

from heapq import *


class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq
        else:
            return self.word > other.word


class Solution(object):
    def topKFrequentWords(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = []
        for word, freq in count.items():
            heappush(heap, FreqWord(freq, word))
            if len(heap) > k:
                heappop(heap)

        return [heappop(heap).word for _ in range(k)][::-1]