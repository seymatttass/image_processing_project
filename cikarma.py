import cv2
import numpy as np

def subtract_images(image_path1, image_path2):
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    
    if img1.shape != img2.shape:
        raise ValueError("Görüntülerin boyutları aynı olmalıdır.")
    
    height, width, channels = img1.shape
    
    difference = np.zeros((height, width, channels), dtype=np.uint8)
    
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                difference[y, x, c] = abs(int(img1[y, x, c]) - int(img2[y, x, c]))
    
    cv2.imshow("Result: ", difference)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

subtract_images("img.jpg", "img.jpg")
