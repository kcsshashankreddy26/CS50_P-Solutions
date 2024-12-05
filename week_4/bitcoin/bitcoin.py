import requests
import sys
import json

try:
    if len(sys.argv) == 2:
        number = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        res = response.json()
        price = res['bpi']['USD']["rate_float"]
        total = price * number
        print(f"${total:,.4f}")
    else:
        sys.exit("Missing command-line argument")
except requests.RequestException:
    sys.exit("Command-line argument is not a number")