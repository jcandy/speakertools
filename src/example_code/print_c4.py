import numpy as np
from libalignment import *

Qtvec=[0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40]

print('           Ql=100         Ql=10           Ql=7    ')
print(' Qt      h    alpha     h    alpha     h    alpha ')
print('-----  -------------  -------------  -------------')  

for Qt in Qtvec:
   k,h1,alpha1 = c4(100.0,Qt)
   k,h2,alpha2 = c4(10.0,Qt)
   k,h3,alpha3 = c4(7.0,Qt)

   print('{:.3f}  {:.4f} {:.4f}  {:.4f} {:.4f}  {:.4f} {:.4f}'
         .format(Qt,h1,alpha1,h2,alpha2,h3,alpha3))
