"""
Veri Seti Yükleme ve İşleme Modülü

Bu modül, üzüm yaprağı görüntülerinin veri setini yükler ve ön işlemeleri gerçekleştirir.
Veri setinin organize edilmesi ve yüklenmesi için gerekli fonksiyonları içerir.
"""

import os
import numpy as np
import cv2
from PIL import Image

def load_and_preprocess_images(image_folder):
    """
    Belirtilen klasördeki görüntüleri yükler ve ön işleme uygular.
    
    Args:
        image_folder (str): Görüntülerin bulunduğu klasör yolu
        
    Returns:
        list: İşlenmiş görüntülerin listesi (numpy array'ler)
    """
    # İşlenmiş görüntüleri tutacak liste
    processed_images = []
    
    # Desteklenen görüntü uzantıları
    valid_extensions = ('.jpg', '.jpeg', '.png')
    
    # Klasördeki tüm dosyaları tara
    for filename in os.listdir(image_folder):
        # Dosya uzantısını kontrol et
        if filename.lower().endswith(valid_extensions):
            # Tam dosya yolunu oluştur
            image_path = os.path.join(image_folder, filename)
            
            try:
                # Görüntüyü OpenCV ile oku
                image = cv2.imread(image_path)
                
                if image is None:
                    print(f"Uyarı: {filename} dosyası okunamadı, atlanıyor.")
                    continue
                
                # Görüntüyü 256x256 boyutuna yeniden boyutlandır
                image = cv2.resize(image, (256, 256))
                
                # Gri tonlamaya çevir
                image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                
                # 0-1 arası normalize et ve float32'ye dönüştür
                image = image.astype(np.float32) / 255.0
                
                # İşlenmiş görüntüyü listeye ekle
                processed_images.append(image)
                
            except Exception as e:
                print(f"Hata: {filename} dosyası işlenirken hata oluştu: {str(e)}")
                continue
    
    return processed_images

def load_dataset(data_path):
    """
    Veri setini yükler ve organize eder.
    
    Args:
        data_path: Veri setinin bulunduğu dizin yolu
    
    Returns:
        X: Görüntü verileri
        y: Etiketler
    """
    # TODO: Veri seti yükleme işlemleri eklenecek
    pass

def split_dataset(X, y, test_size=0.2):
    """
    Veri setini eğitim ve test setlerine ayırır.
    
    Args:
        X: Görüntü verileri
        y: Etiketler
        test_size: Test seti oranı
    
    Returns:
        Eğitim ve test setleri
    """
    # TODO: Veri seti bölme işlemleri eklenecek
    pass 