class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            res = n1
            while res != parent[res]:
                res = parent[parent[res]]
                res = parent[res]
            return res
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return 0
            if p1 > p2:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        components = n
        for n1 in range(n):
            for n2 in range(n1+1,n):
                if isConnected[n1][n2] == 1:
                    components -= union(n1,n2)
        return components