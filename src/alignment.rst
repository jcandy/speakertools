Alignments
==========

Basic theory
------------

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4th-order bass-reflex alignments. These alignments are particular types of 4th-order high-pass filters. Following Small :cite:`small:1973c` (Eq. 57) we can write the normalized response function as 

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + a_1 s^3 + a_2 s^2 + a_3 s + 1} \; ,

where :math:`s` is the dimensionless complex frequency variable normalized to :math:`\omega_0 \doteq \sqrt{\omega_B \, \omega_S}`. In the first part of his article series, Small :cite:`small:1973c` (Eqs. 22--24) writes the lossy box filter coefficients as

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

Butterworth filters have :math:`A_1=A_2=A_3=0` which gives the mathematical feature of *maximal flatness*. We summarize the values for :math:`A_i` below

.. csv-table:: **Discrete Alignments Coefficients**
   :header: Filter, :math:`Q_T`, :math:`A_1`, :math:`A_2`, :math:`A_3`
   :widths: 16, 6, 5, 5, 5
   :align: center

   Butterworth (B4), 0.383, 0, 0, 0
   Linkwitz-Riley (LR4), 0.354, 0, 2, 0
   Bessel (BL4), 0.316, 1.464, 1.286, 0.976

Since these respective alignments are possible only for a single value of :math:`Q_T`, a procedure is required to extend (or approximate) them for a continuous range of :math:`Q_T`. 

Generalized quasi-alignments
----------------------------

In a design process based on alignments, we consider :math:`(Q_L,Q_T)` as given inputs and :math:`(\alpha,h)` as output parameters to be computed by the alignment. Since we have two free parameters, it follows that we can specify only two of the three values :math:`(A_1,A_2,A_3)`. The approach taken is to relax (i.e., ignore) the condition on :math:`A_3`; that is, we match the behaviour in the pass-band :math:`(A_1)` and mid-band :math:`(A_2)` but **not** the stop-band :math:`(A_3)`.

By defining :math:`\Gamma = \left( \alpha+1+h \right)/h`, we can rewrite these two conditions as

.. math::
  \begin{eqnarray}
  A_1 &=& \frac{q^2}{h} - 2\Gamma + \epsilon^2 q^2 h \; , \\
  A_2 &=& \left( \Gamma + \epsilon q^2 \right)+2-2q^2\left[ 1+\epsilon^2+\epsilon (h+1/h) \right] \; .
  \end{eqnarray}

where :math:`q = 1/Q_T` and :math:`\epsilon = Q_T/Q_L \ll 1` is a small parameter.

Recursive solution
------------------

In the limit :math:`\epsilon = 0`, we can solve explicitly for :math:`(\Gamma,h)`, and this uniquely determines :math:`(\alpha,h)`. However, an explicit solution is not possible in the case :math:`\epsilon >  0`. But since :math:`\epsilon` is small, we expect the following recursion to converge in a few iterations: 

.. math::
   \begin{eqnarray}
   \Gamma &=& -\epsilon q^2 + \sqrt{A_2-2+2q^2 \left[ 1+\epsilon^2+\epsilon\left(h+1/h\right)\right]}\\
        h &=& \frac{q^2}{2\Gamma + A_1-\epsilon^2 q^2 h}
   \end{eqnarray}

Once converged, we can obtain :math:`\alpha` according to

.. math::
   \alpha = h \Gamma-\left(1+h^2\right)

Finally, note that by setting :math:`\epsilon=0` above we obtain the lossless solution explicitly.

Source code:

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
  Qtvec=[0.34,0.35,0.36,0.37,0.38,0.39]

  print('QLR4')
  A1=0 ; A2=2
  for Qt in Qtvec:
     h,alpha = quasi(Ql,Qt,A1,A2)
     print('Qt={:.4f}, h={:.4f}, alpha={:.4f}'.format(Qt,h,alpha))

  print()
  print('QB4')
  A1=0 ; A2=0
  for Qt in Qtvec:
     h,alpha = quasi(Ql,Qt,A1,A2)
     print('Qt={:.4f}, h={:.4f}, alpha={:.4f}'.format(Qt,h,alpha))


Output

::

  QLR4
  Qt=0.3400, h=1.0808, alpha=2.1629
  Qt=0.3500, h=1.0489, alpha=1.9869
  Qt=0.3600, h=1.0188, alpha=1.8253
  Qt=0.3700, h=0.9902, alpha=1.6767
  Qt=0.3800, h=0.9631, alpha=1.5396
  Qt=0.3900, h=0.9374, alpha=1.4130

  QB4
  Qt=0.3400, h=1.1493, alpha=2.0109
  Qt=0.3500, h=1.1197, alpha=1.8342
  Qt=0.3600, h=1.0918, alpha=1.6719
  Qt=0.3700, h=1.0656, alpha=1.5225
  Qt=0.3800, h=1.0409, alpha=1.3846
  Qt=0.3900, h=1.0175, alpha=1.2571
   
..
   Speakerbench Suggested Alignments
   :header: Alignment, Description,:math:`Q_T` range
   :widths: 10, 20, 10 
   :align: center

   C4,     Chebyshev (extension of B4), :math:`0.24 < Q_T < 2.0`
   B4-CA,  B4 with compliance alteration, :math:`0.36 < Q_T < 0.56`
   B4-AM,  B4 with amplitude matching (same as QB3),  :math:`0.36 < Q_T < 0.56`
   LR4-CA, LR4 with compliance alteration, :math:`0.34 < Q_T < 0.4`
   LR4-AM, LR4 with amplitude matching, :math:`0.34 < Q_T < 0.4`
   BL4-CA, BL4 with compliance alteration, :math:`0.3 < Q_T < 0.36`
   BL4-AM, BL4 with amplitude matching, :math:`0.3 < Q_T < 0.36`
   
