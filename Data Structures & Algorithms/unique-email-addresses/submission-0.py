class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            names = email.split("@")
            local_name = names[0]
            plus_sign_index = local_name.find("+")
            if plus_sign_index != -1:
                local_name = local_name[:plus_sign_index]
            period_index = local_name.find(".")
            while period_index != -1:
                local_name = local_name[:period_index] + local_name[period_index+1:]
                period_index = local_name.find(".")
            domain_name = names[1]

            email_set.add(local_name + "@" + domain_name)
            
        return len(email_set)