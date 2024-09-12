import cv2

image = cv2.imread("7497b6366247cace632c69cc465a8c16.png")
cv2.namedWindow("blue", cv2.WINDOW_NORMAL)
cv2.namedWindow("green", cv2.WINDOW_NORMAL)
cv2.namedWindow("red", cv2.WINDOW_NORMAL)
cv2.imshow("blue",image[:,:,0])
cv2.imshow("green",image[:,:,1])
cv2.imshow("red",image[:,:,2])
cv2.resizeWindow("blue", 400, 500)
cv2.resizeWindow("green", 400, 500)
cv2.resizeWindow("red", 400, 500)

grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.namedWindow("grey", cv2.WINDOW_NORMAL)

cv2.imshow("grey",grey)
cv2.waitKey()