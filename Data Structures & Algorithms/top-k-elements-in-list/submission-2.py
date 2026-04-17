class Solution(object):
    def topKFrequent(self, nums, k):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        items = []
        for num in seen:
            items.append((num, seen[num]))


        items.sort(key=lambda x: x[1], reverse=True)

  
        result = []
        for i in range(k):
            result.append(items[i][0])

        return result
        