import re

def parse_interfaces(file):
    pattern_int = r"[GigEthFastEthernet]\d/\d"
    pattern_up = r"up"
    pattern_down = r"down"
    pattern_crc = r"(\d+) CRC"
    pattern_errors = r"(\d+) input errors"
    lst=[]
    for line in file:
        interface = re.search(pattern_int, line)
        up = re.search(pattern_up, line)
        down = re.search(pattern_down, line)
        crc = re.search(pattern_crc, line)
        errors = re.search(pattern_errors, line)
        if crc.group(1) > 0:
            crc = "CRC ERRORS"
            lst+=crc
        if errors.group(1) > 0:
            errors = "ERRORS"
            lst+=errors
        if interface:
            lst+=interface, up, down
    return lst