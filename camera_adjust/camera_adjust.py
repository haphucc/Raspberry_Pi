from picamera2 import Picamera2
import cv2

def adjust_gains():
    # Khởi tạo camera
    picam2 = Picamera2()
    config = picam2.create_preview_configuration(main={"format": "RGB888"})
    picam2.configure(config)

    # Tắt tự động cân bằng trắng
    picam2.set_controls({"AwbEnable": False})

    # Bắt đầu camera
    picam2.start()
    
    print("Nhấn 'q' để thoát, 'u/d' để điều chỉnh Red_gain, 'i/k' để điều chỉnh Blue_gain...")
    red_gain = 1.50  # Giá trị khởi đầu cho Red_gain
    blue_gain = 1.65  # Giá trị khởi đầu cho Blue_gain

    while True:
        # Cập nhật giá trị ColourGains
        picam2.set_controls({"ColourGains": (red_gain, blue_gain)})

        # Lấy khung hình từ camera
        frame = picam2.capture_array()

        # Hiển thị giá trị trên khung hình
        cv2.putText(frame, f"Red_gain: {red_gain:.2f}, Blue_gain: {blue_gain:.2f}",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.imshow("Camera", frame)
        
        # Kiểm tra phím nhấn
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):  # Nhấn 'q' để thoát
            break
        elif key == ord('s'):  # Nhấn 'u' để tăng Red_gain
            red_gain += 0.05
        elif key == ord('d'):  # Nhấn 'd' để giảm Red_gain
            red_gain = max(0.0, red_gain - 0.05)  # Không giảm thấp hơn 0
        elif key == ord('j'):  # Nhấn 'i' để tăng Blue_gain
            blue_gain += 0.05
        elif key == ord('k'):  # Nhấn 'k' để giảm Blue_gain
            blue_gain = max(0.0, blue_gain - 0.05)  # Không giảm thấp hơn 0

    # Dừng camera và đóng cửa sổ hiển thị
    picam2.stop()
    cv2.destroyAllWindows()
    print("Video stream đã dừng.")

if __name__ == "__main__":
    adjust_gains()
