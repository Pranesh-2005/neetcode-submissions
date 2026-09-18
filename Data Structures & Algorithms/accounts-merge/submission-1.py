class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = [i for i in range(n)]
        rank = [1]*n
        def find(n1):
            while n1 != parent[n1]:
                parent[n1] = parent[parent[n1]]
                n1 = parent[n1]
            return n1
        def union(n1,n2):
            p1,p2 = find(n1),find(n2)
            if p1==p2:
                return False
            if rank[p2] > rank[p1]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        emailtoacc = {}
        for i,a in enumerate(accounts):
            for email in a[1:]:
                if email in emailtoacc:
                    union(i,emailtoacc[email])
                else:
                    emailtoacc[email] = i
        emailgrp = defaultdict(list)
        for email,account in emailtoacc.items():
            leader = find(account)
            emailgrp[leader].append(email)
        res = []
        for account,email in emailgrp.items():
            name = accounts[account][0]
            res.append([name]+list(sorted(email)))
        return res