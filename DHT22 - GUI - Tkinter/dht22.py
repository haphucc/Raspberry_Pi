import Adafruit_DHT
import time

# Cảm biến DHT22 - GUI - Tkinter
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # GPIO4

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    
    if humidity is not None and temperature is not None:
        print(f"Nhiệt độ: {temperature:.1f}°C  -  Độ ẩm: {humidity:.1f}%")
        time.sleep(2)
    else:
        print("Không đọc được dữ liệu từ cảm biến!")
