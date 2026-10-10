class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        res = 0
        travel = 0
        for i in range(len(gas)):
            travel += gas[i] - cost[i]
            if travel < 0:
                travel = 0
                res = i+1
        return res