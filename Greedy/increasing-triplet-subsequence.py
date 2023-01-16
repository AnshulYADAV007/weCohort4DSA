# https://leetcode.com/problems/increasing-triplet-subsequence/description/

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        isLeftSmallerExist = self.getIsLeftSmallerExist(nums)
        isRightLargerExist = self.getIsRightLargerExist(nums)
        return self.isBothTrueExist(isLeftSmallerExist, isRightLargerExist)

    def getIsLeftSmallerExist(self, nums):
        answer = []
        minimum = nums[0]
        for num in nums:
            if num > minimum:
                answer.append(True)
            else:
                minimum = num
                answer.append(False)
        return answer

    def getIsRightLargerExist(self, nums):
        answer = []
        maximum = nums[-1]
        for num in nums[::-1]:
            if num < maximum:
                answer.append(True)
            else:
                maximum = num
                answer.append(False)
        return answer[::-1]

    def isBothTrueExist(self, left, right):
        for i in range(len(left)):
            if left[i] and right[i]:
                return True
        return False
