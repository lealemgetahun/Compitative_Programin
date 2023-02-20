class Solution:
    def checkIPv4(self, ip):
        for i in ip:
            if not i.isdigit():
                return False
            if str(int(i)) != i:
                return False
            if int(i) < 0 or int(i) > 255:
                return False
        return True
    def checkIPv6(self, ip):
        for i in ip:
            if len(i) > 4:
                return False
            try:
                if int(i, 16) < 0:
                    return False
            except:
                return False
        return True
        
    def validIPAddress(self, queryIP: str) -> str:
        ip = queryIP.split(".")

        ip6  = queryIP.split(":")
        if len(ip) == 4 and self.checkIPv4(ip):
            return "IPv4"
        if len(ip6) == 8 and self.checkIPv6(ip6):
            return "IPv6"
        return "Neither"


       