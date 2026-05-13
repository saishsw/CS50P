import datetime
import sys 
import inflect

def main():
    print(seasons(input("Date of Birth: ")))

def seasons(b):
    p = inflect.engine()
    try:
        birthdate = datetime.datetime.strptime(b, "%Y-%m-%d").date()
        today = datetime.date.today()
        difference = today - birthdate
        minute_difference = difference.days * 24 * 60
    except ValueError:
        sys.exit()
    return f"{p.number_to_words(minute_difference, andword = "")} minutes"


if __name__ == "__main__":
    main()