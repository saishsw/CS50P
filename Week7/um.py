import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    s = s.lower()
    matches = re.findall(r"(\W|^)(um)(\W|$)", s)
    return len(matches)
