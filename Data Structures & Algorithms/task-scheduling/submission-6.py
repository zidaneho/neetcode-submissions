class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqTable = {}
        for task in tasks:
            freqTable[task] = freqTable[task] + 1 if task in freqTable else 1
        maxf = -1
        maxfTask = None
        for task, count in freqTable.items():
            if count > maxf:
                maxf = count
                maxfTask = task
        idle = (maxf - 1) * n
        for task,count in freqTable.items():
            if task == maxfTask:
                continue
            idle -= min(maxf-1,count)
        if idle > 0:
            return len(tasks) + idle
        return len(tasks)
            

