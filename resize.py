import cv2
import os


overlay = cv2.imread('overlay/overlay.png')
overlay = cv2.resize(overlay,(1280,720))
cv2.imwrite("overlay/overlay.png", overlay)

path_modes = 'overlay/modes'
list_modes = os.listdir(path_modes)

for mode in list_modes:

    img = cv2.imread(f'{path_modes}/{mode}')
    img = cv2.resize(img,(323,480))#414,633
    cv2.imwrite(f'{path_modes}/{mode}', img)

path_worker_img = 'data/worker_id_img'
list_worker_imgs = os.listdir(path_worker_img)

for cur_img in list_worker_imgs:

    img = cv2.imread(f'{path_worker_img}/{cur_img}')
    img = cv2.resize(img,(216,216))#414,633
    cv2.imwrite(f'{path_worker_img}/{cur_img}', img)
