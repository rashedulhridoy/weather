from tkinter import *
from tkinter import ttk
import requests 


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ city + "&appid=b1aa196ca97a701d14929fd64b218cc6").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    per_label1.config(text=data ["main"]["pressure"])




win = Tk()
win.title("Weather Bot")
win.config(bg="white")
win.geometry("500x570")

city_name = StringVar()

name_label = Label(win, text="Weather Bot", bg ="white"
                   , font=("Time New Roman", 16, "bold"))

name_label.place(x=25, y=50, height=50, width=450)

list_name = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

com = ttk.Combobox(win, text="Weather Bot", values = list_name
                   , font=("Time New Roman", 15, "bold"), textvariable=city_name)

com.place(x=20, y=120, height=30, width=450)







w_label = Label(win, text="Weather Climate", bg ="white"
                   , font=("Time New Roman", 10))

w_label.place(x=25, y=260, height=50, width=210)

w_label1 = Label(win, text="", bg ="white"
                   , font=("Time New Roman", 10))

w_label1.place(x=250, y=260, height=50, width=210)





wb_label = Label(win, text="Weather Decription", bg ="white"
                   , font=("Time New Roman", 10))

wb_label.place(x=25, y=330, height=50, width=210)



wb_label1 = Label(win, text="", bg ="white"
                   , font=("Time New Roman", 10))

wb_label1.place(x=250, y=330, height=50, width=210)




temp_label = Label(win, text="Temperature", bg ="white"
                   , font=("Time New Roman", 10))

temp_label.place(x=25, y=400, height=50, width=210)




temp_label1 = Label(win, text="", bg ="white"
                   , font=("Time New Roman", 10))

temp_label1.place(x=250, y=400, height=50, width=210)




per_label = Label(win, text="Pressure", bg ="white"
                   , font=("Time New Roman", 10))
per_label.place(x=25, y=470, height=50, width=210)


per_label1 = Label(win, text="", bg ="white"
                   , font=("Time New Roman", 10))

per_label1.place(x=250, y=470, height=50, width=210)




done_button = Button(win, text="Done",font = ("Time New Roman", 20, "bold"), command=data_get)

done_button.place(x=200, y=190, height=50, width=100)



win.mainloop()