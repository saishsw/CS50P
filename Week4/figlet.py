from pyfiglet import Figlet
import sys
import random

def main():

    fontize()

def fontize():
    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(sys.argv) == 1:
        text = (input("Input: "))
        figlet.setFont(font=random.choice(fonts))

    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in fonts:
            text = (input("Input: "))
            figlet.setFont(font=sys.argv[2])
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")
    
    print(figlet.renderText(text))


main()


