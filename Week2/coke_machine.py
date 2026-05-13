def coke_machine():
    money_owed = 50
    print(f"Amount Due: {money_owed}")
    total_money_paid = 0
    money_paid = 0
    while money_owed > 0:
        money_paid = int(input("Insert Coin: "))
        if money_paid in [5, 10, 25]:
            total_money_paid += money_paid
            money_owed -= money_paid
        if money_owed > 0:
            print(f"Amount Due: {money_owed}")
    
    print(f"Change Owed: {total_money_paid - 50}")

coke_machine()