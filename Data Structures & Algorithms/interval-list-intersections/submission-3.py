class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1 = 0
        ptr2 = 0
        intersections = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
            first = firstList[ptr1]
            second = secondList[ptr2]
            if max(first[0], second[0]) <= min(first[1],second[1]):
                intersections.append([max(first[0],second[0]),min(first[1],second[1])])
            if min(first[1],second[1]) == first[1]:
                ptr1+=1
            if min(first[1],second[1]) == second[1]:
                ptr2+=1
        return intersections