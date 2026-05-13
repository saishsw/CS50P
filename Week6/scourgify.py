import sys 
import csv

def main():
    scourgify()

def scourgify():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            with open(sys.argv[2], "w") as outfile:
                with open(sys.argv[1], "r") as infile:
                    writer = csv.DictWriter(outfile, fieldnames=["first", "last", "house"])
                    reader = csv.DictReader(infile)

                    writer.writeheader()

                    for row in reader:
                        last, first = row["name"].split(", ")
                        writer.writerow({"first": first, "last": last, "house": row["house"]})

        except FileNotFoundError:
            sys.exit("CSV file does not exist")

main()
            
                

