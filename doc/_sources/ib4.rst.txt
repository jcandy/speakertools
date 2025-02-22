.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

=============================
The IB4 Bass Reflex Alignment
=============================

The Inter-Order Butterworth (IB4) alignment is rarely talked about. It
was mentioned briefly by Richard Small [2]. Bullock [3] published a
table for this discrete alignment, and the tables are reproduced in The
Loudspeaker Design Cookbook by Vance Dickason.

The IB4 alignment and the mathematics behind, was first presented in the
Voice Coil Magazine, July 2024. Later the article became Open Access
when AudioXpress released an `online version October 2024
<https://audioxpress.com/article/the-ib4-bass-reflex-alignment>`_.

The Calculation of IB4 Including Leakage Loss
---------------------------------------------

The fourth-order Inter-Order Butterworth high-pass filter is defined by
Thiele as a combination of a second-order and two identical first-order
filters:

.. math::
    G(s) = \frac{ s^4 } { (s^2 + 2 \cdot \kappa \cdot s + \lambda) \cdot (s + 1)^2 }

For our application, the polynomial must be manipulated into a suitable
normalized form for identification of the polynomial coefficients, which
is achieved when :math:`\kappa = \sqrt{2 \cdot (\sqrt{3} - 1)}` and
:math:`\lambda = \sqrt{3}`. With the mentioned special coefficients, the
polynomial coefficients :math:`a_1`, :math:`a_2`, and :math:`a_3` and
the normalized response function can be calculated. The reader is
reminded that the generalized expression for the response function is:

.. math::
    G(s) = \frac{ s^4 } { (s^4 + a_1 \cdot s^3 + a_2 \cdot s^2 + a_3 \cdot s + 1) }

The coefficients of the normalized polynomial based on :math:`\kappa`
and :math:`\lambda` are calculated in the algorithm below. Using Python,
we may calculate the IB4 alignment as follows:

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

   Ql = 10
   K = np.sqrt(2 * (np.sqrt(3) - 1))
   L = np.sqrt(3)
   a1 = (2 + K) / L**0.25
   a2 = (1 + 2 * K + L) / np.sqrt(L)
   a3 = (K + 2 * L) / L**0.75
   Qt_IB4 = 1/(np.sqrt(a1*a3) - 1/Ql)
   A1 = a1**2 - 2 * a2
   A2 = a2**2 + 2 - 2 * a1 * a3
   h, alpha = quasi(Ql, Qt_IB4, A1, A2)

where :math:`\qt` is not something you can specify yourself but is given
by the equations because the IB4 alignment is a discrete alignment.

For leakage :math:`\ql = \infty`, the driver :math:`\qt` that matches
the Inter-Order Butterworth response function is :math:`0.3398 \approx 0.34`.

**Summary**

The IB4 alignment is a specific case of the B4Q (=QB3) alignment, when
:math:`a_2 = 2.5004995097549222 + \sqrt{2}`. Pick any table of QB3
alignments and select the one for the specific driver :math:`\qt` value
that matches IB4, and you shall have the IB4 response function. This
way, there is nothing special about IB4; it is just a specific instance
of the QB3 alignments, but it is the specific one Thiele derived by
replacing a second-order polynomial with two (identical) first-order
polynomials, which places two of the poles on the real axis.

When :math:`\qt` is not matching the IB4 case exactly and given the
intimate relationship to the QB3 alignment, a simple solution is to use
the QB3 (=B4Q) alignment, where :math:`\qt` may be chosen freely.

We have previously discussed three approaches to dealing with discrete
alignments; the quasi-method, the compliance alteration method, as
well as the pure igorance method. Although IB4 is an instance of B4Q,
the three methods still apply. The quasi-approach will overlap B4Q, and
the IB4CA as well as IB4i still uniquely exist.

