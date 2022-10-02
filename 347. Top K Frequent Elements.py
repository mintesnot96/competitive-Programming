
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        listOfTuples = []
        answer = []
        for i in count:
            heappush(listOfTuples,(-1 * count[i], i) )
        while k:
            answer.append(heappop(listOfTuples)[1])
            k -= 1    
        return answer
