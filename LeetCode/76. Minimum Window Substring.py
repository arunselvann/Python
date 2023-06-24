class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''

        result = ''
        result_len = float('inf')
        sub_str_count, t_count = {}, {}

        for i in t:
            t_count[i] = 1 + t_count.get(i, 0)

        have, need = 0, len(t_count)
        start = 0
        for end in range(len(s)):
            c = s[end]
            sub_str_count[c] = 1 + sub_str_count.get(c, 0)

            if c in t_count and sub_str_count[c] == t_count[c]:
                have += 1

            while have == need:
                window_len = end - start + 1
                if window_len < result_len:
                    result_len = window_len
                    result = s[start: end + 1]

                sub_str_count[s[start]] -= 1

                if s[start] in t_count and sub_str_count[s[start]] < t_count[s[start]]:
                    have -= 1
                start += 1

        return result


s = Solution()
print(s.minWindow("aa", "aa"))
