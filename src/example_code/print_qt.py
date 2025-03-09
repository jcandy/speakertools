import numpy as np
from libalignment import *

Ql_vec = ['inf',100,50,10,7]

print('             B4                    LR4                   IB4                   BL4                   CD4        ' )
print(' Ql     Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha ')
print('---  --------------------  --------------------  --------------------  --------------------  --------------------')

for Ql in Ql_vec:
   if Ql == 'inf':
      ql = 0.0
   else:
      ql = 1/Ql

   a1,a2,a3 = coef('B4')
   Qt1,h1,alpha1 = qtsolve(a1,a2,a3,ql)
   a1,a2,a3 = coef('LR4')
   Qt2,h2,alpha2 = qtsolve(a1,a2,a3,ql)
   a1,a2,a3 = coef('IB4')
   Qt3,h3,alpha3 = qtsolve(a1,a2,a3,ql)
   a1,a2,a3 = coef('BL4')
   Qt4,h4,alpha4 = qtsolve(a1,a2,a3,ql)
   a1,a2,a3 = coef('CD4')
   Qt5,h5,alpha5 = qtsolve(a1,a2,a3,ql)
  
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,
                Qt1,h1,alpha1,
                Qt2,h2,alpha2,
                Qt3,h3,alpha3,
                Qt4,h4,alpha4,
                Qt5,h5,alpha5
                ))
                
