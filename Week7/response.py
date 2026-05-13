import validators

def main():
    print(validate(input("Email: ")))

def validate(email):
    if validators.email(email):
        return f"Valid"
    else:
        return f"Invalid"

main()