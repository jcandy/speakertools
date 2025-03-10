import numpy as np
from libalignment import *

Ql = 10
Qt_vec = [0.30,0.32,0.34,0.36,0.38,0.40]

h0     = {}
alpha0 = {}

print('            B4CA                  LR4CA                 IB4CA                 BL4CA                 CD4CA        ')
print(' Ql     Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha ')
print('---  --------------------  --------------------  --------------------  --------------------  --------------------')

ql = 1/Ql
for Qt in Qt_vec:
   for align in ['B4','LR4','IB4','BL4','CD4']:
      a1,a2,a3 = coef(align)
      Qtref,href,aref = qtsolve(a1,a2,a3,ql)
      h0[align],alpha0[align] = casolve(Qt,Qtref,href,aref)
 
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,
                Qt,h0['B4'],alpha0['B4'],
                Qt,h0['LR4'],alpha0['LR4'],
                Qt,h0['IB4'],alpha0['IB4'],
                Qt,h0['BL4'],alpha0['BL4'],
                Qt,h0['CD4'],alpha0['CD4'],
                ))
                
