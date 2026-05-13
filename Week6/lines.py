import sys

def main():
    print(lines())

def lines():
    if len(sys.argv) != 2:
        sys.exit("Too many command-line arguments")
    else:
        counter = 0
        if sys.argv[1].endswith(".py"):
            try:
                with open(sys.argv[1], "r") as file:
                    lines = file.readlines()
            except FileNotFoundError:
                    sys.exit("File does not Exist")
            
            for l in lines:
                if l.strip().startswith("#") or (not l.strip()):
                        continue
                else:
                    counter += 1
        
            return counter
            
        else:
            sys.exit("Not a Python File")
                    
main()
                    

