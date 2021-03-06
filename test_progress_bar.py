#!/usr/bin/env python3.8
import tkinter as tk
from tkinter import ttk
from time import strftime 
import datetime, pytz
mainWindow = tk.Tk()
mainWindow.title("TEST LOOP")
def convert_datetime_timezone(dt, tz1, tz2):
	'''
	dt = 2019-12-18 09:49:31
	'''
	tz1 = pytz.timezone(tz1)
	tz2 = pytz.timezone(tz2)
	
	#format input dt
	dt = datetime.datetime.strptime(dt,"%Y-%m-%d %H:%M:%S")
	dt = tz1.localize(dt)
	dt = dt.astimezone(tz2)
	dt1 = dt.strftime("%H:%M:%S")
	return dt1

def update_progress_bar():
    x = barVar.get()
    if x < 100:
        barVar.set(x+10)
        mainWindow.after(500, update_progress_bar)
    else:
        print("Complete")


def update_clock_label():
    current_dt_hcm_hours = datetime.datetime.now().strftime("%H:%M:%S")
    lb.config(text = current_dt_hcm_hours)
    mainWindow.after(250,update_clock_label)

def update_clock_label2():
    current_dt_hcm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_dt_kst = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Asia/Seoul")
    lb2.config(text = current_dt_kst)
    mainWindow.after(250,update_clock_label2)

def update_clock_label3():
    current_dt_hcm = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    current_dt_sweden = convert_datetime_timezone(current_dt_hcm,"Asia/Ho_Chi_Minh","Europe/Stockholm")
    lb3.config(text = current_dt_sweden)
    mainWindow.after(250,update_clock_label3)

barVar = tk.DoubleVar()
barVar.set(0)
bar = ttk.Progressbar(mainWindow, length=200, style='black.Horizontal.TProgressbar', variable=barVar, mode='determinate')


bar.grid(row=1, column=0)
button= tk.Button(mainWindow, text='Click', command=update_progress_bar)
button.grid(row=0, column=0)

lb = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'purple', foreground = 'white')
lb.grid(row=2, column = 0)
lb2 = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'blue', foreground = 'white')
lb2.grid(row=3, column = 0)
lb3 = tk.Label(mainWindow, font = ('Consolas', 40, 'bold'), background = 'green', foreground = 'white')
lb3.grid(row=4, column = 0)
#loop1
update_clock_label()

#loop2
update_clock_label2()

#loop3
update_clock_label3()

mainWindow.mainloop()