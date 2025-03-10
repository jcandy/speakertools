import numpy as np
from libalignment import *

Ql = 10
Qt_vec = [0.30,0.32,0.34,0.36,0.38,0.40]

h0     = {}
alpha0 = {}

print('             B4Q                  LR4Q                  IB4Q                 BL4Q                   CD4Q         ')
print(' Ql     Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha      Qt    h    alpha ')
print('---  --------------------  --------------------  --------------------  --------------------  --------------------')

ql = 1/Ql
for Qt in Qt_vec:
   for align in ['B4','LR4','IB4','BL4','CD4']:
      a1,a2,a3 = coef(align)
      A1 = a1**2-2*a2
      A2 = a2**2+2-2*a1*a3
      h0[align],alpha0[align] = quasi(Ql,Qt,A1,A2)
 
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,
                Qt,h0['B4'],alpha0['B4'],
                Qt,h0['LR4'],alpha0['LR4'],
                Qt,h0['IB4'],alpha0['IB4'],
                Qt,h0['BL4'],alpha0['BL4'],
                Qt,h0['CD4'],alpha0['CD4'],
                ))
                
