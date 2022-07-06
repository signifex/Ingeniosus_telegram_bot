import requests
import ujson

from config import open_weather_token, stock_token



def get_weather(city = "vienna"):
    req = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}").json()
    return req

def get_stock_market_data(request_word):
    
    req = requests.get(f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={request_word}&apikey={stock_token}").json()
    print (f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={request_word}&apikey={stock_token}")
    return req 

def create_link_stock_api(**kwargs):
    link = "https://www.alphavantage.co/query?"
    for key, value in kwargs.items():
            link += "{0}={1}&".format(key, value)
    link += f"apikey={stock_token}"
    return link


    # 'https://www.alphavantage.co/query?function={TIME_SERIES_INTRADAY}&symbol={IBM}&interval={5min}&outputsize={full}&datatype={}&apikey={demo}').json
    
    # create a list with all possible functions(parcer doctumetation list) and make elif for all kinds of API's requests

    #search endpoint to find out is stock exist
     

"""
def get_data_config(stock_token, core = "stock", function = "TIME_SERIES_INTADAY", symbol = "GOOGL", interval = "15 min", adjusted = "True", outputsize = "compact", datatype = "json"):
    if core = "stock":
        function == "TIME_SERIES_INTRADAY":

    elif core = "fundaemntal data":
        congig
    elif core = "forex":

    elif core = "crypto":

    elif core = "economic_indicator":

    elif core = "techno indicator":
        return 

    else:

alpfa_api_stock_dict = {

    "function" : ("TIME_SERIES_INTRADAY", "TIME_SERIES_INTRADAY_EXTENDED"), #first need a working bot, than fill this dictionary and extend possible requests

    "symbol" : (), # function with API endpoint search
    
    "interval" : ("1min", "5min", "15min", "30min", "60min"),

    "adjusted" : ("true", "false"),

    "outputsize" : ("compact", "full"),

    "datatype" : ("json", "csv")
    
    }

"""
