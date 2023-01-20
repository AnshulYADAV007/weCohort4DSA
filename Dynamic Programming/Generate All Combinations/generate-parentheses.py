class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]
        twoLess = self.generateParenthesis(n-1)
        answer = set(["(" + x + ')' for x in twoLess])
        for i in range(1, n):
            left = self.generateParenthesis(i)
            right = self.generateParenthesis(n-i)
            self.appendAll(answer, left, right)
        return list(answer)

    def appendAll(self, answer, left, right):
        for l in left:
            for r in right:
                answer.add(l + r)
