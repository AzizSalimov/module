'''
Weather forecast with Python
# By: Ayushi Rawat
# '''
#
# #import the necessary package!
# import requests
#
# #input the city name
# city = input('input the city name')
# print(city)
#
# # or you can also hard-code the value
# # city = 'bhopal'
#
# #Display the message!
# print('Displaying Weater report for: ' + city)
#
# #fetch the weater details
# url = 'https://wttr.in/{}'.format(city)
# res = requests.get(url)
#
# #display the result!
# print(res.text)
#
#
# import tkinter as tk
# from bs4 import BeautifulSoup as bs
# import requests
#
# root = tk.Tk()
# root.geometry('300x400')
# root.title('City Weather Forecast')
#
#
# def forecast():
#     city = e.get()
#     url = 'https://www.weather-forecast.com/locations/' + str(city) + '/forecasts/latest'
#     r = requests.get(url)
#     html_code = bs(r.content)
#     day = html_code.find('div', attrs={'class': 'b-forecast__table-days-name'}).get_text()
#     date = html_code.find('div', attrs={'class': 'b-forecast__table-days-date'}).get_text()
#     t = html_code.find_all('span', attrs={'class': 'b-forecast__table-value'})
#     time = [i.get_text() for i in t[0:3]]
#     w = html_code.find('tr', attrs={'class': 'b-forecast__table-summary js-summary'})
#     w1 = w.find_all('div', attrs={'class': 'b-forecast__text-limit'})
#     weather = [i.get_text() for i in w1[0:3]]
#     t = html_code.find_all('span', attrs={'class': 'temp b-forecast__table-value'})
#     temprature = [i.get_text() for i in t[0:3]]
#     mt = html_code.find('tr', attrs={'class': 'b-forecast__table-min-temperature js-min-temp'})
#     mt1 = mt.find_all('span', attrs={'class': 'temp b-forecast__table-value'})
#     min_temprature = [i.get_text() for i in mt1[0:3]]
#
#     day_label = tk.Label(root, text=str(day) + str(date))
#     day_label.pack()
#
#     frame1 = tk.Frame(root)
#     frame1.pack()
#
#     l2 = tk.Label(frame1, text='High')
#     l2.grid(row=1, column=0)
#     l3 = tk.Label(frame1, text='Low')
#     l3.grid(row=2, column=0)
#     l4 = tk.Label(frame1, text='Weather')
#     l4.grid(row=3, column=0)
#
#     for i in range(len(time)):
#         time_label = tk.Label(frame1, text=time[i])
#         time_label.grid(row=0, column=i + 1)
#
#         temprature_label = tk.Label(frame1, text=temprature[i])
#         temprature_label.grid(row=1, column=i + 1)
#
#         min_temprature_label = tk.Label(frame1, text=min_temprature[i])
#         min_temprature_label.grid(row=2, column=i + 1)
#
#         weather_label = tk.Label(frame1, text=weather[i])
#         weather_label.grid(row=3, column=i + 1)
#
#     def reset():
#         day_label.config(text='')
#         frame1.destroy()
#         btn1.destroy()
#         e.delete(0, 'end')
#
#     btn1 = tk.Button(root, text='Delete', command=reset)
#     btn1.pack()
#
#
# l = tk.Label(root, text='City Weather Forecast')
# l.pack(pady=10)
#
# l1 = tk.Label(root, text='Enter City Name')
# l1.pack()
#
# frame = tk.Frame(root)
# frame.pack()
#
# e = tk.Entry(frame, width=20, font=('20'))
# e.grid(row=0, column=0)
#
# btn = tk.Button(frame, text='Search', padx=10, command=forecast)
# btn.grid(row=0, column=1)
#
# root.mainloop()


import tkinter as tk
import requests
import time


def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(
        max_temp) + "°C" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text=final_info)
    label2.config(text=final_data)


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