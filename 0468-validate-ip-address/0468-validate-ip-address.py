class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def checkv4(s):
            s = s.split('.')
            if len(s) != 4 :
                return False
            for i in s:
                if not i.isnumeric():
                    return False
                if len(i) > 1 and  i[0] == '0' or not (0 <= int(i) <= 255):
                    return False
            return True
        def checkv6(s):
            s = s.split(':')
            if len(s) != 8: return False
            for i in s:
                if not 1 <= len(i) <= 4:
                    return False
                for j in i:
                    if not (j.isnumeric() or "a" <= j <= "f" or "A" <= j <= "F"):
                        return False
            return True
        if checkv4(queryIP):
            return "IPv4"
        elif checkv6(queryIP):
            return "IPv6"
        else:
            return "Neither"
                
        