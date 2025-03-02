.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

=========================
Classic Vented Alignments
=========================

In classical loudspeaker theory from the 1960s onwards, the concept of alignments was developed to provide a systematic prescription for choosing box volume and port tuning to yield a target low-frequency response. While the theory is not exact, it offers numerous benefits including insight into the choice between low frequency extension versus group delay (phase distortion). For a brief overview of the alignments discussed here and supported in Speakerbench, please scroll down to the :ref:`Summary` section at end of this page. Because this section is potentially confusing, we outline the overall structure as

1. General framework (key equations)
2. Discrete alignments (B4,BL4,LR4,IB4,CD4)
3. Alignment families (C4,BB4)
4. Misalignment families (quasi and compliance alteration)

General framework
-----------------

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4\ :sup:`th`-order bass-reflex alignments. These alignments are particular types of 4\ :sup:`th`-order high-pass filters. Following Small :cite:`small:1973c` (Eq. 57) we can write the normalized response function as

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + a_1 s^3 + a_2 s^2 + a_3 s + 1} \; ,

where :math:`s = j \omega / \omega_0` is the dimensionless complex frequency variable normalized to :math:`\omega_0 \doteq \sqrt{\omega_B \, \ws}`. In the first part of his article series, Small :cite:`small:1973c` (Eqs. 22--24) writes the lossy box filter coefficients as

.. math::
   \begin{eqnarray}
   \displaystyle
   a_1 &=& \frac{\ql + h \: \qt}{\sqrt{h} \: \ql \: \qt} \nonumber \\
   a_2 &=& \frac{h + (\alpha + 1 + h^2) \: \ql \: \qt}{h \: \ql \: \qt}\nonumber \\
   a_3 &=& \frac{h \: \ql + \qt}{\sqrt{h} \: \ql \: \qt} \; ,\label{eq:box}
   \end{eqnarray}

where :math:`\ql` is the leakage-loss :math:`Q` of the box and :math:`\qt` is the total :math:`Q` of the driver. Here, :math:`h = \omega_B/\ws` is the system tuning ratio and :math:`\alpha = V_{AS} / V_B` is the ratio of the compliance volume to the box volume. We remark that the coefficients are approximate and neglect myriad other terms which appear in a more comprehensive model of a vented box. These missing terms would represent more complex losses in the box and in the driver suspension system, driver inductance and semi-inductance, and so on. In the definition of :math:`\omega_0`, :math:`\ws` is the driver resonant frequency and :math:`\omega_B` is the vent resonant frequency. This normalization is equivalent to setting :math:`T_0=1` in Small's expressions. The magnitude-versus-frequency behavior is also given in Small :cite:`small:1973c` (Eqs. 58 and 59), which we reproduce here as

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + A_1 \omega^6 + A_2 \omega^4 + A_3 \omega^2 + 1} \; ,

where

.. math::
  \begin{eqnarray}
  A_1 &=& a_1^2-2 a_2 \; , \\
  A_2 &=& a_2^2+2-2 a_1 a_3 \; , \\
  A_3 &=& a_3^2-2 a_2 \; .
  \end{eqnarray}

Discrete alignments
-------------------

A *discrete* bass reflex alignment means we need to select a driver with a specific :math:`\qts` value and match that with a specific box volume and port tuning frequency to obtain the unique discrete alignment. Two popular classic discrete alignments are the Butterworth (B4) and Bessel (BL4) ones. In addition, Thiele (reference) defined the Inter-Order Butterworth (IB4) discrete alignment around 1974. In these notes we further discuss the so-called Linkwitz-Riley (LR4) and Critically Damped (CD4) discrete alignments. Each discrete alignment defines a specific 4th-order filter with fixed coefficients :math:`(a_1,a_2,a_3)` along with properties that are broadly suitable for vented aligments. The coefficients are

Butterworth B4
^^^^^^^^^^^^^^

The Butterworth filter response was first described by Stephen Butterworth around 1930. This filter offers a maximally-flat frequency response (with no ripple in the passband) offers the sharpest knee point towards the roll-off region and thus the most extended bandwidth. In relation to bass reflex loudspeakers, B4 was a very popular target response for many years, and several (non-discrete) alignment *families* ultimately develops from B4. The amplitude response function 

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + 2.613 s^3 + 3.141 s^2 + 2.613 s + 1} \; ,

The filter coefficients depend on cosines of the pole locations :math:`\theta_1 = \pi/8` and :math:`\theta_2 = 3\pi/8` as

.. math::
   a_1 &~= 2 \cos\theta_1 + 2 \cos\theta_2 \\
   a_2 &~= 2+4 \cos\theta_1 \cos\theta_2  \\
   a_3 &~= a_1

The remarkable vanishing of all coefficients :math:`(A_1,A_2,A_3)` demonstrates the maximally-flat property via 
 
.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + 1} \; ,


Bessel BL4
^^^^^^^^^^

The Bessel response is written in terms of the Bessel polynomials introduced by Friedrich Wilhelm Bessel (1784 -1846). The practical application to filters was worked out by W.E. Thomson in 1949 in a scientific article titled *Delay Networks Having Maximally Flat Frequency Characteristics*. Thomson described this filter function applied to delay lines. Low-pass Bessel filters are characterized by the fastest settling time and maximally flat group delay of the form :math:`D \sim 1 + O(\omega^8)`. A frequency range with flat group delay implies nearly linear phase response and hence minimal phase distortion of the signal.

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + 3.201 s^3 + 4.392 s^2 + 3.124 s + 1} \; ,

The filter coefficients are derived from the Bessel polynomial :math:`y_4(x) = 105 x^4 + 105 x^3 + 45 x^2 + 10 x + 1`

.. math::
   a_1 &~= 105/105^{3/4} \\
   a_2 &~= 45/105^{1/2} \\
   a_3 &~= 10/105^{1/4}

Linkwitz-Riley LR4
^^^^^^^^^^^^^^^^^^

The Linkwitz-Riley filter response was described by Siegfried H. Linkwitz in 1976 as two cascaded Butterworth filters, which poses the desirable feature as a crossover between two non-coincident transducers, that they sum in-phase. In relation to bass reflex alignment, we are not crossing to another driver, but the LR4 alignment poses some desirable features like fast settling time (nice impulse response) similar to the BL4 alignment and a more extended frequency response when compared with the BL4 alignment. The response function is:

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + 2.8284271 s^3 + 4 s^2 + 2.8284271 s + 1} \; ,

We describe this alignment in a bit more detail in its own section: :ref:`The LR4 Bass Reflex Alignment`.

Critically damped CD4
^^^^^^^^^^^^^^^^^^^^^

A critically damped filter response poses the desirable feature of no overshoot, not even to a step function input (a worst-case scenario), and with this constraint obtains the most extended frequency response. We obtain this by placing all the poles on the real axis. The CD4 alignment is defined as two cascaded second-order Linkwitz-Riley filters. In relation to bass reflex, this alignment is not commonly used due to the early roll-off in the frequency response. The response function is:

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + 4 s^3 + 6 s^2 + 4 s + 1} \; ,


We describe this alignment in a bit more detail in its own section: :ref:`The CD4 Bass Reflex Alignment`.

Inter-Order Butterworth IB4
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The fourth-order Inter-Order Butterworth high-pass filter is defined by A. N. Thiele as a combination of a second-order and two identical first-order filters. Two cascaded first-order 'Butterworth' filters become a second-order Linkwitz-Riley filter function. The other second-order term is defined by targeting a maximally flat 4\ :sup:`th`-order response. When compared to the LR4 response, an IB4 alignment will have a bit more extended response, then a sharper knee and faster roll-off (similar to a maximally flat response, but within what's obtainable with the constraint of two first-order filters). The two first-order filters place two of the poles on the real axis. The response function is:

.. math::

   G_\mathrm{H}(s) = \frac{s^4}{s^4 + 2.7981112 s^3 + 3.9147131 s^2 + 3.0958345 s + 1} \; ,

.. code-block:: python

   import numpy as np

   Ql = 10
   lam = np.sqrt(3)           # lambda
   kap = np.sqrt(2*(lam-1))   # kappa
   a1 = (2+kap)*lam**(-0.25)  # polynomial coefficients
   a2 = (1+2*kap+lam)*lam**(-0.50)
   a3 = (kap+2*lam)*lam**(-0.75)
   Qt = 1/(np.sqrt(a1*a3) - 1/Ql)
   q = 1/Qt
   eps = Qt/Ql
   h = 1
   h0 = 10
   tol = 1e-8                 # numerically solve for h
   while abs(h-h0) > tol:
      h0 = h
      S =  -eps * q**2 + np.sqrt(A2 - 2 + 2 * q**2 * (1 + eps**2 + eps * (h + 1/h)))
      h = q**2 / (2*S + A1 - eps**2 * q**2 * h)

   alpha = S * h - (1 + h**2)

We describe this alignment in a bit more detail in its own section: :ref:`The IB4 Bass Reflex Alignment`.

Comparison
^^^^^^^^^^

:numref:`discrete_spl` and :numref:`discrete_gd` shows the (normalized) magnitude response and group delay response of the above mentioned discrete alignments.

.. figure:: images/discrete_spl.png
            :width: 80 %
	    :name: discrete_spl
	    :align: center

            The normalized magnitude response of the discrete alignments.


.. figure:: images/discrete_gd.png
            :width: 80 %
	    :name: discrete_gd
	    :align: center

            The normalized group delay response of the discrete alignments.

Note: These graphs are **not** normalized relative to the driver's resonance frequency, but :math:`\omega_0 \doteq \sqrt{\omega_B \, \ws} = \sqrt{h} \cdot \ws`.

Modification of discrete alignments 
-----------------------------------

For the discrete alignments, :math:`\qts` is not a free parameter. In practice you need to consider what to do if you have a preferred discrete alignment but the driver is *misaligned* -- that is, if the driver :math:`\qts` does not match that required by your target alignment. 

For example, consider the 4th-order Butterworth. In the section below we will describe three misalignment options for B4; namely, B4i (method of ignorance), B4Q (quasialignment), and B4CA (compliance alteration). These options also appear in the Speakerbench Alignment Chart. The three will converge to a single point in the chart (the same alignment) as your driver :math:`\qts` approaches the :math:`\qts` value for B4. On the other hand, when the driver :math:`\qts` is far from the target :math:`\qts`, the three methods will be far from each other and also probably undesirable as an alignment. 

(1) Method of ignorance
^^^^^^^^^^^^^^^^^^^^^^^

The simplest solution is to ignore the fact that the driver :math:`\qts` is far from the target :math:`\qts`. This we call the method of ignorance, because you ignore the fact that :math:`\qts` is wrong. Speakerbench denotes this approach by adding a trailing 'i' to the name: B4i, LR4i and BL4i. In this case, the suggested :math:`h` and :math:`\alpha` are **unaffected** by the driver :math:`\qts` (the fact that :math:`\qts` is not correct is ignored). The method of ignorance **is not recommended for actual use**, but is included for reference. Despite the name, We suspect that this method was commonly used in the past.

(2) Method of compliance alteration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another approach to handling the situation where the driver :math:`\qts` isn't matched perfectly, is to assume the misalignment (or error) is due to the driver suspension being either too soft or too stiff, i.e., that the driver compliance is imagined to be altered such that the target :math:`\qts` value for the target alignment is met.

Compliance Alteration is computed by first 1) Calculating the reference :math:`Q_\mathrm{Tref}` for your target and the resulting :math:`\alpha_\mathrm{ref}` and :math:`h_\mathrm{ref}`, then 2) shift :math:`\alpha` and :math:`h` relative to the :math:`\qts` for the actual driver at hand in the following way:

.. math::
   \begin{eqnarray}
   \alpha &=& \alpha_\mathrm{ref} \cdot \Big( \frac{Q_\mathrm{Tref}}{\qts} \Big)^2 \; , \\
   h &=& h_\mathrm{ref} \cdot \frac{Q_\mathrm{Tref}}{\qts} \; .
   \end{eqnarray}

In Speakerbench, when we apply this method, the alignment acronym is followed by 'CA' as in B4CA, LR4CA and BL4CA.

**Source code**

.. code-block:: python

  import numpy as np

  def ca_shift(Qtref,Qt,aref,href):
      """Function calculating Compliance Alteration parameter shift"""
      h_out = href * Qtref/Qt
      alpha_out = aref * (Qtref/Qt)**2
      return h_out,alpha_out

  Ql = 10
  Qtvec=[0.34,0.36,0.38,0.40,0.42]

  Qt = 1./(1./np.cos(3*np.pi/8)-1./Ql)
  h_ref = 1
  a3 = np.sqrt(8)*np.cos(np.pi/8)
  alpha_ref = np.sqrt(2) - (1/Ql**2) * (a3*Ql-1)

  print('           B4CA')
  print(' Qts     h    alpha ')
  print('-----  -------------')

  for i,Qts in enumerate(Qtvec):
     h,alpha = ca_shift(Qt,Qts,alpha_ref,h_ref)
     print('{:.3f}  {:.4f} {:.4f}  '
        .format(Qts,h,alpha)   )


**Output**

::

             B4CA
   Qts     h    alpha
  -----  -------------
  0.340  1.1703 1.5928
  0.360  1.1053 1.4207
  0.380  1.0471 1.2751
  0.400  0.9948 1.1508
  0.420  0.9474 1.0438

Compliance Alteration was first presented in Voice Coil Magazine, October 2024. Later the article became Open Access when AudioXpress released an `online version January 2025 <https://audioxpress.com/article/bass-reflex-alignments-compliance-alteration>`_. It can be applied to any target response function of your choice. This method is particularly interesting if your driver :math:`\qts` is a bit too high, because with the compliance alteration technique, the box calculation is then treated as if the suspension is a bit too stiff. Fortunately, the driver suspension will experience aging (or burn-in) over time and will soften. When this happens, the provided equations dictate that your system will, over time, move toward the desired target response, and if softened enough to reach :math:`Q_\mathrm{Tref}`, it drops into place and becomes a correct response without any error.

Generalized quasi-alignments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a design process based on alignments, we consider :math:`(\ql,\qt)` as given inputs and :math:`(\alpha,h)` as output parameters to be computed by the alignment. Since we have two free parameters, it follows that we can specify only two of the three values :math:`(A_1,A_2,A_3)`. The approach taken is to relax (i.e., ignore) the condition on :math:`A_3`; that is, we match the behaviour in the pass-band :math:`(A_1)` and mid-band :math:`(A_2)` but **not** the stop-band :math:`(A_3)`. This is described in more detail for so-called QB3 (although we prefer B4Q because the order of the filter is 4) lossless case by Benson :cite:`benson:1993` (page 188).

By defining :math:`G = \left( \alpha+1+h^2 \right)/h`, we can rewrite these two conditions as

.. math::
  \begin{eqnarray}
  A_1 &=& \frac{q^2}{h} - 2G + \epsilon^2 q^2 h \; , \\
  A_2 &=& \left( G + \epsilon q^2 \right)^2 + 2-2q^2\left[ 1+\epsilon^2+\epsilon (h+1/h) \right] \; .
  \end{eqnarray}

where :math:`q = 1/\qt` and :math:`\epsilon = \qt/\ql \ll 1` is a small parameter.

**Recursive solution**

In the limit :math:`\epsilon = 0`, we can solve explicitly for :math:`(G,h)`, and this uniquely determines :math:`(\alpha,h)`. However, an explicit solution is not possible in the case :math:`\epsilon >  0`. But since :math:`\epsilon` is small, we expect the following recursion to converge in a few iterations:

.. math::
   \begin{eqnarray}
   G &=& -\epsilon q^2 + \sqrt{A_2-2+2q^2 \left[ 1+\epsilon^2+\epsilon\left(h+1/h\right)\right]} \\
   h &=& \frac{q^2}{2G + A_1-\epsilon^2 q^2 h}
   \end{eqnarray}

Once converged, we can obtain :math:`\alpha` according to

.. math::
   \alpha = Gh-\left(1+h^2\right)

Finally, note that by setting :math:`\epsilon=0` above we obtain the lossless solution explicitly.

**Source code**

.. code-block:: python

  import numpy as np

  def quasi(Ql,Qt,A1,A2):

     q = 1/Qt
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

  print('            BL4Q           LR4Q           B4Q')
  print(' Qt      h    alpha     h    alpha     h    alpha ')
  print('-----  -------------  -------------  -------------')

  for Qt in Qtvec:
     h1,alpha1 = quasi(Ql,Qt,1.464,1.286)
     h2,alpha2 = quasi(Ql,Qt,0.0,2.0)
     h3,alpha3 = quasi(Ql,Qt,0.0,0.0)

     print('{:.3f}  {:.4f} {:.4f}  {:.4f} {:.4f}  {:.4f} {:.4f}  '
           .format(Qt,h1,alpha1,h2,alpha2,h3,alpha3))


**Output**

::

             BL4Q           LR4Q           B4Q
   Qt      h    alpha     h    alpha     h    alpha
  -----  -------------  -------------  -------------
  0.310  1.0341 2.3819  1.1887 2.7969  1.2505 2.6469
  0.320  0.9972 2.1634  1.1505 2.5657  1.2146 2.4150
  0.330  0.9626 1.9648  1.1146 2.3551  1.1809 2.2038
  0.340  0.9300 1.7838  1.0808 2.1629  1.1493 2.0109
  0.350  0.8994 1.6185  1.0489 1.9869  1.1197 1.8342
  0.360  0.8704 1.4670  1.0188 1.8253  1.0918 1.6719
  0.370  0.8431 1.3279  0.9902 1.6767  1.0656 1.5225
  0.380  0.8172 1.1999  0.9631 1.5396  1.0409 1.3846
  0.390  0.7927 1.0819  0.9374 1.4130  1.0175 1.2571
  0.400  0.7694 0.9727  0.9130 1.2957  0.9955 1.1389

In Speakerbench, when we apply this method, the alignment acronym is followed by a 'Q' as in B4Q, LR4Q and BL4Q. Be aware, the B4Q in Speakerbench is the same as what is known in classical theory as the QB3 alignment.

Note: Bullock :cite:`bullock:1981` defines SQB3 as a continuation of the QB3 alignment, but for drivers with :math:`\qt > 0.4` and up to 0.56.

This particular implementation of the Quasi algorithm was first presented in Voice Coil Magazine, January 2025.

A special (discrete) alignment named the Inter-Order Butterworth (IB4) alignment was described by Thiele. This is a special case of the B4Q alignments, and we describe this in its own section: :ref:`The IB4 Bass Reflex Alignment`.

.. toctree::
   :caption: Quasi Alignment Resources
   :hidden:

   ib4


Alignment families
------------------

Beyond discrete aligments, for which :math:`(a_1,a_2,a_3)` have explicit numerical values, well-known **alignment families** exist for which :math:`(a_1,a_2,a_3)` depend upon a free parameter. An alignment family allows one to cover a range of driver :math:`\qts` values rather than just a single value. The B4Q quasi-alignment described above is in the loudspeaker industry considered an alignment family. Small and others refer to this family as QB3 (references).


Chebyshev C4
^^^^^^^^^^^^

Perhaps the most remarkable of all vented alignments is the Chebyshev (C4) method. The Chebyshev alignment for loudspeakers was exploted as early as 1956 by F.J. van Leeuwen, a Dutch engineer. These alignments have also been discussed by Thiele and Small, and in detail by Benson following the treatment by Weinberg (expand). It is named after Pafnuty Chebyshev because the amplitude response can be written in terms of the Chebyshev polynomial of the first kind. Consider the 4th-order low-pass case,

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{1}{1+\varepsilon^2 T_4^2 (\omega/\omega_0)}

where

.. math::
   T_4(x) = 8 x^4 - 8 x^2 + 1 \quad \text{such that} \quad T_4(\cos\theta) = \cos(4\theta)

Thus, in the region :math:`|\omega| \le 1` the properties of polynomial ensure that the amplitude is bounded by   

.. math::
   \frac{1}{1+\varepsilon^2} \le \left| H(j \omega_n) \right| \le 1 

The value of :math:`\epsilon` thus determines the **passband ripple** and provides the degree of freedom required for drivers of varying :math:`\qts`.

.. math::
   \left| H(s) \right|^2 = \frac{1 + \epsilon^2} {1 + \epsilon^2 \cdot T_4(1/s)^2 } ,



.. code-block:: python

   import numpy as np

   Ql = 10
   qts = 0.48     # Change this to suit your driver
   h = 0.0        # Initialization
   e = qts/Ql
   z = 8*(1+np.sqrt(2))*qts**2
   a0 = z-1
   b0 = z*(np.sqrt(8)-1)-6
   c0 = -1
   x = (-b0+np.sqrt(b0**2-4*a0*c0))/(2*a0)

   x0 = 1e6       # initialization
   tol = 1e-8     # Iteration condition
   while abs(x-x0) > tol:
      x0 = x

      # Compute D,P,Q,dP,dQ,dW
      d  = (x**2+6*x+1)/8
      p  = (1-(1-x)/np.sqrt(8))/np.sqrt(d)
      q  = qts**2*x*(4+np.sqrt(8))/np.sqrt(d)
      dp = e*(p**2-1)/(1-e*p)
      dq = 0.5*(-(q+2*e)+np.sqrt((q-2*e)**2-4*e**2))
      dw = q*dp+p*dq+dp*dq

      # Define quadratic coefficients including perturbation dw
      a = a0+dw
      b = b0+6*dw
      c = c0+dw
      x = (-b+np.sqrt(b**2-4*a*c))/(2*a)

   if np.isreal(x):       # ensure b**2 > 4*a*c
      if x>0:             # ensure x > 0
         k = np.sqrt(x)   # outside qt-range, this runs into negative x-values
         h = q+dq
         a2 = (1+x*(1+np.sqrt(2)))/np.sqrt(d)
         alpha = -(1+h**2)-e*h/qts**2+a2*h
         K = 1/k**2 - 1   # calculate ripple, just curious
         dB_ripple = 10 * np.log10(1 + K**4 / (64 + 28*K + 80*K**2 + 16*K**3))

Boombox
.......

The Boombox family of alignments was first described by W.J.J. Hoge (1976). This alignment is incredibly simple. The simplicity stems from the definition that the 4\ :sup:`th`-order polynomial, which describes the response function, is defined as two **identical** cascaded 2\ :sup:`nd`-order polynomials. This reduces the math to a 1-parameter family of responses, and it is equally as simple as calculating a closed box. The response function:

.. math::
   G(s) = \frac{ s^4 } { (s^2 + 2 \cdot \zeta \cdot s + 1)^2 }

where :math:`\zeta` is the damping ratio, which is a value that depends on the driver's :math:`\qts`-value. If the system is calculated as lossless, then :math:`\zeta = 1 / (4 \cdot \qts)`. For calculation of a bass reflex box and its parameters, :math:`\alpha` and :math:`h`, we follow the algorithm below:

.. code-block:: python

    Ql = 10
    Qts = 0.367
    h = 1
    alpha = 1/4 * (1/Qts - 1/Ql)**2

In the above code, insert whatever :math:`\ql` and :math:`\qts` values you wish to compute for. The :math:`h` output parameter is always 1 for the boombox alignment, by definition.

It is worth noting that if :math:`\qts = \ql`, then we have a discontinuity (:math:`\alpha = 0`). A low :math:`\ql`-value equivalent to a driver :math:`\qts` value seems quite inappropriate for bass reflex, and in practice, it is reasonable to expect that :math:`\ql` is always much larger than :math:`\qts`. The lowest :math:`\ql`-value that Bullock :cite:`bullock:1981` presents is 3, but even that is border-lining exceptionally bad; meanwhile, one would be hard-pressed to find a driver with :math:`\qts = 3` (it could be reached with significant DC resistance in series with the driver, but only if the driver's :math:`\qms`-value is even higher).

Hoge was focused on a suitable alignment for instrument loudspeakers, e.g., for electric guitars, and was seeking a better bass reflex alignment option for the high :math:`\qts`-drivers of the time than the classical Chebyshev C4-alignment. Choosing to cascade two identical 2\ :sup:`nd`-order polynomials gives double poles and therefore a nicer group delay with a reasonably fast settling time for an impulse. Unfortunately, this alignment always creates a peak before roll-off, and Hoge, who is a witty person, named it the Boombox alignment, or BB4.

Hoge only defined the BB4 alignment for driver :math:`\qts` above ca. 0.37, and he identified the peak with :math:`\ql = 7` for a driver :math:`\qts = 0.72` to be around +6 dB. For high :math:`\qts` drivers, the peak becomes large, which you might accept in favor of the impulse stopping quicker than a similar peaky Chebyshev response. Besides, the single peak of a BB4 alignment is easier to equalize electronically, than the ripples of a Chebyshev alignment. On the other hand, a Chebyshev alignment with a similar driver :math:`\qt` results in 1.3 - 1.4 dB ripple. Finally, when driver :math:`\qts` is this high, one may consider a large closed box.

Bullock realized that the equations also work well for drivers with lower :math:`\qts`, and in this case there is no peak in the frequency response. He coined the term Sub-Boombox for these alignments, or SBB4, and his tables go as low as :math:`\qts = 0.20`. It is therefore reasonable to say that the BB4-SBB4 alignment works for driver :math:`\qts` in the range of 0.20-0.72, although mathematically you are free to calculate outside these limits.

The Boombox family of alignments is home to at least two discrete alignments, that we are aware of. One of them is the Linkwitz-Riley (LR4) alignment, which is described in its own section: :ref:`The LR4 Bass Reflex Alignment`, the other is the Critically Damped (CD4) alignment, which is described in its own section: :ref:`The CD4 Bass Reflex Alignment`.

.. toctree::
   :caption: Boombox Alignment Resources
   :hidden:

   lr4
   cd4

Transitional Alignments
.......................

To the best of our knowledge, the concept of Transitional Alignments was never explored in relation to loudspeaker (Bass Reflex) boxes until it was presented in the Voice Coil Magazine, September 2024. Later the article became Open Access when AudioXpress released an
`online version December 2024 <https://audioxpress.com/article/transitional-bass-reflex-alignments>`_.

Notably, R. M. Golden and J. F. Kaiser :cite:`golden:1971` described the roots of normalized Butterworth and Bessel-Thomson low-pass transfer functions, from which Richard Small :cite:`small:1973c` derived the polynomial coefficients of the fourth-order highpass Bessel alignment. Golden and Kaiser also described a transitional filter design where a chosen balance between the two is realized.

Speakerbench supports a transitional alignment family, which transitions between Butterworth and Linkwitz-Riley, named B4-LR4.

**How it works**

Studying the poles of the polynomial transfer function in the s-plane, we know that the LR4 response function has two double poles, located at :math:`\Theta = \pm 3/4 \pi` (:math:`\pm 135 \deg`), whereas the B4 response function has equally spaced poles, located at :math:`\Theta = 5/8 \pi`, :math:`7/8 \pi`, :math:`9/8 \pi`, and :math:`11/8 \pi` (45 degrees apart).

We can write a one-parameter family of alignments that contains both B4 and LR4 as specific cases. Consider:

.. math::
   a_1 &= 2 \cdot \sqrt{2} \cdot \cos(\epsilon) \\
   a_2 &= 4 \cdot (\cos(\epsilon))^2 \\
   a_3 &= a_1

where :math:`\epsilon` is an angle for which :math:`0 \leq \epsilon \leq
\pi/8`. Geometrically, :math:`\epsilon` is an angle for which the four
distinct poles of the response function lie on the unit circle at
:math:`s = e^{i \Theta}` at :math:`\Theta = 3/4 \pi \pm \epsilon` and
:math:`\Theta = -3/4 \pi \pm \epsilon`. We can see that for
:math:`\epsilon = 0`, we have the LR4 response function, and for
:math:`\epsilon = \pi / 8`, we have the B4 response function.

.. code-block:: python

   import numpy as np

   Qt = 0.37    # insert your driver Qt value here
   Ql = 100
   a1 = 1./Qt + 1./Ql
   # cosepsilon should be between
   # cos(0) = 1 and cos(pi/8) = 0.924
   cosepsilon = a1/np.sqrt(8)
   a2 = 4 * cosepsilon**2
   a3 = a1
   h = 1
   alpha = a2 - 2 - 1/(Ql * Qt)

**Summary**

With the calculated transition from LR4 to B4, we have obtained a subtle improvement over continuing with the Boombox alignment. For drivers with :math:`\qts` values above the LR4-:math:`\qt`, the Boombox alignment will have a (small) peak in its frequency response before roll-off. By transitioning towards the B4 alignment, we avoid this peak, and the frequency response remains monotonic.

Note: Transitioning between B4 and LR4 is only relevant for drivers with :math:`\qts`-values between the two alignment, i.e., ca. :math:`0.37 < \qts < 0,40`. This implies that Speakerbench only shows this option if your driver's :math:`\qts`-value is within this range.

Speakerbench currently only supports one transitional alignment, the B4-LR4 presented above, but in the Alignment Chart you may aim with your pointer and click somewhere in-between the known alignments, and then in the Settings tab, you click the **APPLY** button to transfer the :math:`\alpha` and :math:`h` values into :math:`\vb` and :math:`\fp` values for box simulation. This way Speakerbench supports any transition you can think of. Just, clicking the chart is not as mathematically precise as what we have described here.

Second-order alignments
-----------------------

A second-order alignment is a closed box, not a vented box. Speakerbench supports the calculation of closed boxes simply by setting the port tuning frequency :math:`\fp = 0`, which is equivalent to :math:`h = \fp / \fs = 0`. We can write the normalized response function as

.. math::
   G_\mathrm{H}(s) = \frac{s^2}{s^2 + a_1 s + 1} = \frac{s^2}{s^2 + 2 \zeta s + 1} \; ,

where :math:`a_1` is 2 x the damping ratio :math:`\zeta`, which means :math:`a_1` is the inverse of the Q-factor, for the second-order system.

Without a port tuning frequency, a closed box system only has one free design parameter :math:`\alpha = \cms / \cmb = \vas / \vb`. Ignoring leakage loss, we may write :math:`\qtc = \qts \sqrt{\alpha + 1}` and :math:`\fcb = \fs \sqrt{\alpha + 1}`. There are two factors, which can affect the resulting system Q, one is any electrical resistance :math:`R_\mathrm{S}` in series with the driver, the other is leakage loss :math:`\ql`.

.. math::
   Q_\mathrm{T,R_S} = \frac{\ws \cdot \mms}{\frac{\bls}{\re + R_\mathrm{S}} + \rms}

The :math:`Q_\mathrm{T,R_S}` value is calculated in Speakerbench and you can see the value in the INFO tab. It is affected when you enable the filter and apply a series resistance. The :math:`Q_\mathrm{T,R_S}` value is what Speakerbench uses for response calculations (and in the alignment chart). The second-order response function becomes:

.. math::
   G_\mathrm{H}(s) = \frac{s^2}{s^2 + \frac{1}{Q_\mathrm{T,R_S}} s + 1 + \alpha} \; .

The leakage loss :math:`\ql` is normally not treated in classical alignment analysis for closed box systems, because leakage is typically kept insignificant when building a decent quality box, i.e., it does not affect the SPL response in a significant way. It is different for vented systems because in classical alignment analysis for vented box systems, :math:`\ql` is treated as a lumped parameter for several different losses. Nevertheless, whatever you have entered in :math:`\ql` in Speakerbench will be included in the response calculation. Therefore, you should set this fairly high, e.g. 30-50 or higher, when calculating a closed or vented box in Speakerbench. Since you can adjust losses separately in Speakerbench, also for vented systems, we recommend that you always set :math:`\ql` to its real physical value (a fairly high value). This will give you the most accurate prediction of the response (SPL and impedance, etc.).

In the Speakerbench alignment chart, there are two dots shown at :math:`h = 0`, which are representing the second-order Bessel (:math:`Q = 1 / \sqrt{3} \approx 0.577`) and Butterworth (:math:`Q = 1 / \sqrt{2} \approx 0.707`), respectively. These are useful when designing vented box systems, in which the user may plug the port, essentially converting the system into a closed box design. In principle, one could also show other known alignments, e.g., the second-order Linkwitz-Riley (:math:`Q = 0.5`), but targets outside the range between Bessel and Butterworth are rarely used when designing vented box systems. In other words, the box volume of a vented box system (:math:`\alpha`) is typically chosen such that the driver in box :math:`Q` is between the Bessel and the Butterworth second-order alignment. This observation is almost valid even for the extreme case of a CD4 alignment, where in practice the box volume when the port is closed will give a system :math:`Q \approx 0.55` (the exact value depend on leakage :math:`\ql`). Any second order response where the system :math:`Q > 0.707` is considered a Chebyshev C2 alignment, even if there is not any 'equal' ripple since a second-order response will just have a peak.

In classical theory, a closed box is considered of the acoustic suspension type when :math:`\cmb` dominates over :math:`\cms` such that :math:`\fcb \geq 2 \fs`, which gives :math:`\alpha \geq 3`.

Summary
--------

.. csv-table:: **Table of supported discrete alignments and alignment families**
   :header: "Tag", "Name", "Comments"
   :widths: 25, 25, 50

   "B4i - B4Q - B4CA",  "Butterworth",   "Centered around :math:`\qts = 0.40`"
   "LR4Q - LR4CA",  "Linkwitz-Riley",    "Centered around :math:`\qts = 0.37`"
   "BL4Q - BL4CA",  "Bessel",            "Centered around :math:`\qts = 0.33`"
   "CD4Q - CD4CA",  "Critically damped", "Centered around :math:`\qts = 0.26`"
   "IB4Q - IB4CA",  "Inter-order Butterworth",  "Centered around :math:`\qts = 0.34`"
   "C4 - SC4",      "Chebyshev",         "For :math:`0.236 < \qts < 1.416`"
   "BB4 - SBB4",    "Boombox",           "For :math:`0.20 < \qts < 0.75`"
   "B4-LR4", "Transitional B4-LR4",      "For :math:`0.37 < \qts < 0.40`"
   "B2",  "Butterworth 2\ :sup:`nd` order", "Closed box, :math:`\qtc = 0.707` (requires :math:`\qts < 0.67)`"
   "BL2", "Bessel 2\ :sup:`nd` order",      "Closed box, :math:`\qtc = 0.577` (requires :math:`\qts < 0.55)`"

Note: In Speakerbench the Quasi IB4 (IB4Q) only shows up if :math:`\qts` is close to the target, and since it is identical to B4Q (=QB3), the two will be located at the same spot in the alignment chart. IB4CA is unique and is always shown.
