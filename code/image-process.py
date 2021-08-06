import cv2
import numpy as np

colors = np.random.uniform(0, 255, size=(1, 1))

img = cv2.imread("2.jpg")
x = 397
y = 2160
w = 1730
h = 1545
cv2.rectangle(img, (x, y), (x + w, y + h), colors[0][0], 2)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()