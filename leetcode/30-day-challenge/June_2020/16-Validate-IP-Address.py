class Solution:
    def validIPAddress(self, IP: str) -> str:
        def validateIPv4(IP):
            split = IP.split('.')
            for num in split:
                for ch in num:
                    if not ch.isdigit():
                        return 'Neither'
                if len(num) == 0:
                    return 'Neither'
                if int(num) > 255 or int(num) < 0:
                    return 'Neither'
                if len(str(int(num))) != len(num):
                    return 'Neither'
            return 'IPv4'
        def validateIPv6(IP):
            valid = '0123456789abcdef'
            split = IP.split(':')
            for num in split:
                for ch in num:
                    if ch not in valid:
                        return 'Neither'
                if len(num) > 4 or len(num) <= 0:
                    return 'Neither'
            return 'IPv6'        
        if IP.count('.') == 3:
            return validateIPv4(IP.lower())
        elif IP.count(':') == 7:
            return validateIPv6(IP.lower())
        return 'Neither'