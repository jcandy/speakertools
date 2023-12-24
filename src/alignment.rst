Alignments
==========

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4th-order alignments bass-reflex alignments. These alignments are simply particular types of 4th-order high-pass filters. Following Small :cite:`small:1973c` (Eq. 57) we can write the normalized response function as 

.. math::
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + a_1 s^3 + a_2 s^2 + a_3 s + 1} \; ,

where :math:`s` is the dimensionless complex frequency variable normalized to :math:`\omega_0 \doteq \sqrt{\omega_B \, \omega_S}`. In the definition of :math:`\omega_0`, :math:`\omega_S` is the driver resonant frequency and :math:`\omega_B` is the vent resonant frequency. This normalization is equivalent to setting :math:`T_0=1` in Small's expressions. The magnitude-versus-frequency behavior is also given in Small :cite:`small:1973c` (Eqs. 58 and 59), which we reproduce here as

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + A_1 \omega^6 + A_2 \omega^4 + A_3 \omega^2 + 1} \; ,

where

.. math::
  \begin{eqnarray}
  A_1 &=& a_1^2-2 a_2 \nonumber \\
  A_2 &=& a_2^2+2-2 a_1 a_3 \nonumber \\
  A_3 &=& a_3^2-2 a_2 \; .
  \end{eqnarray}

.. csv-table:: **Discrete Alignments**
   :header: Filter, :math:`Q_T`, :math:`A_1`, :math:`A_2`, :math:`A_3`
   :widths: 20, 6, 5, 5, 5

   Butterworth (B4), 0.383, 0, 0, 0
   Linkwitz-Riley (LR4), 0.354, 0, 2, 0
   Bessel (BL4), 0.316, 1.464, 1.286, 0.976

Since these respective alignments are possible only for a single value of :math:`Q_T`, a procedure is required to extend (or approximate) them for a continuous range of :math:`Q_T`. We use three alignment families which are based on the discrete alignments above.

.. csv-table:: **Speakerbench Continuous Alignments**
   :header: Abbreviation, Description,:math:`Q_T`
   :widths: 13, 20, 10 

   C4,     Chebyshev (extension of B4), :math:`0.24 < Q_T < 2.0`
   B4-CA,  B4 with compliance alteration, :math:`0.36 < Q_T < 0.56`
   B4-AM,  B4 with amplitude matching (QB3),  :math:`0.36 < Q_T < 0.56`
   LR4-CA, LR4 with compliance alteration, :math:`0.34 < Q_T < 0.4`
   LR4-AM, LR4 with amplitude matching, :math:`0.34 < Q_T < 0.4`
   BL4-CA, BL4 with compliance alteration, :math:`0.3 < Q_T < 0.36`
   BL4-AM, BL4 with amplitude matching, :math:`0.3 < Q_T < 0.36`
   
