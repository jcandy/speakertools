import numpy as np

# Butterworth Qt
Qtb = 1/np.sqrt(4+np.sqrt(8))

# Find k in the Ql=inf limit
def root(Qt):
   alpha = (Qt/Qtb)**2
   a = alpha*np.sqrt(8)-1
   b = alpha*(8-np.sqrt(8))-6
   # Positive root
   r = (-b+np.sqrt(b**2+4*a))/(2*a)
   # Cheb k
   k = np.sqrt(r)
   return k

# Evaluate function for secand method
def f(k,Ql,Qt):
   # Standard C4 formulae
   d = (k**4+6*k**2+1)/8
   a3 = k/Qtb/d**0.25
   a1 = a3/d**0.5*(1-(1-k**2)/8**0.5)
   a2 = 1+k**2*(1+np.sqrt(2))/np.sqrt(d)
   
   # Solve a3 equation for l
   l = 0.5*Qt*(a3+np.sqrt(a3**2-4/(Ql*Qt)))

   # function to solve for f(k)=0
   f = 1/(Qt*l)+l/Ql-a1

   return f,l,a2

# Secant method to determine k
def c4(Ql,Qt):

   k1 = root(Qt)
   k2 = k1+0.1

   for i in range(10):
      f1,l1,a2 = f(k1,Ql,Qt)
      f2,l2,a2 = f(k2,Ql,Qt)

      k = (k1*f2-k2*f1)/(f2-f1)
      k1 = k2
      k2 = k
      if abs(k1-k2) < 1e-10:
         break

   ql = 1/Ql
   q0 = 1/Qt
   h  = l2**2
   
   alpha = h*(a2-ql*q0)-(1+h*h)

   return k,h,alpha
      
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
