from tkinter import * 
from tkinter import messagebox 
import time

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())
        
    except:
        print("Please input correct values")
    
    while temp > -1:
        #divmod(first_value = temp // 60, second_value = temp % 60)
        minutes, seconds = divmod(temp,60)
        hours = 00
        if minutes > 60:
            hours, minutes = divmod(minutes, 60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(minutes))
        second.set("{00:2d}".format(seconds))
        window.update()
        time.sleep(1)
        if temp == 00:
            messagebox.showinfo("Time over", "Time is up!")
        temp -= 1





window = Tk()
window.geometry("250x200")
window.title("Stop watch")
window.configure(background = "white")
# declaring the object of StringVar() class

hour = StringVar()
minute = StringVar()
second = StringVar()


#setting default values for all 3 objects
hour.set( "00")
minute.set(" 00")
second.set( "00")


hour_entry = Entry(window, textvariable = hour, width = 3, font = ("times", 30))
minute_entry = Entry(window, textvariable = minute, width = 3, font = ("times", 30))
second_entry = Entry(window, textvariable = second, width = 3, font = ("times", 30))

set_conutdon = Button(window, text = "Set time countdown", command = submit)

hour_entry.grid(row = 1, column = 1, pady = 30, padx = 20)
minute_entry.grid(row = 1, column = 2)
second_entry.grid(row = 1, column = 3, padx = 20)
set_conutdon.place(x = 50, y = 120)

window.mainloop()