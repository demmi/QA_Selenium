import requests
import time


def get_weather(city, lang):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=15577aa2f56cced3d348d73d949e3235&lang={lang}&units=metric'
    r = requests.get(url).json()
    return f'Сейчас в {r["name"]} {r["main"]["temp"]} градусов\n' \
           f'Осадки: {r["weather"][0]["description"]}\n' \
           f'Влажность: {r["main"]["humidity"]}%\n' \
           f'Ветер: {r["wind"]["speed"]} м/с\n' \
           f'Восход солнца: {time.strftime("%H:%M", time.localtime(r["sys"]["sunrise"]))}, закат: {time.strftime("%H:%M", time.localtime(r["sys"]["sunset"]))}'


print(get_weather('Vilnius', 'ru'))
