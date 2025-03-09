import numpy as np
import numpy.polynomial as poly
import sys
import matplotlib.pyplot as plt
from matplotlib import rc
from libalignment import *

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

rc('font',size=16)
rc('text',usetex=True)

# Angle
t = np.linspace(0.0,2*np.pi,128)

#--------------------------------------------
# Pole plots
#--------------------------------------------
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

#--------------------------------------------
# Individual amplitude plots
#--------------------------------------------
for align in ['B4','LR4','IB4','BL4','CD4']:

   fig = plt.figure(figsize=(6,6))
   ax = fig.add_subplot(111)
   ax.set_xscale('log')
   out = align+'-amp.png'

   a1,a2,a3 = coef(align)
   w,spl,delay = response(a1,a2,a3)
   if align == 'B4':
      spl0 = spl
      ax.plot(w,spl0,label=r'B4')
   else:
      ax.plot(w,spl0,label=r'B4')
      ax.plot(w,spl,label=align)

   ax.set_ylim(-36,2)
   ax.set_xlabel(r'$\omega/\omega_0$')
   ax.set_ylabel(r'$\left| G_\mathrm{H}(i\omega) \right| \mathrm{[dB]}$')
   ax.legend()
   plt.tight_layout()
   plt.savefig(out)
   fig.clear()


#--------------------------------------------
# All-amplitude plots
#--------------------------------------------
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xscale('log')
out = 'all-amp.png'

for align in ['B4','LR4','IB4','BL4','CD4']:
   a1,a2,a3 = coef(align)
   w,spl,gd = response(a1,a2,a3)
   ax.plot(w,spl,label=align)

ax.set_ylim(-36,2)
ax.set_xlabel(r'$\omega/\omega_0$')
ax.set_ylabel(r'$\left| G_\mathrm{H}(i\omega) \right| \mathrm{[dB]}$')
ax.legend()
plt.tight_layout()
plt.savefig(out)
fig.clear()

#--------------------------------------------
# All-delay plots
#--------------------------------------------
fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot(111)
ax.set_xscale('log')
out = 'all-delay.png'

for align in ['B4','LR4','IB4','BL4','CD4']:
   a1,a2,a3 = coef(align)
   w,spl,gd = response(a1,a2,a3)
   ax.plot(w,gd,label=align)

ax.set_ylim(0,4)
ax.set_xlabel(r'$\omega/\omega_0$')
ax.set_ylabel(r'$\omega_0 \, \tau_g$')
ax.legend()
plt.tight_layout()
plt.savefig(out)
fig.clear()



