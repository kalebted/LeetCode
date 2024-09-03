class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        res = []
        even = []
        odd = []

        for i in nums:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even.pop())
            else:
                res.append(odd.pop())
        return res