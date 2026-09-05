class Solution:
    def countSeniors(self, details: List[str]) -> int:
        seniors = 0
        for detail in details:
            if int(detail[11:13]) > 60:
                seniors += 1
        return seniors