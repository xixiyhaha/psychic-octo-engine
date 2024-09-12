import cv2

print(cv2.getVersionString())

image = cv2.imread("513b66b7c8d45599c194ca1894540e0d.png")
print(image.shape)
# 创建窗口并显示图片
cv2.namedWindow("image", cv2.WINDOW_NORMAL)  # 设置窗口可调整大小
cv2.imshow("image", image)

# 调整窗口大小
cv2.resizeWindow("image", 800, 1000)

cv2.waitKey()