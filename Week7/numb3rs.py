import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if (matches := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$", ip)):
        validity = True
        for n in matches.groups():
            if n.startswith("0") or int(n) > 255:
                validity = False
            else:
                continue
        return validity
    else:
        return False


if __name__ == "__main__":
    main()