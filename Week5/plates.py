def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
        # Rule 1 - Length
    if not 6 >= len(s) > 2:
        return False
    # Rule 2 - First two letter
    if not s[0:2].isalpha():
        return False
    
    # Rule 3 - Only AlphaNumeric
    if not s.isalnum():
        return False

    seen_number = False 

    for char in s:
        if char.isdigit():
            if not seen_number:
                if char == 0:
                    return False
                seen_number = True
        else:
            if seen_number:
                return False
    return True
    


if __name__ == "__main__":
    main()