from picamera2 import Picamera2
import cv2
from PIL import Image
import ST7735 as TFT
import Adafruit_GPIO.SPI as SPI

# Cấu hình màn hình TFT
WIDTH = 128
HEIGHT = 160
SPEED_HZ = 16000000

# Raspberry Pi configuration
DC = 24
RST = 25
SPI_PORT = 0
SPI_DEVICE = 0

# Hàm hiển thị video
def capture_video_tft():
    # Khởi tạo PiCamera2
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"format": "RGB888", "size": (WIDTH, HEIGHT)})
    picam2.configure(config)
    
    # Thiết lập giá trị AWB gains
    picam2.set_controls({"AwbEnable": False})  # Tắt tự động cân bằng trắng
    picam2.set_controls({"ColourGains": (1.95, 1.80)})  # Thiết lập AWB gains
    
    # Khởi tạo màn hình TFT
    disp = TFT.ST7735(
        DC,
        rst=RST,
        spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=SPEED_HZ)
    )
    disp.begin()
    
    # Bắt đầu camera
    picam2.start()
    
    try:
        while True:
            # Lấy khung hình từ camera
            frame = picam2.capture_array()

            # Chuyển đổi khung hình sang định dạng PIL Image
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)  # Đảm bảo thứ tự kênh
            image = Image.fromarray(frame_rgb)
            
            # Hiển thị lên màn hình TFT
            disp.display(image)
            
            # Hiển thị trên OpenCV để kiểm tra (tùy chọn)
            cv2.imshow("Camera", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # Dừng camera và giải phóng tài nguyên
        picam2.stop()
        cv2.destroyAllWindows()
        print("Video stream stopped.")

if __name__ == "__main__":
    capture_video_tft()
