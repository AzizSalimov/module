# import requests
#
# api_key = '30d4741c779ba94c470ca1f63045390a'
#
# user_input = input("Enter city: ")
#
# weather_data = requests.get(
#     f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
#
# if weather_data.json()['cod'] == '404':
#     print("No City Found")
# else:
#     weather = weather_data.json()['weather'][0]['main']
#     temp = round(weather_data.json()['main']['temp'])
#
#     print(f"The weather in {user_input} is: {weather}")
#     print(f"The temperature in {user_input} is: {temp}ºF")


import tkinter as tk
import requests



def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)

    final_info = condition + "\n" + str(temp) + "°C"
    label1.config(text=final_info)



canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()