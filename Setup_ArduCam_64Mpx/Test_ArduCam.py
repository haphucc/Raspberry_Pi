import cv2
import numpy as np
import subprocess

# Khởi động luồng video từ libcamera
command = [
    "libcamera-vid",
    "--nopreview",
    "--inline",
    "-t", "0",
    "--width", "640",
    "--height", "480",
    "-o", "-",
    "--codec", "mjpeg"
]

# Mở luồng video
process = subprocess.Popen(command, stdout=subprocess.PIPE, bufsize=10**6)

try:
    print("Nhấn 'q' để thoát.")
    buffer = b""
    while True:
        bytes_data = process.stdout.read(1024)
        if not bytes_data:
            break
        buffer += bytes_data

        start_marker = buffer.find(b'\xff\xd8')
        end_marker = buffer.find(b'\xff\xd9')
        if start_marker != -1 and end_marker != -1:
            frame_data = buffer[start_marker:end_marker+2]
            buffer = buffer[end_marker+2:]

            frame = cv2.imdecode(np.frombuffer(frame_data, np.uint8), cv2.IMREAD_COLOR)
            if frame is None:
                continue

            # Hiển thị khung hình duy nhất
            cv2.imshow("Arducam 64MP Stream", frame)

            # Nhấn 'q' để thoát
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
finally:
    process.terminate()
    cv2.destroyAllWindows()

