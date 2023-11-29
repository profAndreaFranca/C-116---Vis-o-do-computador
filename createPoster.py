import cv2
import numpy as np
img = cv2.imread ("./poster.jpg")
rocket = img [120:360,400:500]

img[0:240, 500:600] = rocket

text = "Imagem1"