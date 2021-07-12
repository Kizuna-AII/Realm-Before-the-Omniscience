import cv2
import numpy as np

img = cv2.imread('collection-grey.png')
img2 = cv2.imread('collection-grey-color-mask.png')
cv2.imshow("rua", img)
cv2.waitKey(0)

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cvt = [ 0.114, 0.587 ,0.299 ]
# B, G, R

[h, w, _] = np.shape(img2)
print(h, w, _)

img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img2[:, :, 2] = img[:, :, 2]
img2 = cv2.cvtColor(img2, cv2.COLOR_HSV2BGR)

cv2.imshow("rua", img2)
cv2.waitKey(0)
cv2.imwrite("result_HSV.png", img2)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2HSV)
img = img2
img[:, :, 1] = 0
img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
cv2.imshow("rua", img)
cv2.waitKey(0)
'''

import cv2
import numpy as np
# ? cv2.cvtColor might be different from our method
cvt = [ 0.114, 0.587 ,0.299 ]
grey = cv2.imread('./collection-grey.png', cv2.IMREAD_UNCHANGED) / 255
grey = grey.dot(cvt)[:,:,None] # converting to grey image and augment dim
print(f"Grey shape: {grey.shape}")
color = cv2.imread('./collection-grey-color-mask.png', cv2.IMREAD_UNCHANGED) / 255
color_grey = color.dot(cvt)[:,:,None] # converting to grey image
print(f"Color grey shape: {color.shape}")
cvted = color / color_grey * grey
# cvted = np.clip(color / color_grey * grey, 0, 255).astype('uint8')
print(f"Cvted shape: {cvted.shape}")
cvted_grey = cvted.dot(cvt)[:,:,None]

import matplotlib.pyplot as plt
plt.imshow(cvted[:,:,::-1])
plt.figure()
plt.imshow(cvted_grey,cmap="gray")
plt.show()

cv2.imwrite('./result_2.png', cvted*255)
cv2.imwrite('./result_grey_2.png', cvted_grey*255)
'''
