def main():
    date = transform_outdated("Date: ")

def transform_outdated(prompt):
    month_list = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            outdated = str(input(prompt).title())

            if "/" in outdated:
                month, day, year = outdated.split("/")

            elif "," in outdated:
                outdated = outdated.replace(",", "")
                month, day, year = outdated.split()
                month = (month_list.index(month) + 1)
                
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or day > 31:
                raise ValueError
            else:
                break

        except ValueError:
            continue
    
    print(f"{year}-{month:02}-{day:02}")

main()