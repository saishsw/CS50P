import random

def main():
    game()

def game():
    while True:
        try:
            n = int(input("Level: "))
        except ValueError:
            continue

        if n < 0:
            continue
        else:
            break
    
    answer = random.randint(1, n)

    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            continue
        if guess < 0:
            continue
        elif guess > answer:
            print("Too large!")
        elif guess < answer:
            print("Too small!")
        elif guess == answer:
            print("Just Right!")
            break
main()
    