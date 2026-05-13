import sys
import tabulate
import csv


def main():
    pretty()

def pretty():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line argument")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line argument")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print({tabulate.tabulate(reader, header = "keys", tablefmt = "grid")})
            
        except FileNotFoundError:
            sys.exit("File does not Exist")

main()


