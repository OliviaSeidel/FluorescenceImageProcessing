from skimage import filters
from skimage import io, morphology
import numpy as np
import matplotlib.pyplot as plt
import skimage.feature as features
from scipy import ndimage

dirname2='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.530000000000001.txt'
image2=np.loadtxt(dirname2)

dirname3='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.540000000000001.txt'
tribolium=np.loadtxt(dirname3)

# for a single img 1930.8439792387544 11.842518410251547
#for 4 images:
mean, std =1931.3832179930796, 11.998179447722286

# setting the size of the minimum filter to be larger than the nuclei
size  = 25

minimum_trib = ndimage.minimum_filter(image2, size)
orig_sub_min = image2 - minimum_trib



size2  = 45

minimum_trib2 = ndimage.minimum_filter(image2, size2)
orig_sub_min2 = image2 - minimum_trib2

# visualising the result
fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1, 5, figsize =(20,20))
ax1.imshow(image2, cmap = 'gray')
ax1.set_title('Original')
ax2.imshow(minimum_trib, cmap = 'gray')
ax2.set_title('Minimum')
ax3.imshow(orig_sub_min, cmap = 'gray')
ax3.set_title('Original - Minimum')
ax4.imshow(minimum_trib2, cmap = 'gray')
ax4.set_title('Minimum')
ax5.imshow(orig_sub_min2, cmap = 'gray')
ax5.set_title('Original - Minimum')
plt.show()




'''
# the smaller Gaussian is just there to remove
# noise so it can be just a few pixels
small_gaussian = filters.gaussian(tribolium, sigma = 1)

# the larger Gaussian has to be bigger than our largest
# object, which we can measure or make an educated guess
large_gaussian = filters.gaussian(tribolium, sigma = 100)

# now we subtract the large gaussian from the small one
dog_tribolium = small_gaussian - large_gaussian

# visualising the results
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize =(20,20))
ax1.imshow(small_gaussian, cmap = 'gray')
ax1.set_title('Small Gaussian')
ax2.imshow(large_gaussian, cmap = 'gray')
ax2.set_title('Large Gaussian')
ax3.imshow(dog_tribolium, cmap = 'gray')
ax3.set_title('DoG Image')

# setting the same sigmas as above
sk_dog_tribolium = filters.difference_of_gaussians(tribolium, 1, 100)

# visualising the results
# visualising the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize =(20,20))
ax1.imshow(tribolium, cmap = 'gray')
ax1.set_title('Original')
ax2.imshow(sk_dog_tribolium, cmap = 'gray')
ax2.set_title('DoG Image')
plt.show()
'''