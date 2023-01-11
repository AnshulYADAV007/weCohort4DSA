class Solution:
    def getMaxRepetitions(self, text: str, n1: int, pattern: str, n2: int) -> int:
        if pattern == text:
            return n1//n2
        if self.isSubsequence(pattern, text):
            count = self.countPatterns(pattern, text + text)
            result = ((n1 // 2) * count) // n2
            if n1 % 2 == 1:
                result += self.countPatterns(pattern * n2, text)
            return result
        repeatedText = text * n1
        repeatedPattern = pattern * n2
        return self.countPatterns(repeatedPattern, repeatedText)

    def countPatterns(self, pattern, text):
        dp = [0] * len(text)
        # dp[i] = the count of repeatations of pattern in text[:i+1]
        for i in range(len(text)):
            for j in range(-1, i):
                if self.isSubsequence(pattern, text[j+1: i+1]):
                    dp[i] = dp[j] + 1
        print(dp)
        return max(dp)

    def isSubsequence(self, pattern, text) -> bool:
        if len(pattern) > len(text):
            return False
        # can return if pattern is a subsequence of text
        dp = [[0] * len(text) for _ in range(len(pattern))]
        # dp[i][j] = the length of the longest
        # common subsequence of s1[:i+1], text[:j+1]
        # dp[i][j] = 1 + dp[i-1][j-1] if s1[i] == text[j]
        # otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        dp[0][0] = 1 if pattern[0] == text[0] else 0

        for i in range(1, len(pattern)):
            if pattern[i] == text[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]

        for j in range(1, len(text)):
            if pattern[0] == text[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(pattern)):
            for j in range(1, len(text)):
                if pattern[i] == text[j]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1] == len(pattern)


# Another solution

class Solution2:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        text = s1
        pattern = s2
        textIndex = 0
        textCount = 0
        patternCount = 0
        patternIndex = 0

        while textCount < n1:
            if pattern[patternIndex] == text[textIndex]:
                patternIndex += 1
                textIndex += 1
            else:
                textIndex += 1
            if patternIndex == len(pattern):
                patternCount += 1
                patternIndex = 0
            if textIndex == len(text):
                textIndex = 0
                textCount += 1

        return patternCount // n2
