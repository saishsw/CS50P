import emoji 

def main():
    emojize_text()

def emojize_text():
        original_text = str(input("Input: ").lower())
        print(f"Output: {emoji.emojize(original_text, language='alias')}")

main()
