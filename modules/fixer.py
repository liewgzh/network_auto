from netmiko import ConnectHandler

def fix_issues(dev, issues): # issues is {"gig0/1": "ERROR", "gig0/3": "CRC ERRORS", ...}
    conn = ConnectHandler(**dev)
    output_all={}

    for interface, error in issues.items():
        command = [
            f"interface {interface}",
            "shutdown",
            "no shutdown"
        ]
        output = conn.send_config_set(command)
        output_all[interface] = output

    conn.disconnect()
    return output_all