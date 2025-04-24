"""
Üzüm Yaprağı Hastalık Tespiti - Ana Program

Bu program, üzüm yapraklarında hastalık tespiti yapmak için görüntü işleme tekniklerini kullanır.
Ana program akışını ve sistem başlatma işlemlerini içerir.
"""

import os
import sys
from utils import show_image, apply_threshold
from dataset_loader import load_and_preprocess_images

def main():
    """
    Ana program akışını yöneten fonksiyon.
    """
    # Örnek görüntülerin bulunduğu klasör
    image_folder = "./sample_images"
    
    # Klasörün varlığını kontrol et
    if not os.path.exists(image_folder):
        print(f"HATA: {image_folder} klasörü bulunamadı!")
        print("Lütfen önce sample_images klasörünü oluşturun ve içine örnek görüntüler ekleyin.")
        sys.exit(1)
    
    # Görüntüleri yükle ve ön işle
    print("Görüntüler yükleniyor ve ön işleniyor...")
    processed_images = load_and_preprocess_images(image_folder)
    
    if not processed_images:
        print("HATA: İşlenecek görüntü bulunamadı!")
        print("Lütfen sample_images klasörüne .jpg veya .png uzantılı görüntüler ekleyin.")
        sys.exit(1)
    
    # İlk görüntüyü göster
    print("\nİlk görüntü gösteriliyor...")
    show_image("Orijinal Görüntü", processed_images[0])
    
    # İlk görüntüye eşikleme uygula ve göster
    print("Eşikleme uygulanıyor...")
    threshold_img = apply_threshold(processed_images[0], thresh_value=128)
    show_image("Eşiklenmiş Görüntü", threshold_img)

if __name__ == "__main__":
    main() 