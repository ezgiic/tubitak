"""
Görüntü İşleme Yardımcı Fonksiyonları

Bu modül, görüntü işleme için gerekli yardımcı fonksiyonları içerir.
Yaprak görüntülerinin ön işlenmesi ve analizi için kullanılacak fonksiyonlar burada tanımlanır.
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(title, img):
    """
    Görüntüyü matplotlib ile ekranda gösterir.
    
    Args:
        title (str): Görüntünün başlığı
        img (numpy.ndarray): Gösterilecek görüntü (gri veya renkli)
    """
    plt.figure(figsize=(8, 6))
    plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
    plt.axis('off')
    plt.title(title)
    plt.show()

def apply_threshold(img, thresh_value=128):
    """
    Gri tonlamalı görüntüye eşikleme uygular.
    
    Args:
        img (numpy.ndarray): Gri tonlamalı görüntü
        thresh_value (int): Eşik değeri (varsayılan: 128)
        
    Returns:
        numpy.ndarray: İkili (binary) görüntü
    """
    # Görüntünün gri tonlamalı olduğunu kontrol et
    if len(img.shape) != 2:
        raise ValueError("Görüntü gri tonlamalı olmalıdır!")
    
    # Eşikleme uygula
    _, binary_img = cv2.threshold(img, thresh_value, 255, cv2.THRESH_BINARY)
    
    return binary_img

def calculate_histogram(img):
    """
    Gri tonlamalı görüntünün histogramını hesaplar ve çizer.
    
    Args:
        img (numpy.ndarray): Gri tonlamalı görüntü
    """
    # Görüntünün gri tonlamalı olduğunu kontrol et
    if len(img.shape) != 2:
        raise ValueError("Görüntü gri tonlamalı olmalıdır!")
    
    # Histogramı hesapla
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    
    # Histogramı çiz
    plt.figure(figsize=(10, 4))
    plt.plot(hist)
    plt.title('Görüntü Histogramı')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Frekans')
    plt.grid(True)
    plt.show()

def preprocess_image(image):
    """
    Görüntüyü model için hazırlar.
    
    Args:
        image: İşlenecek görüntü (numpy array)
    
    Returns:
        İşlenmiş görüntü
    """
    # TODO: Görüntü ön işleme adımları eklenecek
    pass

def extract_features(image):
    """
    Görüntüden özellik çıkarımı yapar.
    
    Args:
        image: Özellik çıkarılacak görüntü
    
    Returns:
        Çıkarılan özellikler
    """
    # TODO: Özellik çıkarma işlemleri eklenecek
    pass 