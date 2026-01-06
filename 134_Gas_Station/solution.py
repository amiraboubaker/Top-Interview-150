from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        total_cost = 0
        current = 0
        start = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current += gas[i] - cost[i]
            if current < 0:
                start = i + 1
                current = 0
        return start if total_gas >= total_cost else -1