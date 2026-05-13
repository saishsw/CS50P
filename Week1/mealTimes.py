def main():
    time = input("What time is it? ")
    time = convert(time)
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")


def convert(time):
    if len(time) == 4:
         minuteDecimal = (float(time[-2])) / 60
         return float(time[0]) + minuteDecimal
    elif len(time) == 5:
        minuteDecimal = (float(time[-2])) / 60
        return float(time[:2]) + minuteDecimal       

if __name__ == "__main__":
    main()