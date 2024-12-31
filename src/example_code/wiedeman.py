import numpy as np
import time

def y(s):
    qts = 0.5
    alpha = 0.0
    y = s**2/(s**2+s/qts+1+alpha)
    return y
              
def step():

   #------------------------------------------------------------
   # Some adjustable settings

   # Number of time points
   nt = 400

   # Initial number of integration nodes along parabola
   N0 = 16

   # Max(ws*t) = total integration time (t_max in AES paper)
   tmax = 8.0
   #------------------------------------------------------------

   mu_c = max(1,h)
   t_c = np.pi*N0/(12*mu_c)

   # Pack points closer to t=0
   tvec = tmax*np.linspace(1e-4,1.0,nt)**2
   svec = np.zeros(nt)
   
   for j in range(nt):

      t = tvec[j]

      if t<t_c:
         mu = np.pi*N0/(12.0*t)
         N = N0
      else:
         mu = mu_c
         N = np.ceil(N0*t/t_c).astype('int')

      d = 3.0/N
  
      # Vectorize over contour sum
      u = d*np.arange(-N,N+1)
      s = mu*(1j*u+1)**2
      dsdu = 2.0*mu*(1j-u)
      step = np.sum(np.imag(np.exp(s*t)*y(s)/s*dsdu))*d/(2*np.pi) 
      
      # step response
      svec[j] = step

   return tvec,svec

t,s = step()

exact = np.exp(-t)*(1-t)
for i,t0 in enumerate(t):
    print('{:.3f} {:.4f} {:.4f}'.format(t0,p[i],exact[i]))
