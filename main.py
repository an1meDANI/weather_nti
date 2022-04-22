import telebot
import cfg
import requests
import json

def weather(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = int(data['main']['temp'] - 273.15)
        return temp
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather1(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        pressure = int(data['main']['pressure'] * 0.75)
        return pressure
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather2(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        humidity = int(data['main']['humidity'])
        return humidity
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather3(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        feels_like = int(data['main']['feels_like'] - 273.15)
        return feels_like
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather4(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        visibility = int(data['visibility'])
        return visibility
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather5(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        speed = int(data['wind']['speed'])
        return speed
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather6(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        deg = int(data['wind']['deg'])
        return deg
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

def weather7(city, api_key):
    url_b = "https://api.openweathermap.org/data/2.5/weather?"
    url = url_b + "q=" + city + "&appid=" + api_key
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        all = int(data['clouds']['all'])
        return all
    else:
        print("ERROR")
bot = telebot.TeleBot(cfg.telegram_api)

@bot.message_handler(commands=['start'])
def start_message(message):
    msg = bot.reply_to(message, "Привет, сейчас я покажу тебе актуальную погоду на сегодня.")
    bot.send_message(message.chat.id, "Введите название города:")
    bot.register_next_step_handler(msg, print_weather)
def print_weather(message):
    city = message.text
    temp = weather(city, cfg.weather_api)
    pressure = weather1(city, cfg.weather_api)
    humidity = weather2(city, cfg.weather_api)
    feels_like = weather3(city, cfg.weather_api)
    visibility = weather4(city, cfg.weather_api)
    speed = weather5(city, cfg.weather_api)
    deg = weather6(city, cfg.weather_api)
    all = weather7(city, cfg.weather_api)
    msg = bot.reply_to(message, f"Температура: {temp}°C\n"
                                f"Давление: {pressure} мм рт.ст.\n"
                                f"Влажность: {humidity}%\n"
                                f"По ощущениям: {feels_like}°C\n"
                                f"Атмосферная видимость: {visibility} км\n"
                                f"Скорость ветра: {speed} м/с\n"
                                f"Направление ветра: {deg}°\n"
                                f"Облачность: {all}%\n")
    bot.send_message(message.chat.id, "Введите название города:")
    bot.register_next_step_handler(msg, print_weather)
bot.polling()