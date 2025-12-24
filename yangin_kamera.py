import cv2
import numpy as np
import winsound
import os
import time
from datetime import datetime



CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

MIN_FIRE_AREA = 1500         
FIRE_CONFIRM_FRAMES = 6       
ALARM_COOLDOWN = 4            

VIDEO_FPS = 20.0



def alarm_cal():
    winsound.Beep(1200, 700)



os.makedirs("reports", exist_ok=True)
os.makedirs("videos", exist_ok=True)



def write_report(start_time, frame_count):
    with open(
        f"reports/fire_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
        "w",
        encoding="utf-8"
    ) as f:
        f.write("YANGIN ALGILAMA RAPORU\n")
        f.write("-" * 30 + "\n")
        f.write(f"Başlangıç Zamanı : {start_time}\n")
        f.write(f"Bitiş Zamanı     : {datetime.now()}\n")
        f.write(f"Kayıtlı Kare     : {frame_count}\n")



cap = cv2.VideoCapture(CAMERA_INDEX, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

if not cap.isOpened():
    print("❌ Kamera açılamadı")
    exit()

print("✅ Kamera açıldı | Q: Çık | S: Alarm Sustur | R: Alarm Aç")



fourcc = cv2.VideoWriter_fourcc(*'XVID')
video_writer = None
recording = False


fire_frame_counter = 0
fire_active = False
alarm_enabled = True
last_alarm_time = 0

fire_start_time = None
recorded_frames = 0



while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT))

    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_fire = np.array([0, 120, 120])
    upper_fire = np.array([35, 255, 255])

    mask = cv2.inRange(hsv, lower_fire, upper_fire)

    
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.dilate(mask, kernel, iterations=2)

   
    contours, _ = cv2.findContours(
        mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    fire_found_this_frame = False

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > MIN_FIRE_AREA:
            x, y, w, h = cv2.boundingRect(cnt)
            ratio = w / float(h)

            if 0.2 < ratio < 4.0:
                fire_found_this_frame = True

                cv2.rectangle(
                    frame, (x, y), (x + w, y + h),
                    (0, 0, 255), 2
                )

                cv2.putText(
                    frame,
                    "YANGIN ALGILANDI",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,
                    (0, 0, 255),
                    2
                )

   
    if fire_found_this_frame:
        fire_frame_counter += 1
    else:
        fire_frame_counter = 0

   
    if fire_frame_counter >= FIRE_CONFIRM_FRAMES and not fire_active:
        fire_active = True
        fire_start_time = datetime.now()
        recorded_frames = 0

        if alarm_enabled and time.time() - last_alarm_time > ALARM_COOLDOWN:
            alarm_cal()
            last_alarm_time = time.time()

        video_writer = cv2.VideoWriter(
            f"videos/fire_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi",
            fourcc,
            VIDEO_FPS,
            (FRAME_WIDTH, FRAME_HEIGHT)
        )
        recording = True

   
    if recording:
        video_writer.write(frame)
        recorded_frames += 1

  
    if fire_active and fire_frame_counter == 0:
        fire_active = False
        recording = False

        if video_writer:
            video_writer.release()
            video_writer = None

        write_report(fire_start_time, recorded_frames)

  
    cv2.imshow("GELISMIS YANGIN ALGILAMA SISTEMI", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        alarm_enabled = False
        print("🔕 Alarm susturuldu")
    elif key == ord("r"):
        alarm_enabled = True
        print("🔔 Alarm aktif")



cap.release()
if video_writer:
    video_writer.release()

cv2.destroyAllWindows()
print("🛑 Sistem kapatıldı")
