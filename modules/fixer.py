from netmiko import ConnectHandler

def fix_issues(dev, issues): # issues is {"gig0/1": "ERROR", "gig0/3": "CRC ERRORS", ...}
    conn = ConnectHandler(**dev)
    for interface, error in issues:
        command = f"interface {interface}\r\nshutdown\r\nno shutdown"
        output = conn.send_config_set(command)
    conn.disconnect()
    return output