import requests
from datetime import datetime
import math
from newsapi import NewsApiClient
import os
from twilio.rest import Client
import html



API_KEY_STOCK = "N6YTJ2C85QNQT963"
NEWS_API_KEY = "a4d28a6f6e9445fcbbd72d0b0b9e0e86"
TWILIO_ACT_ID = "AC858b33ee0a38269cf3af758e8809dd2b"
TWILIO_AUTH_TOKEN = "fdea73a89fb6abf795fec20005bb56ad"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


def get_stock_change():
    stock_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
    params = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'apikey': API_KEY_STOCK
    }

    dataset = {
        "change": 0,
        "yesterday": None,
        "day before yesterday": None
    }
    response = requests.get(stock_url, params)
    response.raise_for_status()
    print(response.status_code)
    print(response.json())
    stocks_data = response.json()
    last_refreshed = stocks_data['Meta Data']['3. Last Refreshed']

    prev_date = datetime.fromisoformat(last_refreshed)
    prev_before_prev = prev_date.replace(day=(prev_date.day - 1))
    prev_date_string = prev_date.strftime("%Y-%m-%d")
    prev_before_prev_string = prev_before_prev.strftime("%Y-%m-%d")

    yesterday_stocks = stocks_data['Time Series (Daily)'][prev_date_string]
    day_before_yesterday_stocks = stocks_data['Time Series (Daily)'][prev_before_prev_string]

    print(yesterday_stocks)
    print(day_before_yesterday_stocks)

    price_close_yesterday = float(yesterday_stocks['4. close'])
    price_close_day_before = float(day_before_yesterday_stocks['4. close'])
    change = math.floor(((price_close_yesterday - price_close_day_before) / price_close_day_before) * 100)
    print(change)
    dataset['change'] = change
    dataset['yesterday'] = prev_date_string
    dataset['day before yesterday'] = prev_before_prev_string
    return dataset


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news_articles(yesterday, day_before_yesterday):
    news = NewsApiClient(api_key=NEWS_API_KEY)
    all_articles = news.get_everything(q="tesla", from_param=day_before_yesterday, to=yesterday,
                                       language="en", sort_by="relevancy")
    if all_articles['status'] == 'ok':
        news = all_articles['articles'][:3]
        return news


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message(content):
    client = Client(TWILIO_ACT_ID, TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=content,
        from_='+12058517950',
        to='+919810116672'
    )

    print(message.sid)
    print(message.status)
    print(message.error_message)
    print(message.error_code)

# Optional: Format the SMS message like this:

returned_data = get_stock_change()
print(returned_data)
if math.fabs(returned_data['change']) >= 3:
    news = get_news_articles(returned_data['yesterday'], returned_data['day before yesterday'])
    print(news)
    for news_article in news:
        content = ""
        if returned_data['change'] < 0:
            content += STOCK + "↑"
        else:
            content += STOCK + "↓"
        content += str(math.fabs(returned_data['change'])) + "%" + "\n"

        heading = html.unescape(news_article['title'])
        brief = html.unescape(news_article['description'])
        content += "Headline: " + heading + '\n'
        content += "Brief: " + brief + '\n'
        send_message(content)

    print(content)
    # send_message(content)
# print(prev_date)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
