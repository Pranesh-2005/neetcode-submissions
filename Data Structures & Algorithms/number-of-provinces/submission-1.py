class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [1] * n
        def find(n1):
            while n1 != parent[n1]:
                parent[n1] = parent[parent[n1]]
                n1 = parent[n1]
            return n1
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                return 0
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return 1
        res = n
        for n1 in range(n):
            for n2 in range(n1,n):
                if isConnected[n1][n2] == 1:
                    res -= union(n1,n2)
        return res