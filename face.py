'''
Created on Aug 10, 2019

@author: asharda
'''
from scipy import misc
f=misc.face()
misc.imsave('test.png',f)
import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()
