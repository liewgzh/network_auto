import re

def check_issues(lines):
    issues={}
    current_intf=None

    intf_pattern = r"^(?:GigabitEthernet|FastEthernet)\d+/\d+"
    crc_pattern = r"(\d+)\s+CRC"
    err_pattern = r"(\d+)\s+input errors"

    for line in lines:
        line = line.strip()

        m_intf = re.match(intf_pattern, line)
        if m_intf:
            current_intf = m_intf.group(0)
            continue

        m_crc = re.search(crc_pattern, line)
        if m_crc and int(m_crc.group(1)) > 0:
            issues[current_intf] = "CRC ERRORS"

        m_err = re.match(err_pattern, line)
        if m_err and int(m_err.group(1)) > 0:
            issues[current_intf] = "INPUT ERRORS"
    
    return issues