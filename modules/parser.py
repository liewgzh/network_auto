import re

def parse_interfaces(raw_output):
    lines = raw_output.splitlines() # "Gig0/1 up up\nGig0/2 down down" -> ["Gig0/1 up up", "Gig0/2 down down"]
    return lines