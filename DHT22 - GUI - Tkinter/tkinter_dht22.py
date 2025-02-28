from tkinter import *
from Adafruit_DHT import *
import time
from threading import Thread

#  khai báo dht22
dht22_pin = 4

# hm đọc giá trị t dht22
def read_dht22():
    while True:
        humidity, temperature = read_retry(DHT22, dht22_pin)
        if humidity is not None and temperature is not None:
            print(f"Nhiệt độ: {temperature:.1f}°C  -  Độ ẩm: {humidity:.1f}%")

            temp_label_val.config(text = f"{temperature:.1f}°C")
            humi_label_val.config(text = f"{humidity:.1f}%")
        else:
            temp_label.config(text="--err--")
            humi_label.config(text="--err--")
        time.sleep(2)

window = Tk()
window.title("DHT22 - GUI - Tkinter")
window.geometry("400x170")

label = Label(text = "Đọc giá trị cảm biến DHT22", fg = "red", font = ("Arial", 20))
label.grid(column = 0, row = 0, padx = 35, pady = 10, columnspan=2)

# khung hiển thị nhiệt độ
temp_label = Label(text = "Nhiệt độ:", font = ("Arial", 17))
temp_label.grid(column = 0, row = 1, padx = 15, pady = 10, sticky = "e")

temp_label_val = Label(text = "--", font = ("Arial", 17), width = 8, relief="solid")
temp_label_val.grid(column = 1, row = 1, pady = 10, sticky = "w")

# khung hiển thị độ ẩm
humi_label = Label(text = "Độ ẩm:", font = ("Arial", 17))
humi_label.grid(column = 0, row = 2, padx= 15, pady = 10, sticky = "e")

humi_label_val = Label(text = "--", font = ("Arial", 17), width = 8, relief="solid")
humi_label_val.grid(column = 1, row = 2, pady = 10, sticky = "w")

# tao luong cho ham doc gia tri dht22
read_dht22_threading = Thread(target = read_dht22, daemon = True)
read_dht22_threading.start()

window.mainloop()