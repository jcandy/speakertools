# libalignment.py
# Library for calculation of alignments used in Speakerbench

import numpy as np

# Butterworth Qt
Qtb = 1/np.sqrt(4+np.sqrt(8))

#------------------------------------------------------------------------
# Return coefficients for the five standard discrete alignments in
# Speakerbench
#------------------------------------------------------------------------
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

#------------------------------------------------------------------------
# Function to compute Qt,h,alpha for a discrete alignment
#
#  Input: (a1,a2,a3) and ql=1/Ql
# Output: Qt,h,alpha
#------------------------------------------------------------------------
def qtsolve(a1,a2,a3,ql):

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

#------------------------------------------------------------------------
# Function to compute compliance alteration
#------------------------------------------------------------------------
def casolve(Qt,Qtref,href,aref):
   h = href*(Qtref/Qt)
   a = aref*(Qtref/Qt)**2
   return h,a


#------------------------------------------------------------------------
# Function to compute Chebyshev alignment
#------------------------------------------------------------------------

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

# Evaluate function used in secant method
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

#------------------------------------------------------------------------
# Function to compute quasialignments
#------------------------------------------------------------------------

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

def response(a1,a2,a3,x0=3.1):

   # frequency 
   w = np.logspace(np.log10(1/x0),np.log10(x0),64)
   s = 1j*w

   # complex response function
   h = s**4/(s**4+a1*s**3+a2*s**2+a3*s+1)

   # SPL
   spl = 20*np.log10(abs(h))

   # Phase
   p = np.unwrap(np.angle(h))

   # Group delay
   gd = -np.gradient(p,w)

   return w,spl,gd
