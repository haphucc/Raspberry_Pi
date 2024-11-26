from picamera2 import Picamera2
import os
from datetime import datetime
import time

def capture_image():
    picam2 = Picamera2()
    
    # Create preview configuration
    config = picam2.create_preview_configuration(main={"format": "RGB888"})
    picam2.configure(config)
    
    # Thiết lập giá trị AWB gains
    picam2.set_controls({"AwbEnable": False})  # Tắt tự động cân bằng trắng
    picam2.set_controls({"ColourGains": (1.50, 1.65)})  # Thiết lập AWB gains
    
    # Start the camera
    picam2.start()
    
    
    # Create save directory
    save_directory = '/home/pi/Desktop/camera_images'
    os.makedirs(save_directory, exist_ok=True)    
    
    # Capture image
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{save_directory}/image_{timestamp}.jpg"
    
    # Wait for camera to stabilize
    time.sleep(3)
    
    # Capture the image
    picam2.capture_file(filename)    
    print(f"Đã chụp và lưu ảnh: {filename}")
    
    # Stop the camera
    picam2.stop()

if __name__ == "__main__":
    capture_image()