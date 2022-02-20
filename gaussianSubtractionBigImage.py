
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
import os
from skimage import filters

def applyFilter(image):

    # the smaller Gaussian is just there to remove
    # noise so it can be just a few pixels
    small_gaussian = filters.gaussian(image, sigma = 0)

    # the larger Gaussian has to be bigger than our largest
    # object, which we can measure or make an educated guess
    large_gaussian = filters.gaussian(image, sigma = 7)

    # now we subtract the large gaussian from the small one
    dog_tribolium = small_gaussian - large_gaussian
    '''
    # visualising the results
    fig, (ax1,ax12, ax2, ax3) = plt.subplots(1, 4, figsize =(20,20))
    ax1.imshow(image, cmap = 'gray')
    ax1.set_title('Original')
    ax12.imshow(small_gaussian, cmap = 'gray')
    ax12.set_title('smallgaussian')
    ax2.imshow(large_gaussian, cmap = 'gray')
    ax2.set_title('Large Gaussian')
    ax3.imshow(dog_tribolium, cmap = 'gray')
    ax3.set_title('Subtractlarge from small gaussian Image')
    plt.show()
    '''
    return dog_tribolium

files = []
file_list = os.listdir(r"/Users/oliviaseidel/Downloads/drive-download-20220220T155705Z-001")
dirname = '/Users/oliviaseidel/Downloads/drive-download-20220220T155705Z-001'
for name in file_list:
    files.append(os.path.join(dirname, name))
files = np.asarray(files)
print(files.shape)

combinedfullImg = []
combinedfullImg = np.asarray(combinedfullImg)

combinedxImg = []
combinedxImg = np.asarray(combinedxImg)

# combine the first two images
# (0 for first round, then 10 and 10+1)
newimage = np.loadtxt(files[0])
newimage = np.asarray(newimage)
newimage=applyFilter(newimage)

secondimage = np.loadtxt(files[1])
secondimage = np.asarray(secondimage)
secondimage = applyFilter(secondimage)
combinedxImg = np.concatenate((newimage, secondimage), 1)

# combine the next 18 or 8 images
# (range 2-10 for 8 more photos)

for x in range(2, 10):
    newimage = np.loadtxt(files[x])
    newimage = np.asarray(newimage)
    newimage = applyFilter(newimage)
    combinedxImg = np.concatenate((combinedxImg, newimage), 1)

combinedfullImg = combinedxImg

# now for the rest (range of 9 bc we have 9 more to add after the first one has been added)

for i in range(1, 10):

    combinedxImg = []
    combinedxImg = np.asarray(combinedxImg)

    # combine the first two images
    # (0 for first round, then 10 and 10+1)
    newimage = np.loadtxt(files[i * 10])
    newimage = np.asarray(newimage)
    newimage = applyFilter(newimage)
    secondimage = np.loadtxt(files[i * 10 + 1])
    secondimage = np.asarray(secondimage)
    secondimage = applyFilter(secondimage)
    combinedxImg = np.concatenate((newimage, secondimage), 1)

    # combine the next 18 or 8 images
    # (range 2-10)
    for x in range(i * 10 + 2, i * 10 + 10):
        newimage = np.loadtxt(files[x])
        newimage = np.asarray(newimage)
        newimage = applyFilter(newimage)
        combinedxImg = np.concatenate((combinedxImg, newimage), 1)

    combinedfullImg = np.concatenate((combinedfullImg, combinedxImg), 0)

pic = np.array(combinedfullImg)
fig, (ax1) = plt.subplots(1, 1, figsize=(20, 20))
ax1.imshow(pic, cmap='gray')
ax1.set_title('Gaussian Filter')

plt.show()
im = Image.fromarray(combinedfullImg)
im = im.convert("L")
im.save("biggaussian7sigma.png")
'''
a_file = open("biggaussian7sigma.txt", "w")
for row in pic:
    np.savetxt(a_file, row)
'''
#plt.savefig('GaussianFitIndividualImages.png')
