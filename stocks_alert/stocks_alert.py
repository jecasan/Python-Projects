import requests
import os
import smtplib

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

MY_EMAIL = "jerickpython@gmail.com"
PASSWORD = os.environ.get("JP_PASS")

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_PARAMS = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK,
    "apikey" : os.environ.get("STOCK_APIKEY"),
}

def main():
    prices = get_prices()
    percent = get_diff_percent(prices[0], prices[1])
    
    if percent[0] > 5 and percent[1] is False:
        tsla = f"🔻{percent[0]}%"
        get_news(tsla)
    elif percent[0] > 5 and percent[1] is True:
        tsla = f"🔺🔻{percent[0]}%"
        get_news(tsla)
    else:
        pass
    
def get_prices():
    stock_res = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
    stock_res.raise_for_status()
    stock_data = stock_res.json()["Time Series (Daily)"]
    data_list = [value for (key, value) in stock_data.items()]
    yesterday_data = data_list[0]
    yesterday_closing = float(yesterday_data["4. close"])
    bf_yesterday_data = data_list[1]
    bf_yesterday_closing = float(bf_yesterday_data["4. close"])
    return yesterday_closing, bf_yesterday_closing

def get_diff_percent(yesterday, before_yesterday):
    change_in_value = abs(yesterday - before_yesterday)
    diff_percent = (change_in_value / yesterday) * 100
    
    if yesterday > before_yesterday:
        increase = True
        return diff_percent, increase
    else:
        increase = False
        return diff_percent, increase

def get_news(tsla):
    news_res = requests.get('https://newsapi.org/v2/everything?'
        'q=tesla&'
        'from=2025-01-20&'
        'sortBy=popularity&'
        'apiKey=801ad8a8940944fc92d0710014224d9b')
    news_res.raise_for_status()
    news = news_res.json()["articles"]
    articles = [f"TSLA: {tsla}\n Headline: {news[_]['title']}\n Brief: {news[_]['description']}" for _ in range(0,3)]
    
    for message in articles:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, 
                                to_addrs=MY_EMAIL, 
                                msg=f"Subject:Tesla Stocke News!\n\n{message}".encode('utf-8')
            )
    


