import numpy as np

def coef(align):

   if align == 'BL4':
      # Bessel BL4
      a1 = 105/105**0.75  
      a2 = 45/105**0.5
      a3 = 10/105**0.25
   elif align == 'B4':
      # Butterworth B4
      t1 = np.pi/8 ; t2 = 3*np.pi/8
      a1 = 2*(np.cos(t1)+np.cos(t2))
      a2 = 2+4*np.cos(t1)*np.cos(t2)
      a3 = a1
   elif align == 'LR4':
      # Linkwitz-Riley LR4
      t1 = t2 = np.pi/4
      a1 = 2*(np.cos(t1)+np.cos(t2))
      a2 = 2+4*np.cos(t1)*np.cos(t2)
      a3 = a1
   elif align == 'IB4':
      # Inter-order Butterworth IB4 
      b = np.sqrt(3)
      a = np.sqrt(2*(b-1))
      a1 = (2+a)/b**0.25
      a2 = (1+2*a+b)/b**0.5
      a3 = (a+2*b)/b**0.75
   elif align == 'CD4':
      # Critically damped CD4
      a1 = 4.0
      a2 = 6.0
      a3 = 4.0

   return a1,a2,a3

# Function to compute Qt,h,alpha for a discrete alignment
def solve(a1,a2,a3,ql):

   if ql > 1e5:
      ql = 0.0
      
   q0 = np.sqrt(a3*a1)
   l0 = np.sqrt(a3/a1)
   
   for i in range(5):
      s1 = a1-q0/l0-ql*l0
      s2 = a3-q0*l0-ql/l0
      u1 = 1/l0
      u2 = l0
      v1 = ql-q0/l0**2
      v2 = q0-ql/l0**2
      dl = (s1/u1-s2/u2)/(v1/u1-v2/u2)
      dq = (s1/v1-s2/v2)/(u1/v1-u2/v2)
      l0 = l0+dl
      q0 = q0+dq

      if abs(dl)+abs(dq) < 1e-10:
         break

   Qt    = 1/q0
   h     = l0**2
   alpha = h*(a2-ql*q0)-(1+h*h)
      
   return Qt,h,alpha

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
   Qt1,h1,alpha1 = solve(a1,a2,a3,ql)
   a1,a2,a3 = coef('LR4')
   Qt2,h2,alpha2 = solve(a1,a2,a3,ql)
   a1,a2,a3 = coef('IB4')
   Qt3,h3,alpha3 = solve(a1,a2,a3,ql)
   a1,a2,a3 = coef('BL4')
   Qt4,h4,alpha4 = solve(a1,a2,a3,ql)
   a1,a2,a3 = coef('CD4')
   Qt5,h5,alpha5 = solve(a1,a2,a3,ql)
  
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,
                Qt1,h1,alpha1,
                Qt2,h2,alpha2,
                Qt3,h3,alpha3,
                Qt4,h4,alpha4,
                Qt5,h5,alpha5
                ))
                
