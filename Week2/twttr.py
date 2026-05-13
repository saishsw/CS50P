def twttr():
    initial = str(input("Input: "))
    output = ""

    for char in initial:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output += char
    
    return output

print(twttr())



