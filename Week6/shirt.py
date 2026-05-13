import sys 
from PIL import Image, ImageOps 

def main():
    shirt()

def shirt():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif (sys.argv[1].split(".")[-1].lower() not in ["jpeg", "jpg", "png"]) or (sys.argv[2].split(".")[-1].lower() not in ["jpeg", "jpg", "png"]):
        sys.exit("Invalid input")
    elif sys.argv[1].split(".")[-1].lower() != sys.argv[2].split(".")[-1].lower():
        sys.exit("Input and Output have different extensions")
    else:
        try:
            input_image = Image.open(sys.argv[1])
            shirt = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("Input does not exist")
        
        size = shirt.size
        result = ImageOps.fit(input_image, size)
        result.paste(shirt, shirt)
        result.save(sys.argv[2])


