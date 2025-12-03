def print_report(summary):
    for dev, issues in summary:
        print(f"Device: {dev}, Issues: {issues} (fixed)\n")
    return True