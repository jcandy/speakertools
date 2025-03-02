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

Ql_vec = [100,50,10,7]

print('             BL4                   LR4                   B4')
print(' Ql     Qt    h    alpha      Qt    h    alpha      Qt    h    alpha ')
print('---  --------------------  --------------------  --------------------')

for Ql in Ql_vec:
   a1,a2,a3 = coef('BL4')
   Qt_BL4,h_BL4,alpha_BL4 = solve(a1,a2,a3,1/Ql)
   a1,a2,a3 = coef('LR4')
   Qt_LR4,h_LR4,alpha_LR4 = solve(a1,a2,a3,1/Ql)
   a1,a2,a3 = coef('B4')
   Qt_B4,h_B4,alpha_B4    = solve(a1,a2,a3,1/Ql)
  
   print('{:3}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}  {:.4f} {:.4f} {:.4f}'.
         format(Ql,Qt_BL4,h_BL4,alpha_BL4,
                Qt_LR4,h_LR4,alpha_LR4,
                Qt_B4,h_B4,alpha_B4))
