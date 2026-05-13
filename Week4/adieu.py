def main():
    adieu()

def adieu():
    names = []
    song = "Adieu, Adieu"

    while True:
        try:
            name = (input("Name: "))
            names.append(name)
        except EOFError:
            break 

    if len(names) == 1:
        song += (", to " + names[0])
        print(song)

    elif len(names) == 2:
        song += (", to " + names[0] + " and " + names[1])
        print(song)
    
    elif len(names) > 2:
        for i, n in enumerate(names):
            if i != len(names)-1:
                song += (", to " + n)
            else:
                song += (", and " + n)
        print(song)

main()
    
            




        
