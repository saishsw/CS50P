def main():
    make_list()

def make_list():
    groceries = {}
    while True:
        try:
            item = str(input().upper())

            if item not in groceries:
                groceries[item] = 1
            
            elif item in groceries:
                groceries[item] += 1
        
        except EOFError:
            break 
    
    for item in sorted(groceries):
        print(f"{groceries[item]} {item}")
    
main()
