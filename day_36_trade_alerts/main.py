import requests
from twilio.rest import Client

news_url = "https://gnews.io/api/v4/search?q=bitcoin&token=e006d703dfd3b85f7ce52b47a56ec704"
price_url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
yesterday_price_url = "https://api.coingecko.com/api/v3/coins/bitcoin/history?date=04-11-2021&localization=false"

twilio_account_sid = "XXXX"
twilio_auth_token = "XXXX"
client = Client(twilio_account_sid, twilio_auth_token)

news_response = requests.get(news_url)
price_response = requests.get(price_url)
yesterday_price_response = requests.get(yesterday_price_url)

trading_news = news_response.json()["articles"][0]
trading_prices = price_response.json()["bitcoin"]
yesterday_prices = yesterday_price_response.json()["market_data"]["current_price"]

if trading_prices['usd'] - yesterday_prices['usd'] < 0:
    change = yesterday_prices['usd'] - trading_prices['usd']
    symbol = '🔻'
else:
    change = trading_prices['usd'] - yesterday_prices['usd']
    symbol = '🔺'

percentage = change * 100 / yesterday_prices["usd"]

message = f""

message = client.messages \
    .create(
    body=f"${trading_prices['usd']} {round(percentage, 2)}%{symbol}\n{trading_news['description']}\nlink: {trading_news['url']} ",
    from_='+12674891940',
    to='+XXXX'
)
print(message.status)
