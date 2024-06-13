'''
import requests
import json

city = input("Enter the name of city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=e8343a6f55fa485f8c472535241206&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic["current"]["temp_c"])
print(wdic["current"]["humidity"])

'''

import requests
import json
import PySimpleGUI as sg

layout = [
    [sg.Text("Enter the name of city: "), sg.InputText(key='-CITY-'), sg.Button('Get Weather')],
    [sg.Text("Temperature (°C):"), sg.Text(size=(10, 1), key='-TEMP-C')],
    [sg.Text("Temperature (°F):"), sg.Text(size=(10, 1), key='-TEMP-F')],
    [sg.Text("Wind Speed:"), sg.Text(size=(10,1), key='-WindSpeed-')],
    [sg.Text("Humidity:"), sg.Text(size=(10, 1), key='-HUMIDITY-')]
]

window = sg.Window('Weather App', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Get Weather':
        city = values['-CITY-']
        url = f"https://api.weatherapi.com/v1/current.json?key=e8343a6f55fa485f8c472535241206&q={city}"
        r = requests.get(url)
        wdic = json.loads(r.text)
        temperature_C = wdic["current"]["temp_c"]
        temperature_F = wdic["current"]["temp_f"]
        windspeed = wdic["current"]["wind_mph"]
        humidity = wdic["current"]["humidity"]
        window['-TEMP-C'].update(temperature_C)
        window['-TEMP-F'].update(temperature_F)
        window['-WindSpeed-'].update(windspeed)
        window['-HUMIDITY-'].update(humidity)

window.close()
