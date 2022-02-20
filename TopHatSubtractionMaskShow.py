
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
import os

def applyFilter(image):
    # setting the size of the minimum filter to be larger than the nuclei
    size  = 25

    minimum_trib = ndimage.minimum_filter(image, size)
    orig_sub_min = image - minimum_trib
    '''
    # visualising the result
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize =(20,20))
    ax1.imshow(image, cmap = 'gray')
    ax1.set_title('Original')
    ax2.imshow(minimum_trib, cmap = 'gray')
    ax2.set_title('Minimum')
    ax3.imshow(orig_sub_min, cmap = 'gray')
    ax3.set_title('Original - Minimum')
    plt.show()
    '''
    return minimum_trib








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
ax1.set_title('Original')

plt.show()
plt.savefig('topHatFitIndividualImages.png')


'''
fig = plt.figure(figsize=(1, 1), dpi=250)
gs = fig.add_gridspec(1, 1, hspace=0, wspace=0)
axes = gs.subplots(sharex='col', sharey='row')
axes.imshow(pic)

plt.show()
'''

