from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre_req_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_req_map[crs].append(pre)

        visit_set = set()

        def dfs(crs):
            if crs in visit_set:
                return False
            if not pre_req_map:
                return True

            visit_set.add(crs)

            for pre in pre_req_map[crs]:
                if not dfs(pre):
                    return False

            visit_set.remove(crs)
            pre_req_map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True


s = Solution()
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
