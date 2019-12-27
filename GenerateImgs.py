import os
import cv2
import numpy as np

np.random.seed(0)

save_dir = 'data/imgs'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

img_num = 100
img_height = 256
img_width = 256

square_size = min(img_height, img_width) // 3
img = np.full((img_height, img_width, 3), 0, dtype=np.uint8)
for i in range(img_num):
    x1 = np.random.randint(img_width - square_size)
    y1 = np.random.randint(img_height - square_size)
    pt1 = (x1, y1)
    pt2 = (x1+square_size, y1+square_size)
    B, G, R = np.random.randint(255), np.random.randint(255), np.random.randint(255)
    cv2.rectangle(img, pt1, pt2, (B, G, R), thickness=-1)
    cv2.imwrite('{}/{:03d}.png'.format(save_dir, i), img)
