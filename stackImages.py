import numpy as np
import skimage.color
import skimage.io
import matplotlib.pyplot as plt

dirname='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.490000000000002.txt'
image1=np.loadtxt(dirname)

dirname2='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.530000000000001.txt'
image2=np.loadtxt(dirname2)

dirname3='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.540000000000001.txt'
image3=np.loadtxt(dirname3)

dirname4='/Users/oliviaseidel/Downloads/drive-download-20220220T142911Z-001/img-3.64-3.5600000000000005.txt'
image4=np.loadtxt(dirname4)

totalImage=np.hstack((image1, image2, image3,image4))

ax = plt.hist(totalImage.ravel(), bins = 256)
plt.show()

# display the image
fig, ax = plt.subplots()
plt.imshow(totalImage, cmap='gray')
plt.show()


import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mean,std=norm.fit(totalImage)

plt.hist(totalImage, bins=30, density=True)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
y = norm.pdf(x, mean, std)
plt.plot(x, y)
plt.show()

print(mean, std)

