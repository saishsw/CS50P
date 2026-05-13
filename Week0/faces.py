def convert(InitialString):
    print(InitialString.replace(":)","🙂").replace(":(","🙁"))

def main():
    InitialString = str(input("What faces do you want to convert? "))
    convert(InitialString)

main()