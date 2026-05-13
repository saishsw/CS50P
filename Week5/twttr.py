def main():
    word = str(input("Input: "))
    print(shorten(word))

def shorten(word):
    output = ""

    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            output += char
    
    return output

if __name__ == "__main__":
    main()