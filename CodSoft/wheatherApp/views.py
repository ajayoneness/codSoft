from django.shortcuts import render
import requests


def weather(request):
    api_key = 'bf784afb3b9139133fb9f1fce83cda4c'
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    data={}
    location = ''
    message=''
    if request.POST:
        location = request.POST['place']

        params = {"q": location, "appid": api_key, "units": "metric"}
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()
            data=data
            message=''
        except requests.exceptions.RequestException as e:
            message = e

        print(data)
    return render(request,'weather.html',{'data':data,'loc':location,"message":message})