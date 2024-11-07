import cv2
import numpy as np
import math

def rotate_image(image_path, angle):
    image_path = "/Users/o/Desktop/ip project/assets/img.jpg"
    img = cv2.imread(image_path)
    
    height, width = img.shape[:2]
    
    angle_rad = math.radians(angle)
    
    #dönüşüm matrisini kullandık
    new_width = int(abs(width * math.cos(angle_rad)) + abs(height * math.sin(angle_rad)))
    new_height = int(abs(width * math.sin(angle_rad)) + abs(height * math.cos(angle_rad)))
    
    rotated_img = np.zeros((new_height, new_width, 3), dtype=np.uint8)
    
    center_x = width / 2
    center_y = height / 2
    
    for x in range(new_width):
        for y in range(new_height):
            new_x = int((x - new_width / 2) * math.cos(angle_rad) - (y - new_height / 2) * math.sin(angle_rad) + center_x)
            new_y = int((x - new_width / 2) * math.sin(angle_rad) + (y - new_height / 2) * math.cos(angle_rad) + center_y)
            
            if 0 <= new_x < width and 0 <= new_y < height:
                rotated_img[y, x] = img[new_y, new_x]
    
    cv2.imshow("Result: ", rotated_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

rotate_image("/Users/o/Desktop/ip project/assets/img.jpg", 45) 
