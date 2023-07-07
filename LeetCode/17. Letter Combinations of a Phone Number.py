from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_digit_map = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                         '9': 'wxyz'}

        result = []

        def backtrack(i, curstr):
            if len(curstr) == len(digits):
                result.append(curstr)
                return

            for c in num_digit_map[digits[i]]:
                backtrack(i + 1, curstr + c)

        if digits:
            backtrack(0, '')

        return result


s = Solution()
print(s.letterCombinations("23"))
