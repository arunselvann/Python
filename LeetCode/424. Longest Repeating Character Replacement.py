class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count = {}
        result = 0
        start = 0
        for end in range(len(s)):
            char_count[s[end]] = 1 + char_count.get(s[end], 0)

            cur_len = end - start + 1
            if cur_len - max(char_count.values()) > k:
                char_count[s[start]] -= 1
                start += 1
            else:
                result = max(result, cur_len)
        return result


s = Solution()
print(s.characterReplacement("AABABBA", 1))
