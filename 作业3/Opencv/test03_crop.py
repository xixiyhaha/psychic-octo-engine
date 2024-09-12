import cv2

image = cv2.imread("c778f7e3094b0daf53c6eb3e2926cadf.png")

crop = image[10:1700, 40:2000]
resized_crop = cv2.resize(crop, (1000, 800))
cv2.imshow("crop", resized_crop)
cv2.waitKey()