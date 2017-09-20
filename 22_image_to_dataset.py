import cv2
import numpy as np

e1 = cv2.getTickCount()
img = cv2.imread('C:/Users/Mig/Desktop/seven.jpg')

row, col, channels = img.shape
print(row, col, channels)

'''
tiny_crop = img[0:5, 0:5]
cv2.imshow('tiny-crop', tiny_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

for i in range(0, row, 5):
    for j in range(0, col, 5):
        tiny_crop = img[i:i+5, j:j+5]

        blue = tiny_crop[:, :, 0]
        green = tiny_crop[:, :, 1]
        red = tiny_crop[:, :, 2]

        # Blue pixel
        mean_blue = np.mean(blue)
        img[i:i+5, j:j+5, 0] = mean_blue.astype(np.int64)

        # Green pixel
        mean_green = np.mean(green)
        img[i:i+5, j:j+5, 1] = mean_green.astype(np.int64)

        # Red pixel
        mean_red = np.mean(red)
        img[i:i+5, j:j+5, 2] = mean_red.astype(np.int64)

        #print(img[i:i+5, j:j+5])
        # cv2.imwrite('C:/Users/Mig/Desktop/cropp/tiny-crop_' + str(i) + '_' + str(j) + '.jpg', tiny_crop)

# cv2.imwrite('C:/Users/Mig/Desktop/seven_editt.jpg', img)

print(type(img))
data = img.ravel()
data = data.astype(np.int64)

data_set = []

print(data.shape)
for i in range(data.shape[0]):
    data_set.append(str(data[i]) + " ")
# np.savetxt('C:/Users/Mig/Desktop/data-text.txt', data.astype(np.int32))

count = 0
with open('C:/Users/Mig/Desktop/data-text.txt', 'w') as outfile:
    for data_line in data_set:
        outfile.write(data_line)
        count += 1

print(count)
print('finish')
e2 = cv2.getTickCount()
time = (e2 - e1) / cv2.getTickFrequency()
print(time)
