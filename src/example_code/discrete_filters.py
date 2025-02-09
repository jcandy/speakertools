import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
GFONTSIZE=18
rc('text',usetex=True)
rc('font',size=GFONTSIZE)

def filter(s,name):
    if name == 'bw4':
        # 4th-order Butterworth
        h = 1.0/(1.0+2*np.cos(np.pi/8)*s+s**2)/(1.0+2*np.cos(3*np.pi/8)*s+s**2)
    elif name == 'bl4':
        # 4th-order Bessel
        h = 1.0/(1.0+3.201*s+4.392*s**2+3.124*s**3+s**4)
    elif name == 'lr4':
        # 4th-order Linkwitz-Riley
        h = 1.0/(1.0+np.sqrt(2.0)*s+s*s)**2
    elif name == 'cd4':
        # 4th-order Critically Damped
        h = 1.0/(1.0+4*s+6*s**2+4*s**3+s**4)
    elif name == 'ib4':
        # 4th-order Interorder Butterworth (QB3)
        b = np.sqrt(3)
        a = np.sqrt(2*(b-1))
        a1 = b**(-0.25) * (2+a)
        a2 = b**(-0.50) * (1+2*a+b)
        a3 = b**(-0.75) * (a+2*b)
        h = 1.0/(1.0+a1*s+a2*s**2+a3*s**3+s**4)
        # h = 1.0/(1.0+a3*s+a2*s**2+a1*s**3+s**4)
    return h

fig = plt.figure(figsize=(10,6))
fig.set_tight_layout(True)
ax = fig.add_subplot(111)

w = np.logspace(-1.2,1.2,256)
s = 1j*w

# Butterworth
resp = filter(1/s,'bw4')
h = abs(resp)
spl_bw4 = 20*np.log10(h)
ax.plot(w[62::],spl_bw4[62::],label=r'Butterworth (B4)')
p = np.unwrap(np.angle(resp))
gd_b4 = -np.gradient(p,w) # Group Delay

# Bessel
resp = filter(1/s,'bl4')
h = abs(resp)
spl_bl4 = 20*np.log10(h)
ax.plot(w[62::],spl_bl4[62::],label=r'Bessel (BL4)')
p = np.unwrap(np.angle(resp))
gd_bl4 = -np.gradient(p,w) # Group Delay

# Linwitz-Riley
resp = filter(1/s,'lr4')
h = abs(resp)
spl_lr4 = 20*np.log10(h)
ax.plot(w[62::],spl_lr4[62::],label=r'Linkwitz-Riley (LR4)')
p = np.unwrap(np.angle(resp))
gd_lr4 = -np.gradient(p,w) # Group Delay

# Critically Damped
resp = filter(1/s,'cd4')
h = abs(resp)
spl_cd4 = 20*np.log10(h)
ax.plot(w[62::],spl_cd4[62::],label=r'Crit. Damped (CD4)')
p = np.unwrap(np.angle(resp))
gd_cd4 = -np.gradient(p,w) # Group Delay

# Inter-Order Butterworth (IB4)
resp = filter(1/s,'ib4')
h = abs(resp)
spl_ib4 = 20*np.log10(h)
ax.plot(w[62::],spl_ib4[62::],label=r'Inter-Order (IB4)')
p = np.unwrap(np.angle(resp))
gd_ib4 = -np.gradient(p,w) # Group Delay


#ax.plot([1,1],[0,1],color='k',alpha=0.3)

ax.set_xlim([0.1,10])
ax.set_ylim([-25,3])
ax.set_xscale('log')
ax.set_xlabel(r'$\omega_n = \omega / \omega_0$')
ax.set_ylabel(r'$\vert H(\omega_n) \vert$')
plt.grid(which='both')
ax.legend()

plt.savefig('discrete_spl.png')
plt.show()

# Plot Group Delay
fig = plt.figure(figsize=(10,6))
fig.set_tight_layout(True)
ax = fig.add_subplot(111)
ax.plot(w[62::],gd_b4[62::],label=r'Butterworth (B4)')
ax.plot(w[62::],gd_bl4[62::],label=r'Bessel (BL4)')
ax.plot(w[62::],gd_lr4[62::],label=r'Linkwitz-Riley (LR4)')
ax.plot(w[62::],gd_cd4[62::],label=r'Crit. Damped (CD4)')
ax.plot(w[62::],gd_ib4[62::],label=r'Inter-Order (IB4)')
ax.set_xlim([0.1,10])
ax.set_ylim([0,5])
ax.set_xscale('log')
ax.set_xlabel(r'$\omega_n = \omega / \omega_0$')
ax.set_ylabel(r'$\tau(\omega_n)$')
plt.grid(which='both')
ax.legend()
plt.savefig('discrete_gd.png')
plt.show()
