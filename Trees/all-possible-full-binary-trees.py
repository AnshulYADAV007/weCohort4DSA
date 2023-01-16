# https://leetcode.com/problems/all-possible-full-binary-trees/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        return self.allPossibleFBTHelper(n, dp)

    def allPossibleFBTHelper(self, n, dp):
        if n in dp:
            return dp[n]
        if n == 1:
            return [TreeNode()]
        if n % 2 == 0:
            return []
        answer = []
        for leftCount, rightCount in self.getChildrenCount(n):
            leftTrees = self.allPossibleFBTHelper(leftCount, dp)
            rightTrees = self.allPossibleFBTHelper(rightCount, dp)
            answer = self.combineAll(answer, leftTrees, rightTrees)
        dp[n] = answer
        return dp[n]

    def getChildrenCount(self, n):
        answer = []
        for left in range(1, n - 1, 2):
            yield [left, n-1-left]

    def combineAll(self, answer, leftTrees, rightTrees):
        for left in leftTrees:
            for right in rightTrees:
                root = TreeNode()
                root.left = left
                root.right = right
                answer.append(root)
        return answer


# Version 2

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution2:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}
        return self.allPossibleFBTHelper(n, dp)

    def allPossibleFBTHelper(self, n, dp):
        if n in dp:
            return dp[n]
        if n == 1:
            return [TreeNode()]
        if n % 2 == 0:
            return []
        answer = []
        for leftCount, rightCount in self.getChildrenCount(n):
            leftTrees = self.allPossibleFBTHelper(leftCount, dp)
            rightTrees = self.allPossibleFBTHelper(rightCount, dp)
            self.combineAll(answer, leftTrees, rightTrees)
        dp[n] = answer
        return dp[n]

    def getChildrenCount(self, n):
        answer = []
        for left in range(1, n - 1, 2):
            yield [left, n-1-left]

    def combineAll(self, answer, leftTrees, rightTrees):
        for left in leftTrees:
            for right in rightTrees:
                root = TreeNode()
                root.left = left
                root.right = right
                answer.append(root)
