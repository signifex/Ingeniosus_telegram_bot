import requests
import telebot
import json
from modules import get_stock_market_data, create_link_stock_api
from config import telegram_bot_token

bot = telebot.TeleBot(telegram_bot_token)

commands_list = ["start","help","find"]

@bot.message_handler(commands = commands_list)
def response(message):
    
    if message == "start":
        bot.send_message(message.chat.id, "Hey, im stock viewer bot\n" + f"Here is list of all commands: {commands_list}")
        
    if message == "help":
        bot.send_message(message.chat.id, f"Here is list of all commands: {commands_list}")
        
    if message == "find":
        bot.send_message(message.chat.id, "give me name or simbol of your security")
        echo_find(message)


    
@bot.message_handler(func=lambda message: True)
def echo_find(message):
    
    answer = get_stock_market_data(message.text)
    bot.send_message(message.chat.id, json.dumps(answer))





"""
# Handles all text messages that match the regular expression
@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(message):
	pass


dp = Dispatcher(Bot(telegram_bot_token))

@dp.message_handler(commands="start", "write todo", "search stock")
async def start(message: types.Message):
    start_buttons = ["weather", "stocks", "pull requests"]
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.add(*start_buttons)
    await message.answer(f"hey, im ur bot! \nhere is weather trendings:{get_weather}", reply_markup=keyboard)
"""

    
def main():
    bot.infinity_polling()



if __name__ == "__main__":
    main()
