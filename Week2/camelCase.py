def camel_to_snake():
    input_word = input("camel case: ")
    result = ""

    for char in input_word:
        if char.isupper():
            result += "_"
        result += char.lower()

    return result
    

print(camel_to_snake())




