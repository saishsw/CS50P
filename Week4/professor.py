import random


def main():
    level = get_level()
    score = 0

    for i in range(10):
        X = generate_integer(level)
        Y = generate_integer(level)

        for j in range(3):
            try:
                answer = input(f"{X} + {Y} = ")

                if int(answer) == (X + Y):
                    score += 1
                    break
                else:
                    print("EEE")
                    if (j == 2):
                         print(f"{X} + {Y} = {X + Y}")
            except ValueError:
                print("EEE")
                if (j == 2):
                    print(f"{X} + {Y} = {X + Y}")
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    return random.randint((10 ** (level - 1)), (1 * ((10 ** level) - 1 )))


if __name__ == "__main__":
    main()