import numpy as np
from libalignment import *

Ql=10
Qtvec=[0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40]

print('            QBL4           QLR4           QB4')
print(' Qt      h    alpha     h    alpha     h    alpha ')
print('-----  -------------  -------------  -------------')

for Qt in Qtvec:
   h1,alpha1 = quasi(Ql,Qt,1.464,1.286)
   h2,alpha2 = quasi(Ql,Qt,0.0,2.0)
   h3,alpha3 = quasi(Ql,Qt,0.0,0.0)

   print('{:.3f}  {:.4f} {:.4f}  {:.4f} {:.4f}  {:.4f} {:.4f}  '
         .format(Qt,h1,alpha1,h2,alpha2,h3,alpha3))



