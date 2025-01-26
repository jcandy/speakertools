.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

The CD4 Bass Reflex Alignment
=============================

The CD4 alignment was first presented in the Voice Coil Magazine, August
2024. Later the article became Open Access when AudioXpress released an
`online version October 2024 <https://audioxpress.com/article/the-cd4-bass-reflex-alignment>`_.

A critically damped loudspeaker is a system that has no overshoot to a
step function input. A critically damped 2nd-order closed box is known
from theory and implies that the box is designed such that the system
:math:`Q_{TC} = 0.5`. In this article, we describe the Critically Damped
4th-order (CD4) bass reflex alignment.

The Calculation of CD4 Including Leakage Loss
---------------------------------------------

In a bass reflex design, we achieve no overshoot to a step function with
a 4th-order polynomial if the response has all poles on the real axis.
If we limit ourselves to :math:`h = 1`, with all poles on the unit
circle, this becomes a special case of the (Sub-) Boombox alignment,
where the damping ratio :math:`\zeta = 1`, which is equivalent to each
second-order filter :math:`Q = 1/(2 \cdot \zeta) = 0.5`. We remind ourselves that a
bass reflex system consists of two oscillators: 1) the driver in the
box, and 2) the port in the box, and each of these two 2nd-order systems
must be critically damped, i.e., have a filter :math:`Q = 0.5`, which means they
are 2nd-order Linkwitz-Riley filter functions. Since a 2nd-order
Linkwitz-Riley filter is composed of two cascaded 1st-order
(Butterworth) filters, you can also say the 4th-order critically damped
system consists of four cascaded 1st-order filters. The normalized
response function becomes:

.. math::
   \begin{eqnarray}
    G(s) &=& \frac{ s^4 } { (s + 1)^4 } \\
         &=& \frac{ s^4 } { (s^2 + 1/0.5 \cdot s + 1)^2 } \\
         &=& \frac{ s^4 } { (s^4 + 4 \cdot s^3 + 6 \cdot s^2 + 4 \cdot s + 1) }
   \end{eqnarray}

Using Python, we may calculate the CD4 alignment as follows:

.. code-block:: python

   Ql = 10
   Qt = 1/(4-1/Ql)
   h = 1
   alpha = 4 - 1/(Ql * Qt)

where :math:`Q_T` is not something you can specify yourself but is given
by the equations because the CD4 alignment is a discrete alignment.

Please note that, in a reflex box, setting the driver in box
:math:`Q_{TC} = 0.5` does not provide the correct filter Q, but rather,
for the lossless case, :math:`Q_{TC} = Q_T \cdot \sqrt(\alpha + 1) = 0.559`.
For a design with leakage loss, you may recalculate :math:`Q_T` and
:math:`\alpha`. Leakage loss results in a smaller :math:`\alpha` and
consequently a larger box, which means :math:`Q_{TC}` is reduced. To
arrive at :math:`Q_{TC} = 0.5`, one must set :math:`Q_L = 1.5`
(:math:`Q_L = 0.3`). This is awfully lossy, and we conclude that, in
practice, for a CD4 reflex box with a plugged (stuffed or covered) port,
:math:`Q_{TC}` will always be larger than 0.5.

With :math:`h = 1`, we imply that the driver's resonant frequency and
the port tuning coincide. With :math:`Q_L = 10`, the required
:math:`Q_T` value is 0.2564, and in the lossless case, we get driver
:math:`Q_T = 0.25`. Remember to compensate for all electrical resistance
in series with the driver.

The CD4 alignment is a special case of the (S)BB4 alignments, similar to
LR4, but in this case targeting no overshoot in the time domain.
Therefore, the equations are similar, and it is a 1-parameter alignment,
but with our requirement of being critically damped and consequently
having all four poles on the real axis (at -1), it follows that the
calculation of the required :math:`Q_T` and :math:`\alpha` are a bit
different.

