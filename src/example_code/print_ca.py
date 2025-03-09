import numpy as np
from libalignment import *

Ql = 10
Qt_vec = [0.30,0.32,0.34,0.36,0.38,0.40]

print('            B4CA                  LR4CA                 IB4CA                 BL4CA                 CD4CA        ')
print(' Ql     Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha ')
print('---  --------------------  --------------------  --------------------  --------------------  --------------------')

ql = 1/Ql
for Qt in Qt_vec:
   
   a1,a2,a3 = coef('B4')
   Qtref,href,aref = qtsolve(a1,a2,a3,ql)
   h1,alpha1 = casolve(Qt,Qtref,href,aref)
   Qt1 = Qt

   a1,a2,a3 = coef('LR4')
   Qtref,href,aref = qtsolve(a1,a2,a3,ql)
   h2,alpha2 = casolve(Qt,Qtref,href,aref)
   Qt2 = Qt
   
   a1,a2,a3 = coef('IB4')
   Qtref,href,aref = qtsolve(a1,a2,a3,ql)
   h3,alpha3 = casolve(Qt,Qtref,href,aref)
   Qt3 = Qt
   
   a1,a2,a3 = coef('BL4')
   Qtref,href,aref = qtsolve(a1,a2,a3,ql)
   h4,alpha4 = casolve(Qt,Qtref,href,aref)
   Qt4 = Qt
   
   a1,a2,a3 = coef('CD4')
   Qtref,href,aref = qtsolve(a1,a2,a3,ql)
   h5,alpha5 = casolve(Qt,Qtref,href,aref)
   Qt5 = Qt
 
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,
                Qt1,h1,alpha1,
                Qt2,h2,alpha2,
                Qt3,h3,alpha3,
                Qt4,h4,alpha4,
                Qt5,h5,alpha5
                ))
                
