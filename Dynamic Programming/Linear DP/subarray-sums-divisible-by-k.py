# https://leetcode.com/problems/subarray-sums-divisible-by-k/


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixSumModFreq = {}
        prefixSumModFreq[0] = 1

        answer = 0
        prefixSum = 0

        for num in nums:
            prefixSum += num
            prefixSumMod = prefixSum % k

            if prefixSumMod in prefixSumModFreq:
                answer += prefixSumModFreq[prefixSumMod]
            else:
                prefixSumModFreq[prefixSumMod] = 0
            prefixSumModFreq[prefixSumMod] += 1

        return answer
