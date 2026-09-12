class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        premp = { c:[] for c in range(numCourses)}
        for crs,pre in prerequisites:
            premp[crs].append(pre)
        res = []
        visit,cycle = set(),set()
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in premp[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
            return True
        for crs in range(numCourses):
            if dfs(crs) == False:
                return []
        return res