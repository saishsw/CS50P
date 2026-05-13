def hello():
    Greeting = str(input("Greeting: ")).lower().strip()
    if Greeting == "hello":
        print("$0")
    elif Greeting[0] == "h":
        print("$20")
    else:
        print("$100")

hello()
