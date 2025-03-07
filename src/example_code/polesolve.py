import numpy as np
import numpy.polynomial as poly

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

for align in ['BL4','B4','LR4','IB4','CD4']:
   a1,a2,a3 = coef(align)
   a = np.array([1.0,a3,a2,a1,1.0])
   x = poly.Polynomial(a)
   r = x.roots()
   r0 = np.sqrt(abs(r[0]*r[1]))
   r1 = np.sqrt(abs(r[2]*r[3]))
   arg0 = np.real(r[0]+r[1])/(2*r0)
   arg1 = np.real(r[2]+r[3])/(2*r1)
   if abs(arg0) > 1.0:
      ang0 = np.pi
   else:
      ang0 = np.arccos(arg0)
   if abs(arg1) > 1.0:
      ang1 = np.pi
   else:
      ang1 = np.arccos(arg1)
   print('{:<3} {:.3f} {:.3f} {:.3f} {:.3f}'.format(align,r0,ang0/np.pi,r1,ang1/np.pi))





