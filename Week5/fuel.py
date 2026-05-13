def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    while True:
        try:
            num, denom = fraction.split("/")
            num = int(num)
            denom = int(denom)

            if denom == 0:
                raise ZeroDivisionError
            if num < 0 or denom < 0 or num > denom:
                raise ValueError
        
        except (ZeroDivisionError, ValueError):
            continue

        return round((num / denom) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    
    elif percentage <= 1:
        return "E"

    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()