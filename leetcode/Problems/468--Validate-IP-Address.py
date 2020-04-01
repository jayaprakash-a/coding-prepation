class Solution:
    def validateIPV4(self, IP):
        ipSplit = IP.split('.')
        if len(ipSplit) != 4:
            return False
        for i in range(4):
            if len(ipSplit[i]) == 0 or len(ipSplit[i]) > 3:
                return False
            if not ipSplit[i].isdigit():
                return False
            intVal = int(ipSplit[i])
            if intVal < 0 or intVal > 255:
                return False
            if ipSplit[i][0] == '0'  and len(ipSplit[i]) > 1:
                return False
        return True
    
    def validateIPV6(self, IP):
        ipSplit = IP.split(':')
        validChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a','b','c','d','e','f','A','B','C','D','E','F']
        if len(ipSplit) != 8:
            return False
        for i in range(8):
            if len(ipSplit[i]) == 0 or len(ipSplit[i]) > 4:
                return False
            for ch in ipSplit[i]:
                if ch not in validChar:
                    return False

#             if ipSplit[i][0] == '0'  and len(ipSplit[i]) > 1:
#                 return False
        return True
        
        
        
    def validIPAddress(self, IP: str) -> str:
        ipv4, ipv6 = False, False
        if '.' in IP:
            ipv4 = self.validateIPV4(IP)
        elif ':' in IP:
            ipv6 = self.validateIPV6(IP)
        
        if not ipv4 and not ipv6:
            return 'Neither'
        elif ipv4:
            return 'IPv4'
        else:
            return 'IPv6'
        