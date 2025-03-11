.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

=============================
The LR4 Bass Reflex Alignment
=============================

The LR4 alignment was first presented in the Voice Coil Magazine, June
2024. Later the article became Open Access when AudioXpress released an
`online version September 2024 <https://audioxpress.com/article/the-lr4-bass-reflex-alignment>`_.

Although the Linkwitz-Riley alignment was never explicitly mentioned
anywhere prior to the article in Voice Coil Magazine (except in our own
work, e.g., some YouTube videos), it was possible to compute this as a
specific instance of the (S)BB4 family of alignments.

This is obvious when it is realized that the Linkwitz-Riley filter and
the Boombox alignment share the characteristic property that they use
cascaded identical filters.

The Calculation of LR4 Including Leakage Loss
---------------------------------------------

The fourth-order Linkwitz-Riley high-pass filter is defined as two
cascaded second-order Butterworth filters. The normalized response
function becomes:

.. math::
    G(s) = \frac{ s^4 } { (s^2 + 2 \cdot \zeta \cdot s + 1)^2 }

where :math:`\zeta = 1/\sqrt{2} \approx 0.707` is the damping ratio. The
filter-Q of each second-order Butterworth section is
:math:`Q = 1/(2 \cdot \zeta) \approx 0.707`.

Using Python, we may calculate the LR4 alignment as follows:

.. code-block:: python

   import numpy as np

   Ql = 10
   Qt = 1/(np.sqrt(8)-1/Ql)
   h = 1
   alpha = 1/4 * (1/Qt - 1/Ql)**2

where :math:`\qt` is not something you can specify yourself but is given
by the equations because the LR4 alignment is a discrete alignment.

The classic Thiele-Small (T-S) theory prescribes that the loudspeaker
designer should account for losses by setting :math:`\ql` in the range
of 5 to 20, typically set conservatively to 7, but no matter what value
is chosen, it is arbitrary and not based on physical leakage. In the
shown code, :math:`\ql` is set to 10, a round number. An even higher
:math:`\ql` value could be chosen, calculating a larger :math:`\alpha`
value (smaller box volume), with a slightly increased risk that the box
you build becomes a bit too small. You are welcome to change the
:math:`\ql` value as you see fit.

For leakage :math:`\ql = \infty`, the driver :math:`\qt` that matches
the Linkwitz-Riley response function is: :math:`1/\sqrt{8} \approx 0.354`.
If :math:`\ql = 10`, as in the code example, then :math:`\qt = 0.367`.
When aiming for these :math:`\qt`-values, remember that the driver
specification from the datasheet should be a bit lower to allow for some
series resistance.
