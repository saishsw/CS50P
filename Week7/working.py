import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^([\d:]+)(?: )(AM|PM)(?: to )([\d:]+)(?: )(AM|PM)$", s):
        initial_minute = "00"
        final_minute = "00"
        initial_hour = matches.group(1)
        final_hour = matches.group(3)
        if ":" in matches.group(1):
            initial_hour, initial_minute = matches.group(1).split(":")
        if ":" in matches.group(3):
            final_hour, final_minute, = matches.group(3).split(":")
        if ((1 <= int(initial_hour) <= 12) and (int(initial_minute) < 60) and (matches.group(2) in ["AM", "PM"])) and ((1 <= int(final_hour) <= 12) and (int(final_minute) < 60)and (matches.group(4) in ["AM", "PM"])):
            converted_initial_time = convert_time(initial_hour, initial_minute, matches.group(2))                
            converted_final_time = convert_time(final_hour, final_minute, matches.group(4))
        else:
            raise ValueError
    else:            
        raise ValueError
    
    return f"{converted_initial_time} to {converted_final_time}"

def convert_time(hour, minute, period):
    new_hour = ""
    if period == "AM":
        if hour == "12":
            new_hour = "00"
        else:
            new_hour = f"{int(hour):02}"
    elif period == "PM":
        if hour == "12":
            new_hour = "12"
        else:
            new_hour = f"{(int(hour) + 12):02}"
    else:
        raise ValueError
    new_time = f"{new_hour}:{minute}"
    return new_time



if __name__ == "__main__":
    main()