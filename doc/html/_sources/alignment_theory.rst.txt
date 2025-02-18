.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

.. _alignment_theory:

Classic Vented Alignments
=========================

In classical loudspeaker theory from the 1960s and onwards, the concept of alignments was developed to provide a systematic prescription for choosing box volume and port tuning to yield a target low-frequency response function.

History and framework
---------------------

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4th-order bass-reflex alignments. These alignments are particular types of 4th-order high-pass filters. Following Small :cite:`small:1973c` (Eq. 57) we can write the normalized response function as

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + a_1 s^3 + a_2 s^2 + a_3 s + 1} \; ,

where :math:`s = j \omega / \omega_0` is the dimensionless complex frequency variable normalized to :math:`\omega_0 \doteq \sqrt{\omega_B \, \omega_S}`. In the first part of his article series, Small :cite:`small:1973c` (Eqs. 22--24) writes the lossy box filter coefficients as

.. math::
   \begin{eqnarray}
   \displaystyle
   a_1 &=& \frac{Q_L + h \: Q_T}{\sqrt{h} \: Q_L \: Q_T} \nonumber \\
   a_2 &=& \frac{h + (\alpha + 1 + h^2) \: Q_L \: Q_T}{h \: Q_L \: Q_T}\nonumber \\
   a_3 &=& \frac{h \: Q_L + Q_T}{\sqrt{h} \: Q_L \: Q_T} \; ,\label{eq:box}
   \end{eqnarray}

where :math:`Q_L` is the leakage-loss :math:`Q` of the box and :math:`Q_T` is the total :math:`Q` of the driver. Here, :math:`\omega_B/\omega_S` is the system tuning ratio and :math:`\alpha = V_{AS} / V_B` is the ratio of the compliance volume to the box volume. We remark that the coefficients are approximate and neglect myriad other terms which appear in a more comprehensive model of a vented box. These missing terms would represent more complex losses in the box and in the driver suspension system, driver inductance and semi-inductance, and so on. In the definition of :math:`\omega_0`, :math:`\omega_S` is the driver resonant frequency and :math:`\omega_B` is the vent resonant frequency. This normalization is equivalent to setting :math:`T_0=1` in Small's expressions. The magnitude-versus-frequency behavior is also given in Small :cite:`small:1973c` (Eqs. 58 and 59), which we reproduce here as

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + A_1 \omega^6 + A_2 \omega^4 + A_3 \omega^2 + 1} \; ,

where

.. math::
  \begin{eqnarray}
  A_1 &=& a_1^2-2 a_2 \; , \\
  A_2 &=& a_2^2+2-2 a_1 a_3 \; , \\
  A_3 &=& a_3^2-2 a_2 \; .
  \end{eqnarray}

We summarize the values for :math:`A_i` for some classical alignments as well as :math:`Q_T` for the lossless case below

.. csv-table:: **Discrete Alignments Coefficients**
   :header: Filter, :math:`Q_T`, :math:`A_1`, :math:`A_2`, :math:`A_3`
   :widths: 16, 6, 5, 5, 5
   :align: center

   Butterworth (B4), 0.383, 0, 0, 0
   Linkwitz-Riley (LR4), 0.354, 0, 2, 0
   Bessel (BL4), 0.316, 1.464, 1.286, 0.976

Butterworth filters have :math:`A_1=A_2=A_3=0` which gives the mathematical feature of *maximal flatness*.

Since these respective alignments are possible only for a single value of :math:`Q_T`, a procedure is required to extend (or approximate) them for a continuous range of :math:`Q_T`.

1. Method of ignorance
----------------------

When targeting one of the discrete alignments, it is unlikely (almost impossible) that you will have a driver available at hand, which fits the required :math:`Q_T` value exactly. The simplest solution is to ignore this fact and continue designing the speaker as if there is a perfect match. This we call the method of ignorance, because you ignore the fact that :math:`Q_T` isn't matched perfectly.

In Speakerbench, when we apply this method, the alignment acronym is followed by an 'i' as in B4i, LR4i and BL4i.

**Source code**

.. code-block:: python

   import numpy as np

   Ql=10
   Qtvec=[0.34,0.35,0.36,0.37,0.38,0.39,0.40]

   # Butterworth B4 (from theory)
   Qt = 1./(1./np.cos(3*np.pi/8)-1./Ql)
   h_ref = 1
   a3 = np.sqrt(8)*np.cos(np.pi/8)
   alpha_ref = np.sqrt(2) - (1/Ql**2) * (a3*Ql-1)

   print('            B4i ')
   print(' Qt      h    alpha ')
   print('-----  ------------- ')

   for Qt in Qtvec:
      print('{:.3f}  {:.4f} {:.4f}  '
            .format(Qt,h_ref,alpha_ref))

**Output**

::

              B4i
   Qt      h    alpha
  -----  -------------
  0.340  1.0000 1.1629
  0.350  1.0000 1.1629
  0.360  1.0000 1.1629
  0.370  1.0000 1.1629
  0.380  1.0000 1.1629
  0.390  1.0000 1.1629
  0.400  1.0000 1.1629

It can be observed that :math:`h` and :math:`\alpha` are completely
unaffected by the change in  :math:`Q_T`, i.e., the fact that
:math:`Q_T` is not correct, in this example for the Butterworth B4
alignment, is simply ignored.

2. Compliance Alteration
------------------------

Another approach to handling the situation where the driver :math:`Q_T` isn't matched perfectly, is to assume the misalignment (or error) is due to the driver suspension being either too soft or too stiff, i.e., that the driver compliance is imagined to be altered such that the target :math:`Q_T` value for the target alignment is met.

Compliance Alteration is computed by first 1) Calculating the reference :math:`Q_{Tref}` for your target and the resulting :math:`\alpha_{ref}` and :math:`h_{ref}`, then 2) shift :math:`\alpha` and :math:`h` relative to the :math:`Q_T` for the actual driver at hand in the following way:

.. math::
   \begin{eqnarray}
   \alpha &=& \alpha_{ref} \cdot \Big( \frac{Q_{Tref}}{Q_T} \Big)^2 \; , \\
   h &=& h_{ref} \cdot \frac{Q_{Tref}}{Q_T} \; .
   \end{eqnarray}

In Speakerbench, when we apply this method, the alignment acronym is followed by 'CA' as in B4CA, LR4CA and BL4CA.

**Source code**

.. code-block:: python

  import numpy as np

  def ca_shift(Qtref,Qt,aref,href):

     h = href * Qtref/Qt
     alpha = aref * (Qtref/Qt)**2
     return h,alpha

  Ql = 10
  Qts = 0.42    # for example

  # Butterworth B4 (from theory)
  Qt_ref = 1./(1./np.cos(3*np.pi/8)-1./Ql)
  h_ref = 1
  a3 = np.sqrt(8)*np.cos(np.pi/8)
  alpha_ref = np.sqrt(2) - (1/Ql**2) * (a3*Ql-1)

  h,alpha = ca_shift(Qt_ref,Qts,alpha_ref,h_ref)

  print('           B4CA')
  print(' Qts     h    alpha ')
  print('-----  -------------')
  print('{:.3f}  {:.4f} {:.4f}  '
        .format(Qts,h,alpha)   )

**Output**

::

             B4CA
   Qt      h    alpha
  -----  -------------
  0.420  0.9474 1.0438

Compliance Alteration was first presented in Voice Coil Magazine, October
2024. Later the article became Open Access when AudioXpress released an
`online version January 2025 <https://audioxpress.com/article/bass-reflex-alignments-compliance-alteration>`_.
It can be applied to any target response function of
your choice. This method is particularly interesting if your driver
:math:`Q_T` is a bit too high, because with the compliance alteration
technique, the box calculation is then treated as if the suspension is a
bit too stiff. Fortunately, the driver suspension will experience aging
(or burn-in) over time and will soften. When this happens, the provided
equations dictate that your system will, over time, move toward the
desired target response, and if softened enough to reach
:math:`Q_{Tref}`, it drops into place and becomes a correct response
without any error.

3. Generalized quasi-alignments
-------------------------------

In a design process based on alignments, we consider :math:`(Q_L,Q_T)`
as given inputs and :math:`(\alpha,h)` as output parameters to be
computed by the alignment. Since we have two free parameters, it follows
that we can specify only two of the three values :math:`(A_1,A_2,A_3)`.
The approach taken is to relax (i.e., ignore) the condition on
:math:`A_3`; that is, we match the behaviour in the pass-band
:math:`(A_1)` and mid-band :math:`(A_2)` but **not** the stop-band
:math:`(A_3)`. This is described in more detail for so-called QB3
(although we prefer B4Q because the order of the filter is 4) lossless
case by Benson :cite:`benson:1993` (page 188).

By defining :math:`G = \left( \alpha+1+h^2 \right)/h`, we can rewrite these two conditions as

.. math::
  \begin{eqnarray}
  A_1 &=& \frac{q^2}{h} - 2G + \epsilon^2 q^2 h \; , \\
  A_2 &=& \left( G + \epsilon q^2 \right)^2 + 2-2q^2\left[ 1+\epsilon^2+\epsilon (h+1/h) \right] \; .
  \end{eqnarray}

where :math:`q = 1/Q_T` and :math:`\epsilon = Q_T/Q_L \ll 1` is a small parameter.

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

In Speakerbench, when we apply this method, the alignment acronym is
followed by a 'Q' as in B4Q, LR4Q and BL4Q. Be aware, the B4Q in
Speakerbench is the same as what is known in classical theory as the QB3
alignment.

Note: Bullock defines SQB3 as a continuation of the QB3 alignment, but
for drivers with :math:`Q_T > 0.4` and up to 0.56.

A special (discrete) alignment named the Inter-Order Butterworth (IB4)
alignment was described by Thiele. This is a special case of the B4Q
alignments, and we describe this in its own section:
:ref:`The IB4 Bass Reflex Alignment`.

.. toctree::
   :caption: Quasi Alignment Resources
   :hidden:

   ib4

Summary
-------

We have presented three methods to cope with the (quite normal) situation that the :math:`Q_T` for your driver does not match the target response exactly. For example, consider the 4th order Butterworth, we have the B4i, B4Q (=QB3), as well as the B4CA method. With the three methods in mind, you can study their location in the Alignment Chart. The three methods will converge to a single point as your driver :math:`Q_T` approaches the :math:`Q_T` value for the target respone. On the other hand, when your driver :math:`Q_T` is far away from the :math:`Q_T` for the target response, the three methods will be far away from each other.

If you wish to target something rather exact, then choose an alignment where the three methods are close, ideally they overlap.

If you can accept deviation from your target alignment, consider studying what you get from each of the three methods, and go for a method which reflects your target performance, or go for a compromise (i.e., choose something in-between the parameters proposed by the methods).

Chebyshev
---------

Should we write something about this?

Boombox
-------

The Boombox family of alignments was first described by W.J.J. Hoge
(1976). This alignment is incredibly simple. The simplicity stems from
the definition that the 4th-order polynomial, which describes the
response function, is defined as two **identical** cascaded 2nd-order
polynomials. This reduces the math to a 1-parameter family of responses,
and it is equally as simple as calculating a closed box. The response
function:

.. math::
   G(s) = \frac{ s^4 } { (s^2 + 2 \cdot \zeta \cdot s + 1)^2 }

where :math:`\zeta` is the damping ratio, which is a value that depends
on the driver's :math:`Q_T`-value. If the system is calculated as
lossless, then :math:`\zeta = 1 / (4 \cdot Q_T)`. For calculation of a
bass reflex box and its parameters, :math:`\alpha` and :math:`h`, we
follow the algorithm below:

.. code-block:: python

    Ql = 10
    Qt = 0.367
    h = 1
    alpha = 1/4 * (1/Qt - 1/Ql)**2

In the above code, insert whatever :math:`Q_L` and :math:`Q_T` values
you wish to compute for. The :math:`h` output parameter is always 1 for
the boombox alignment, by definition.

It is worth noting that if :math:`Q_T = Q_L`, then we have a
discontinuity (:math:`\alpha = 0`). A low :math:`Q_L`-value equivalent
to a driver :math:`Q_T` value seems quite inappropriate for bass reflex,
and in practice, it is reasonable to expect that :math:`Q_L` is always
much larger than :math:`Q_T`. The lowest :math:`Q_L`-value that Bullock
(1) presents is 3, but even that is border-lining exceptionally bad;
meanwhile, one would be hard-pressed to find a driver with :math:`Q_T =
3` (it could be reached with significant DC resistance in series with
the driver, but only if the driver's :math:`Q_M`-value is even higher).

Hoge was focused on a suitable alignment for instrument loudspeakers,
e.g., for electric guitars, and was seeking a better bass reflex
alignment option for the high :math:`Q_T`-drivers of the time than the
classical Chebyshev C4-alignment. Choosing to cascade two identical
2nd-order polynomials gives double poles and therefore a nicer group
delay with a reasonably fast settling time for an impulse.
Unfortunately, this alignment always creates a peak before roll-off, and
Hoge, who is a witty person, named it the Boombox alignment, or BB4.

Hoge only defined the BB4 alignment for driver :math:`Q_T` above ca.
0.37, and he identified the peak with :math:`Q_L = 7` for a driver
:math:`Q_T = 0.72` to be around +6 dB. For high :math:`Q_T` drivers, the
peak becomes large, which you might accept in favor of the impulse
stopping quicker than a similar peaky Chebyshev response. Besides, the
single peak of a BB4 alignment is easier to equalize electronically,
than the ripples of a Chebyshev alignment. On the other hand, a
Chebyshev alignment with a similar driver Qt results in 1.3 - 1.4 dB
ripple. Finally, when driver :math:`Q_T` is this high, one may consider
a large closed box.

Bullock realized that the equations also work well for drivers with
lower :math:`Q_T`, and in this case there is no peak in the frequency
response. He coined the term Sub-Boombox for these alignments, or SBB4,
and his tables go as low as :math:`Q_T = 0.20`. It is therefore
reasonable to say that the BB4-SBB4 alignment works for driver
:math:`Q_T` in the range of 0.20-0.72, although mathematically you are
free to calculate outside these limits.

The Boombox family of alignments is home to at least two discrete
alignments, that we are aware of. One of them is the Linkwitz-Riley
(LR4) alignment, which is described in its own section:
:ref:`The LR4 Bass Reflex Alignment`, the other is the Critically Damped
(CD4) alignment, which is is described in its own section:
:ref:`The CD4 Bass Reflex Alignment`.

.. toctree::
   :caption: Boombox Alignment Resources
   :hidden:

   lr4
   cd4

Transitional Alignments
-----------------------

To the best of our knowledge, the concept of Transitional Alignments was
never explored in relation to loudspeaker (Bass Reflex) boxes until it
was presented in the Voice Coil Magazine, September 2024.

Notably, R. M. Golden and J. F. Kaiser [1] described the roots of
normalized Butterworth and Bessel-Thomson low-pass transfer functions,
from which Richard Small [2] derived the polynomial coefficients of the
fourth-order highpass Bessel alignment. Golden and Kaiser also described
a transitional filter design where a chosen balance between the two is
realized.

Speakerbench supports a transitional alignment family, which transitions
between Butterworth and Linkwitz-Riley, named B4-LR4.

**How it works**

Studying the poles of the polynomial transfer function in the s-plane,
we know that the LR4 response function has two double poles, located at
:math:`\Theta = \pm 3/4 \pi` (:math:`\pm 135 \deg`), whereas the B4
response function has equally spaced poles, located at :math:`\Theta =
5/8 \pi`, :math:`7/8 \pi`, :math:`9/8 \pi`, and :math:`11/8 \pi` (45
degrees apart).

We can write a one-parameter family of alignments that contains both B4
and LR4 as specific cases. Consider:

.. math::
   a_1 &= 2 \cdot \sqrt(2) \cdot \cos(\epsilon) \\
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

With the calculated transition from LR4 to B4, we have obtained a subtle
improvement over continuing with the Boombox alignment. For drivers with
:math:`Q_T` values above the LR4-Qt, the Boombox alignment will have a
(small) peak in its frequency response before roll-off. By transitioning
towards the B4 alignment, we avoid this peak, and the frequency response
remains monotonic.

Note: Transitioning between B4 and LR4 is only relevant for drivers with
:math:`Q_T`-values between the two alignment, i.e., ca. :math:`0.37 <
Q_T < 0,40`. This implies that Speakerbench only shows this option if
your driver's :math:`Q_T`-value is within this range.

Speakerbench currently only supports one transitional alignment, the
B4-LR4 presented above, but in the Alignment Chart you may aim with your
pointer and click somewhere in-between the known alignments, and then in
the Settings tab, you click the **APPLY** button to transfer the
:math:`\alpha` and :math:`h` values into :math:`V_B` and :math:`f_P`
values for box simulation. This way Speakerbench supports any transition
you can think of. Just, clicking the chart is not as mathematically
precise as what we have described here.

Overview
--------

.. csv-table:: **Table of supported discrete alignments and alignment families**
   :header: "Tag", "Name", "Comments"
   :widths: 25, 25, 50

   "B4i - B4Q - B4CA",  "Butterworth",   "Centered around :math:`Q_T = 0.40`"
   "LR4Q - LR4CA",  "Linkwitz-Riley",    "Centered around :math:`Q_T = 0.37`"
   "BL4Q - BL4CA",  "Bessel",            "Centered around :math:`Q_T = 0.33`"
   "CD4Q - CD4CA",  "Critically damped", "Centered around :math:`Q_T = 0.26`"
   "IB4Q - IB4CA",  "Inter-order Butterworth",  "Centered around :math:`Q_T = 0.34`"
   "C4 - SC4",      "Chebyshev",         "For :math:`0.236 < Q_T < 1.416`"
   "BB4 - SBB4",    "Boombox",           "For :math:`0.20 < Q_T < 0.75`"
   "B4-LR4", "Transitional B4-LR4",      "For :math:`0.37 < Q_T < 0.40`"
   "B2",  "Butterworth 2\ :sup:`nd` order", "Closed box, :math:`Q_{TC} = 0.71` (requires :math:`Q_T < 0.67)`"
   "BL2", "Bessel 2\ :sup:`nd` order",      "Closed box, :math:`Q_{TC} = 0.58` (requires :math:`Q_T < 0.55)`"

Note: In Speakerbench the Quasi IB4 (IB4Q) only shows up if :math:`Q_T` is
close to the target, and since it is identical to B4Q (=QB3), the two
will be located at the same spot in the alignment chart. IB4CA is unique
and is always shown.
