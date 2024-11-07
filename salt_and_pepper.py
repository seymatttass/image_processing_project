import cv2
import numpy as np
import random

def add_salt_and_pepper_noise(image_path, salt_prob, pepper_prob):
    # Görüntüyü yükle
    img = cv2.imread(image_path)
    
    # Görüntünün boyutlarını al
    height, width, channels = img.shape
    
    # Gürültü eklenmiş görüntünün kopyasını oluştur
    noisy_img = img.copy()
    
    # Salt gürültüsü (beyaz pikseller)
    num_salt = int(salt_prob * height * width)
    for _ in range(num_salt):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        noisy_img[y, x] = [255, 255, 255]  # Beyaz piksel
    
    # Pepper gürültüsü (siyah pikseller)
    num_pepper = int(pepper_prob * height * width)
    for _ in range(num_pepper):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        noisy_img[y, x] = [0, 0, 0]  # Siyah piksel
    
    # Gürültü eklenmiş görüntüyü göster
    cv2.imshow("Noisy Image", noisy_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek kullanım
add_salt_and_pepper_noise("example.jpg", 0.02, 0.02)  # %2 salt ve %2 pepper gürültüsü eklenmiş örnek
