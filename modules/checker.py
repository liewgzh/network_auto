import re

def check_issues(lst):
    interfaces = {}
    pattern_int = r"\w+\d/\d"
    pattern_crc = r"CRC ERRORS"
    pattern_error = r"ERRORS"
    for i in range(len(lst)):
        if re.match(pattern_int, lst[i]):
            for j in range(i+1, len(lst)):
                if not re.match(pattern_int, lst[j]) and (re.match(pattern_crc, lst[j]) or re.match(pattern_error, lst[j])):
                    interfaces[lst[i]] = lst[j]
                    break
    return interfaces