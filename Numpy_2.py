import numpy as np
import cv2

size = 255

#Черный слева
horizontal_gradient1 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         horizontal_gradient1[i][j] = 0 + j + 1

print(horizontal_gradient1,'\n')
cv2.imwrite('C:/Users/Aleks/Desktop/Phyton/horizontal_grad1.jpg', horizontal_gradient1)


#черный справа
horizontal_gradient2 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         horizontal_gradient2[i][j] = size - j
        
print(horizontal_gradient2,'\n')
cv2.imwrite('C:/Users/Aleks/Desktop/Phyton/horizontal_grad2.jpg', horizontal_gradient2)


#черный сверху
vertical_gradient1 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         vertical_gradient1[i][j] = 0 + i + 1
        
print(vertical_gradient1,'\n')
cv2.imwrite('C:/Users/Aleks/Desktop/Phyton/vertical_gradient1.jpg', vertical_gradient1)


#черный снизу
vertical_gradient2 = np.zeros((size,size))

for i in range(size):
    for j in range(size):
         vertical_gradient2[i][j] = size - i
        
print(vertical_gradient2,'\n')
cv2.imwrite('C:/Users/Aleks/Desktop/Phyton/vertical_gradient2.jpg', vertical_gradient2)
