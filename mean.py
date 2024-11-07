import cv2
import numpy as np

def mean(image, kernel_size):
    height, width, channels = image.shape
    filtered_img = np.zeros((height, width, channels), dtype=np.uint8)
    k = kernel_size // 2
    for y in range(k, height - k):
        for x in range(k, width - k):
            for c in range(channels):
                neighborhood = image[y - k:y + k + 1, x - k:x + k + 1, c]
                mean_value = np.mean(neighborhood)
                filtered_img[y, x, c] = mean_value
    
    return filtered_img

image_path = "gurultulu_foto.jpg"  
noisy_img = cv2.imread(image_path)

kernel_size = 3  # Kernel boyutu 3x3
filtered_img = mean(noisy_img, kernel_size)

cv2.imshow("Temizzz", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
