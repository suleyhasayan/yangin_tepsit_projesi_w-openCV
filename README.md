# 🔥 Yangın Tespit Projesi (OpenCV ile)

Bu proje, **Python** ve **OpenCV** kütüphanesini kullanarak gerçek zamanlı görüntü işleme teknikleriyle yangın ve ateş tespiti yapmayı amaçlamaktadır. Kamera görüntüsü veya video dosyaları üzerinden renk ve hareket analizi yaparak olası yangın durumlarını algılar.

## 🚀 Özellikler

* **Gerçek Zamanlı Tespit:** Webcam üzerinden anlık görüntü işleme.
* **Renk Analizi:** Yangın renk uzaylarına (HSV) dayalı hassas algılama.
* **Hafif ve Hızlı:** Düşük sistem gereksinimleriyle çalışabilen optimize edilmiş kod yapısı.
* **Görüntü İşleme:** Gürültü giderme ve maskeleme teknikleri ile hatalı tespitlerin azaltılması.

## 🛠 Gereksinimler

Projeyi çalıştırmak için bilgisayarınızda **Python 3.x** yüklü olmalıdır. Ayrıca aşağıdaki kütüphanelere ihtiyacınız vardır:

* OpenCV (`cv2`)
* NumPy

## 💻 Kurulum

Projeyi yerel bilgisayarınıza klonlamak ve gerekli bağımlılıkları yüklemek için terminal veya komut satırında aşağıdaki adımları izleyin:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/suleyhasayan/yangin_tepsit_projesi_w-openCV.git](https://github.com/suleyhasayan/yangin_tepsit_projesi_w-openCV.git)
    cd yangin_tepsit_projesi_w-openCV
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install opencv-python numpy
    ```

## ▶️ Kullanım

Kurulum tamamlandıktan sonra projeyi çalıştırmak için ana Python dosyasını başlatın (Dosya adı projenizdeki `.py` uzantılı ana dosyadır, örneğin `main.py` veya `yangin_tespit.py` olabilir):

```bash
python main.py
