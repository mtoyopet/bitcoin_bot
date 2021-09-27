from datetime import datetime

# ts = int("1514678400")
# time = datetime.utcfromtimestamp(ts).strftime("%Y/%m/%d %H:%M:%S")
# print(time)

import requests
response = requests.get("https://api.cryptowat.ch/markets/bitflyer/btcjpy/ohlc?periods=86400&after=1514764800")
data = response.json()

# print(data['result']['86400'])

for element in data['result']['86400']:
  if element[0] == 1516147200:
    print(f"最安値: {element[3]}")
    print(f"終値: {element[4]}")
