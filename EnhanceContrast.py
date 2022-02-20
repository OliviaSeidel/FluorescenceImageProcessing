

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

# Open the input image as numpy array, convert to greyscale and drop alpha
from matplotlib import cm

npImage=np.array(Image.open("biggaussian7sigma.png").convert("L"))




#npImage= npImage.set_clim(0, 0.5)


fig, ax = plt.subplots(1,1)
x_label_list = ['0.01', '0.02','0.03','0.04', '0.05','0.06', '0.07','0.08', '0.09', '0.1']
plt.imshow(npImage,cmap="gray")
plt.clim(0, 40)
plt.xticks(ticks=[170,2*170,3*170,4*170,5*170,6*170,7*170,8*170,9*170,10*170], labels=x_label_list)
y_label_list = ['0.1','0.09','0.08','0.07','0.06', '0.05','0.04', '0.03','0.02', '0.01', '0.00']
plt.yticks(ticks=[0, 170,2*170,3*170,4*170,5*170,6*170,7*170,8*170,9*170,10*170], labels=y_label_list)


plt.title('Single Molecule Flourecence over O.1mm^2')

plt.ylabel("Distance (mm)")
plt.xlabel("Distance (mm)")




#ax.set_xticks([1,2,3,4,5,6,7,8,9,10])
#ax.set_xticklabels(['0.01', '0.02','0.03','0.04', '0.05','0.06', '0.07','0.08', '0.09', '0.1'])

ig, ax = plt.subplots(1,1)

ax.imshow(npImage, cmap="gray")
#ax.set_clim(0, 40)


ax.set_xticks([170,2*170,3*170,4*170,5*170,6*170,7*170,8*170,9*170,10*170])
ax.set_xticklabels(x_label_list)

y_label_list = ['0.1','0.09','0.08','0.07','0.06', '0.05','0.04', '0.03','0.02', '0.01', '0.00']
ax.set_yticks([0, 170,2*170,3*170,4*170,5*170,6*170,7*170,8*170,9*170,10*170])
ax.set_yticklabels(y_label_list)

plt.title('Single Molecule Flourecence over O.1mm^2')

plt.ylabel("Distance (mm)")
plt.xlabel("Distance (mm)")

plt.show()


# Get brightness range - i.e. darkest and lightest pixels
min=np.min(npImage)        # result=144
max=np.max(npImage)        # result=216

# Make a LUT (Look-Up Table) to translate image values
LUT=np.zeros(256,dtype=np.uint8)
LUT[min:max+1]=np.linspace(start=0,stop=255,num=(max-min)+1,endpoint=True,dtype=np.uint8)

# Apply LUT and save resulting image
Image.fromarray(LUT[npImage]).save('result.png')


'''



#image brightness enhancer
enhancer = ImageEnhance.Contrast(im)

factor = 1 #gives original image
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 0.5 #decrease constrast
im_output = enhancer.enhance(factor)
im_output.save('less-contrast-image.png')

factor = 1.5 #increase contrast
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')
'''