def main():
    taqueria_menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0.00

    get_order("Item:", taqueria_menu, total)
         

def get_order(prompt, menu, total):
    while True:
        try:
            order = input(prompt).title()
            if order in menu:
                total += menu[order]
                print (f"Total: ${total:.2f}")
        except (ValueError, KeyError):
            continue
        except EOFError:
            break

main()