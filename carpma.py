import cv2
import numpy as np

def multiply(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    
    if img1.shape != img2.shape:
        raise ValueError("Görüntülerin boyutları aynı olmalıdır.")
    
    height, width, channels = img1.shape
    
    multiplied = np.zeros((height, width, channels), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                multiplied_value = int(img1[y, x, c]) * int(img2[y, x, c])
                if multiplied_value > 255:
                    multiplied_value = 255
                multiplied[y, x, c] = multiplied_value
    
    cv2.imshow("Result: ", multiplied)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Örnek kullanım
multiply("image1.jpg", "image2.jpg")
