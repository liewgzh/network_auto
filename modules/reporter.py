def print_report(summary):
    for dev, issues in summary.items():
        if not issues:
            print(f"{dev}: no issues found")
        else:
            print(f"{dev}: fixed issues:")
            for intf, err in issues.items():
                print(f" - {intf}: {err} fixed!")
        print()