import requests

def advice_slip():
    url = 'https://api.adviceslip.com/daily_adviceslip.rss'
    response = requests.get(url)
    info = info.json()

    
    return info
print(advice_slip())