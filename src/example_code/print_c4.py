import numpy as np
from libalignment import *

Qtvec=[0.32,0.34,0.36,0.38,0.40,0.42,0.44,0.46,0.48,0.50]

print('           Ql=100         Ql=10           Ql=7    ')
print(' Qt      h    alpha     h    alpha     h    alpha ')
print('-----  -------------  -------------  -------------')  

for Qt in Qtvec:
   k,h1,alpha1 = c4(100.0,Qt)
   k,h2,alpha2 = c4(10.0,Qt)
   k,h3,alpha3 = c4(7.0,Qt)

   print('{:.3f}  {:.4f} {:.4f}  {:.4f} {:.4f}  {:.4f} {:.4f}'
         .format(Qt,h1,alpha1,h2,alpha2,h3,alpha3))
