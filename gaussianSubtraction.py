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


# the smaller Gaussian is just there to remove
# noise so it can be just a few pixels
small_gaussian = filters.gaussian(tribolium, sigma = 0)

# the larger Gaussian has to be bigger than our largest
# object, which we can measure or make an educated guess
large_gaussian = filters.gaussian(tribolium, sigma = 20)

# now we subtract the large gaussian from the small one
endImage = small_gaussian - large_gaussian
divideGaussian = endImage/large_gaussian+small_gaussian
#M =255*max(np.sqrt(divideGaussian * divideGaussian))
#O = 255 * (divideGaussian + M) / (2 * M)



# visualising the results
fig, (ax1,ax12, ax2, ax3, ax4) = plt.subplots(1, 5, figsize =(20,20))
ax1.imshow(tribolium, cmap = 'gray')
ax1.set_title('Original')
ax12.imshow(small_gaussian, cmap = 'gray')
ax12.set_title('smallgaussian')
ax2.imshow(large_gaussian, cmap = 'gray')
ax2.set_title('Large Gaussian')
ax3.imshow(dog_tribolium, cmap = 'gray')
ax3.set_title('Subtractlarge from small gaussian Image')
plt.show()
ax4.imshow(divideGaussian, cmap = 'gray')
ax4.set_title('divideSubtractedByGaussian')
plt.show()
'''
# setting the same sigmas as above
sk_dog_tribolium = filters.difference_of_gaussians(tribolium, 1, 10)

# visualising the results
# visualising the results
fig, (ax1, ax2) = plt.subplots(1, 2, figsize =(20,20))
ax1.imshow(tribolium, cmap = 'gray')
ax1.set_title('Original')
ax2.imshow(sk_dog_tribolium, cmap = 'gray')
ax2.set_title('DoG Image')
plt.show()
'''