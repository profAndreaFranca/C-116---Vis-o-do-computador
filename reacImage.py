import cv2

image = cv2.imread("./butterfly.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem",image)
cv2.imshow("ImagemCinza",gray)


print(gray)

cv2.waitKey(0)