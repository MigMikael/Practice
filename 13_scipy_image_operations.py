from scipy.misc import imread, imsave, imresize

img = imread('C:\\Users\\Mig\\Desktop\\PDVD_009.jpg')
print(img.dtype, img.shape)

img_tinted = img * [1, 0.5, 0.5]
imsave('C:\\Users\\Mig\\Desktop\\PDVD_009_tinted.jpg', img_tinted)

img_tinted_resize = imresize(img_tinted, (1000, 1000))
imsave('C:\\Users\\Mig\\Desktop\\PDVD_009_tinted_resize.jpg', img_tinted_resize)

print('Done!')