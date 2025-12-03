from netmiko import ConnectHandler

def run_cmd(device, command):
    conn = ConnectHandler(**device)
    output = conn.send_command(command)
    conn.disconnect()
    return output