class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {c:[] for c in range(numCourses)} # 0 -> [], 1 -> []
        for crs, pre in prerequisites: # 0 -> [1], 1 -> []
            mp[crs].append(pre)
        visit = set()
        def dfs(crs):
            if crs in visit:
                return False
            if mp[crs] == []:
                return True
            visit.add(crs)
            for pre in mp[crs]:
                if dfs(pre) == False:
                    return False
            visit.remove(crs)
            mp[crs] = []
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True