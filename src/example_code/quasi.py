import numpy as np
   
def quasi(Ql,Qt,A1,A2):

   q   = 1/Qt
   eps = Qt/Ql

   # starting values
   h = 1
   alpha = 1

   # iterate (should add convergence check)
   for i in range(4):
      gamma = -eps*q**2+np.sqrt(A2-2+2*q**2*(1+eps**2+eps*(1/h+h)))
      h = q**2/(2*gamma+A1-eps**2*h*q**2)
      alpha = h*gamma-(1+h**2)
      
   return h,alpha

Ql=10
Qtvec=[0.31,0.32,0.33,0.34,0.35,0.36,0.37,0.38,0.39,0.40]

print('            QBL4           QLR4           QLR4e           QB4')
print(' Qt      h    alpha     h    alpha     h    alpha     h    alpha ')
print('-----  -------------  -------------  -------------  -------------')  

for Qt in Qtvec:
   h1,alpha1 = quasi(Ql,Qt,1.464,1.286)
   h2,alpha2 = quasi(Ql,Qt,0.0,2.0)
   h3,alpha3 = quasi(Ql,Qt,0.0,0.0)

   h2e,alpha2e = epsqlr4(Ql,Qt)

   print('{:.3f}  {:.4f} {:.4f}  {:.4f} {:.4f}  {:.4f} {:.4f}   {:.4f} {:.4f}  '
         .format(Qt,h1,alpha1,h2,alpha2,h2e,alpha2e,h3,alpha3))



