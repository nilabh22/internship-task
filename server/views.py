from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipient
from django.core.mail import send_mail
from django.db.models.signals import post_save
import requests,json
def main_script(*args, **kwargs):
    users = Recipient.objects.all()
    last_user = users[len(users)-1]
    temp = get_temp(last_user.city)
    emo_G = get_emo_G(temp)
    send_mail(
        subject=f"Hi {last_user.name}, interested in our services",
        message=f"Dear {last_user.name}, The temperature in {last_user.city} is {temp} Kelvin {emo_G}",
        from_email="sahunilabh@gmail.com",
        recipient_list=[last_user.mail],
        fail_silently=False
        )
    return HttpResponse("Success")

def get_temp(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a0b93b673a0c898e5eaf8643efd860a2'
    r = requests.get(url,allow_redirects=True)

    open('weather.json', 'wb+').write(r.content)
    with open('weather.json') as json_file:
        data = json.load(json_file)

    return data['main']['temp']

def get_emo_G(temp):
    if temp < 283.15:
        return '\U0001F976'
    if temp >= 283.15 and temp < 298.15:
        return '\U0001F973'
    if temp >= 298.15 and temp < 308.15:
        return '\U0001F975'
    if temp >= 308.15:
        return '\U0001F92F'

post_save.connect(main_script,sender=Recipient)