"""
YOLOv5 Entegrasyon Modülü

Bu modül, YOLOv5 nesne tespit modelini kullanarak bitki hastalıklarını tespit eder.
Ultralytics YOLOv5 modelini kullanır ve görüntü üzerinde hastalık tespiti yapar.
"""

import os
import sys
import torch
import matplotlib.pyplot as plt
from pathlib import Path

# YOLOv5 reposunu klonla ve gerekli bağımlılıkları yükle
def setup_yolov5():
    """
    YOLOv5 modelini ve gerekli bağımlılıkları kurar.
    """
    # YOLOv5 reposunu klonla
    if not os.path.exists('yolov5'):
        os.system('git clone https://github.com/ultralytics/yolov5')
        os.system('pip install -r yolov5/requirements.txt')
    
    # YOLOv5'i Python path'ine ekle
    yolov5_path = str(Path('yolov5').absolute())
    if yolov5_path not in sys.path:
        sys.path.append(yolov5_path)

def detect(image_path, conf_thres=0.25):
    """
    Verilen görüntüde hastalık tespiti yapar.
    
    Args:
        image_path (str): Tespit yapılacak görüntünün dosya yolu
        conf_thres (float): Güven eşiği (varsayılan: 0.25)
    
    Returns:
        tuple: (İşlenmiş görüntü, tespit sonuçları)
    """
    # YOLOv5 modelini yükle
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    
    # Model parametrelerini ayarla
    model.conf = conf_thres  # Güven eşiği
    model.iou = 0.45  # IoU eşiği
    
    # Görüntüyü yükle ve tespit yap
    results = model(image_path)
    
    # Sonuçları görselleştir
    results.show()
    
    return results

def main():
    """
    Test fonksiyonu
    """
    # YOLOv5 kurulumunu yap
    setup_yolov5()
    
    # Test görüntüsü üzerinde tespit yap
    test_image = "../sample_images/test.jpg"  # Örnek görüntü yolu
    if os.path.exists(test_image):
        results = detect(test_image)
        print("Tespit tamamlandı!")
    else:
        print(f"HATA: {test_image} bulunamadı!")

if __name__ == "__main__":
    main() 