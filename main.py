import yaml
from modules.connector import run_cmd
from modules.parser import parse_interfaces
from modules.checker import check_issues
from modules.fixer import fix_issues
from modules.reporter import print_report

def load_devices():
    with open("devices.yml") as f:
        return yaml.safe_load(f)["devices"]

def main():
    devices = load_devices()
    summary={}

    for dev in devices:
        raw = run_cmd(dev, "show interfaces")
        parsed = parse_interfaces(raw) # parsed is now ["Gig0/1", "up", "Gig0/2", "up", "CRC ERRORS", "Gig0/3", ...]
        issues = check_issues(parsed)

        if issues:
            fix_issues(dev, issues) # issues is now {"gig0/1": "ERROR", "gig0/3": "CRC ERRORS", ...}

        summary[dev["name"]] = issues

    print_report(summary)

if __name__ == "__main__":
    main()