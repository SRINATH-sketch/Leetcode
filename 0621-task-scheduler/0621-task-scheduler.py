from collections import Counter
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        frequency=Counter(tasks)
        max_frequency=max(frequency.values())
        count_max_frequency=list(frequency.values()).count(max_frequency)
        return max(len(tasks),(max_frequency-1) * (n+1)+count_max_frequency)
