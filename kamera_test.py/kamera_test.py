import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Kamera açılamadı")
    exit()

print("✅ Kamera açıldı")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Görüntü alınamadı")
        break

    cv2.imshow("Kamera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not cap.isOpened():
    print("❌ Kamera açılamadı")
    exit()

print("✅ Kamera açıldı - pencere geliyor")

cv2.namedWindow("CANLI KAMERA", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Frame alınamadı")
        break

    cv2.imshow("CANLI KAMERA", frame)

    # pencerenin donmaması için
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print("📷 Kamera kapatıldı")

