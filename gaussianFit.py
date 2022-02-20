import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt


# read the image of a plant seedling as grayscale from the outset
dirname='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.490000000000002.txt'
image=np.loadtxt(dirname)

ax = plt.hist(image.ravel(), bins = 256)
plt.show()

# display the image
fig, ax = plt.subplots()
plt.imshow(image, cmap='gray')
plt.show()

#fit gaussian

import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mean,std=norm.fit(image)

plt.hist(image, bins=30, density=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)
plt.show()

print(mean, std)