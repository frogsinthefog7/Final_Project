"""from picamera2 import Picamera2, Preview
import time

folder_path = "/home/mads/'Final_Project Git'/Final_Project/'Photo Gallary'"
os.makedirs(folder_path, exist_ok=True)

file_path = os.path.join(folder_path, "cute.jpg")

pictures_taken = 0

picam2 = Picamera2()
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
picam2.start()
time.sleep(2)
picam2.capture_file("cute.jpg")"""