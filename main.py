import requests
import telebot
import json
from config import telegram_bot_token, stock_token

bot = telebot.TeleBot(telegram_bot_token)

commands_list = []

@bot.message_handler(commands = ["start","help"])
def response(message):
    
    if message.text == "/start":
        bot.send_message(message.chat.id, "Hey, im stock viewer bot\n" + f"Here is list of all commands: {commands_list}")
        
    if message.text == "/help":
        bot.send_message(message.chat.id, f"Here is list of all commands: {commands_list}")
        
   # if message.text == "/find":
    #    bot.send_message(message.chat.id, "give me name or simbol of your security")
        
@bot.message_handler(func=lambda message: True)
def response_security(message):
    response = search_security(message.text)
    if response["bestMatches"] == []:
        bot.send_message(message.chat.id, "I found nothing")

    else:
        bot.send_message(message.chat.id, "I found this:")
        for i in response["bestMatches"]:
            bot.send_message(message.chat.id, format_answer_telegram(i))


def search_security(request_word):
    req = requests.get(f"https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords={request_word}&apikey={stock_token}").json()
    return req 


def create_link_stock_api(**kwargs):
    link = "https://www.alphavantage.co/query?"
    for key, value in kwargs.items():
            link += "{0}={1}&".format(key, value)


            link += f"apikey={stock_token}"
    return link

def format_answer_telegram(row_data):
    row_answer = []
    for i in row_data.keys():
        if i == "5. marketOpen" or i == "6. marketClose" or i == "9. matchScore":
            continue
        else:
            row_answer.append(f"{i[3:].capitalize()}: {row_data[i]}")
    answer = "\n".join(row_answer)
    return answer
    
def main():
    bot.infinity_polling()

if __name__ == "__main__":
    main()
