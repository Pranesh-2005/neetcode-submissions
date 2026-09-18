class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    def find(self,n1):
        res = n1
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res
    def union(self,n1,n2):
        p1,p2 = self.find(n1),self.find(n2)
        if p1 == p2:
            return False
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        else: 
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        return True
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailtoacc = {}
        for i,a in enumerate(accounts):
            for e in a[1:]:
                if e in emailtoacc:
                    uf.union(i,emailtoacc[e])
                else:
                    emailtoacc[e] = i
        emailgrp = defaultdict(list)
        for e,a in emailtoacc.items():
            leader = uf.find(a)
            emailgrp[leader].append(e)
        res = []
        for a,emails in emailgrp.items():
            name = accounts[a][0]
            res.append([name]+list(sorted(emailgrp[a])))
        return res
        