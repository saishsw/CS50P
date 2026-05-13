import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit()
    else:
        try:
            quantity = float(sys.argv[1])
        except ValueError:
            sys.exit()
    

        try:
            response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b315c5de4366c03cc46e9703c8244b6cda263da1480371b1e327da3d56e4c54e")
            result = response.json()
            price = float(result["data"]["priceUsd"])
        except requests.RequestException:
            sys.exit()
    total = quantity * price
    print(f"${total:,.4f}")

main()
 

