def main():
    tank = get_tank("Fraction: ")

    if tank >= 99:
        print("F")
    
    elif tank <= 1:
        print("E")

    else:
        print(f"{tank}%")

def get_tank(prompt):
    while True:
        try:
            f = input(prompt)
            num, denom = f.split("/")
            num = int(num)
            denom = int(denom)

            if denom == 0:
                raise ZeroDivisionError
            if num < 0 or denom < 0 or num > denom:
                raise ValueError
        
        except (ZeroDivisionError, ValueError):
            continue

        return round((num / denom) * 100)
    
main()