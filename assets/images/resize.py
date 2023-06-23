import cv2
import os
import sys
sys.path.append(os.getcwd())

image_root = 'assets\images\\fulls'
image_paths = [os.path.join(image_root,i) for i in os.listdir(image_root)]

for image_path in image_paths:
    img = cv2.imread(image_path)
    h,w,c = img.shape
    print(h,w,c)
    priority = h if h>w else w
    print(priority)
    rotio_full = 1024.0/priority
    img_full = cv2.resize(img,(int(rotio_full*w),int(rotio_full*h)),interpolation=cv2.INTER_AREA)
    cv2.imwrite(image_path,img_full)

    rotio_thumb =  360.0/priority
    img_thumb = cv2.resize(img,(int(rotio_thumb*w),int(rotio_thumb*h)),interpolation=cv2.INTER_AREA)
    cv2.imwrite(image_path.replace("fulls","thumbs"),img_thumb)
