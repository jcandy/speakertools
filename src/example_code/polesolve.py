import numpy as np
import numpy.polynomial as poly
import sys
import matplotlib.pyplot as plt
from matplotlib import rc

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

def poles(align):

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

   return r0,ang0,r1,ang1

#for align in ['BL4','B4','LR4','IB4','CD4']:
#   r0,ang0,r1,ang1 = poles(align)
#   print('{:<3} {:.3f} {:.3f} {:.3f} {:.3f}'.format(align,r0,ang0/np.pi,r1,ang1/np.pi))

rc('font',size=16)
rc('text',usetex=True)

x0 = 3.0

# Laplace freq 
s = 1j*np.logspace(np.log10(1/x0),np.log10(x0),64)
w = abs(s)

# Angle
t = np.linspace(0.0,2*np.pi,128)

for align in ['B4','LR4','IB4','BL4','CD4']:

   fig = plt.figure(figsize=(6,6))
   ax = fig.add_subplot(111)
   ax.set_aspect('equal')
   out = align+'-poles.png'
   r0 = 1.0
   a0 = 0.25

   c = ['k','r']
   u = 1

   ax.plot(r0*np.cos(t),r0*np.sin(t),alpha=0.3,linewidth=1,color='k')

   r0,ang0,r1,ang1 = poles(align)

   theta = np.array([ang0,ang1])
   r     = np.array([r0,r1])
   for i,t0 in enumerate(theta):
      # points
      ax.plot(r[i]*np.cos(t0),r[i]*np.sin(t0),'o',color='k')
      ax.plot(r[i]*np.cos(t0),-r[i]*np.sin(t0),'o',color='k')

   # axes
   ax.plot([-u,u],[0,0],linestyle=':',color='k',alpha=0.4)
   ax.plot([0,0],[-u,u],linestyle=':',color='k',alpha=0.4)

   ax.set_xlim(-1.1,1.1)
   ax.set_ylim(-1.1,1.1)
   ax.set_xticks([-1,0,1])
   ax.set_yticks([-1,0,1])
   ax.set_xlabel(r'$\mathrm{Re(s)}$')
   ax.set_ylabel(r'$\mathrm{Im(s)}$')

   plt.tight_layout()
   plt.savefig(out)
   fig.clear()

for align in ['B4','LR4','IB4','BL4','CD4']:

   fig = plt.figure(figsize=(6,6))
   ax = fig.add_subplot(111)
   ax.set_xscale('log')
   out = align+'-amp.png'

   a1,a2,a3 = coef(align)
   h = abs(s**4)/abs(s**4+a1*s**3+a2*s**2+a3*s+1)
   if align == 'B4':
      spl0 = 20*np.log10(h)
      ax.plot(w,spl0,label=r'B4')
   else:
      spl = 20*np.log10(h)
      ax.plot(w,spl0,label=r'B4')
      ax.plot(w,spl,label=align)

   ax.set_xlabel(r'$\omega/\omega_0$')
   ax.set_ylabel(r'$\left| G_\mathrm{H}(i\omega) \right| \mathrm{[dB]}$')
   ax.legend()
   plt.tight_layout()
   plt.savefig(out)
   fig.clear()


# amp
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xscale('log')
out = 'all-amp.png'

for align in ['B4','LR4','IB4','BL4','CD4']:
   a1,a2,a3 = coef(align)
   h = abs(s**4)/abs(s**4+a1*s**3+a2*s**2+a3*s+1)
   spl = 20*np.log10(h)
   ax.plot(w,spl,label=align)

ax.set_xlabel(r'$\omega/\omega_0$')
ax.set_ylabel(r'$\left| G_\mathrm{H}(i\omega) \right| \mathrm{[dB]}$')
ax.legend()
plt.tight_layout()
plt.savefig(out)
fig.clear()

# delay
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xscale('log')
out = 'all-delay.png'

for align in ['B4','LR4','IB4','BL4','CD4']:
   a1,a2,a3 = coef(align)
   h = s**4/(s**4+a1*s**3+a2*s**2+a3*s+1)
   p = np.unwrap(np.angle(h))
   gd = -np.gradient(p,w) # Group Delay
   ax.plot(w,gd,label=align)

ax.set_xlabel(r'$\omega/\omega_0$')
ax.set_ylabel(r'$\omega_0 \tau_g$')
ax.legend()
plt.tight_layout()
plt.savefig(out)
fig.clear()



