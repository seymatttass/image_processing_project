import cv2
import numpy as np

def apply_median_filter(image, kernel_size):
    # Görüntünün boyutlarını al
    height, width, channels = image.shape
    
    # Filtrelenmiş görüntü için boş bir görüntü oluştur
    filtered_img = np.zeros((height, width, channels), dtype=np.uint8)
    
    # Kernel yarıçapını hesapla
    k = kernel_size // 2
    
    # Görüntü sınırlarını kontrol ederek median filtresini uygula
    for y in range(k, height - k):
        for x in range(k, width - k):
            for c in range(channels):
                # Kernel altındaki piksellerin medyanını hesapla
                neighborhood = image[y - k:y + k + 1, x - k:x + k + 1, c]
                median_value = np.median(neighborhood)
                filtered_img[y, x, c] = median_value
    
    return filtered_img

# Örnek kullanım
image_path = "example_noisy.jpg"  # Gürültülü bir görüntü
noisy_img = cv2.imread(image_path)

# Median filtresi ile gürültü temizleme
kernel_size = 3  # Kernel boyutu 3x3
filtered_img = apply_median_filter(noisy_img, kernel_size)

# Gürültü temizlenmiş görüntüyü göster
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
