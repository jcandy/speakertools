.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

=========================
Classic Vented Alignments
=========================

In classical loudspeaker theory from the 1960s onwards, the concept of alignments was developed to provide a systematic prescription for choosing box volume and port tuning to yield a target low-frequency response. While the theory is not exact, it offers numerous benefits including insight into the choice between low frequency extension versus group delay (phase distortion). A brief overview of the alignments discussed here and supported in Speakerbench is given in the :ref:`Summary` section at end of this page.

Alignment source code
---------------------

All the plots and data output shown on this page were generated using the **Speakerbench python alignment library**. That library and all software (including these webpages) is freely-available

- Source code at `GitHub speakerbench repository <https://github.com/jcandy/speakertools/tree/master/src/example_code>`_.
- Download :download:`ZIP archive <example_code/libalignment.zip>`
- Download :download:`TGZ archive <example_code/libalignment.zip>`

.. code-block:: bash
		
   $ unzip libalignment.zip
   $ python print_qt.py
   $ python print_c4.py
   $ python print_qa.py
   $ python print_quasi.py

Within the ZIP file is a Python library of functions (libalignment.py), which is used in code samples throughout this chapter.

General framework
-----------------

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4\ :sup:`th`-order bass-reflex alignments. These alignments are particular types of 4\ :sup:`th`-order high-pass filters. Following Small :cite:`small:1973c` (Eq. 57) we can write the normalized response function as

.. math::
   :label: eq.response
	
   G_\mathrm{H}(s) = \frac{s^4}{s^4 + a_1 s^3 + a_2 s^2 + a_3 s + 1} \; ,

where :math:`s = j \omega / \omega_0` is the dimensionless complex frequency variable normalized to :math:`\omega_0 \doteq \sqrt{\wb\ws} = \sqrt{h} \, \ws`. In the first part of his article series, Small :cite:`small:1973c` (Eqs. 22-24) writes the lossy box filter coefficients as

.. math::
   :label: eq.a
	
   \displaystyle
   a_1 & = \frac{\ql + h \: \qts}{\sqrt{h} \: \ql \: \qts}  \\
   a_2 & = \frac{h + (\alpha + 1 + h^2) \: \ql \: \qts}{h \: \ql \: \qts} \\
   a_3 & = \frac{h \: \ql + \qts}{\sqrt{h} \: \ql \: \qts} \; ,

where :math:`\ql` is the leakage-loss :math:`Q` of the box and :math:`\qts` is the total :math:`Q` of the driver. Here, :math:`h = \wb/\ws` is the system tuning ratio and :math:`\alpha =\vas/\vb` is the ratio of the compliance volume to the box volume. We remark that the coefficients are approximate and neglect myriad other terms which appear in a more comprehensive model of a vented box. These missing terms would represent more complex losses in the box and in the driver suspension system, driver inductance and semi-inductance, and so on. It is generally accepted that :math:`\ql` does not represent a true leakage loss. Rather it is an approximate *total loss* which is dominated by driver losses not accounted for in the standard Thiele-Small theory. These losses are included in the advanced model and thus we recommend setting :math:`\ql > 100` in this case.

In the definition of :math:`\omega_0`, :math:`\ws` is the driver resonant frequency and :math:`\wb` is the vent resonant frequency. This normalization is equivalent to setting :math:`T_0=1` in Small's expressions. The magnitude-versus-frequency behavior is also given in Small :cite:`small:1973c` (Eqs. 58 and 59) facilitated by the use of the squared modulus technique, which we reproduce here as

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + A_1 \omega^6 + A_2 \omega^4 + A_3 \omega^2 + 1} \; ,

where

.. math::
  A_1 & = a_1^2-2 a_2 \; , \\
  A_2 & = a_2^2+2-2 a_1 a_3 \; , \\
  A_3 & = a_3^2-2 a_2 \; .

A note about series resistance
..............................

The driver Q is given by

.. math::
   \frac{1}{\qts} = \frac{1}{\qms} + \frac{1}{\qes} \; .

Here, we have the electrical and mechanical Q values

.. math::
   \qms & = \frac{\mms}{\rms} \, \ws \\
   \qes & = \frac{\mms}{\rme} \, \ws

where :math:`\rme` is the electrical DC resistance :math:`\re` converted to the mechanical side. The electrical damping depends on the electrical resistance of the driver voice coil :math:`\re` as well as any added electrical resistance :math:`R_\mathrm{S}` in series with the driver including the output resistance :math:`R_g` of the voltage source (amplifier), and we may name this :math:`R_\mathrm{MES}`

.. math::
   R_\mathrm{MES} = \frac{\bls}{\re + R_\mathrm{S}} \; .

When you enable the optional filter in the Speakerbench box mode, and apply a series resistance, the modified value :math:`Q_\mathrm{T,R_S}` is calculated in Speakerbench and displayed in the INFO tab.

.. math::
   Q_\mathrm{T,R_S} = \frac{\mms}{R_\mathrm{MES} + \rms} \, \ws

This value is what Speakerbench uses for response calculations (and in the alignment chart). The second-order response function (see :ref:`Second-order alignments`) becomes:

.. math::
   G_\mathrm{H}(u) = \frac{u^2}{\displaystyle u^2 + \frac{u}{Q_\mathrm{T,R_S}} + 1 + \alpha} \; .

Discrete alignments
-------------------

A *discrete* bass reflex alignment means we need to select a driver with a specific :math:`\qts` value and match that with a specific box volume and port tuning frequency to obtain the unique discrete alignment. Two popular classic discrete alignments are the Butterworth (B4) and Bessel (BL4) ones. In addition, Thiele :cite:`thiele:1974` defined the Inter-Order Butterworth (IB4) discrete alignment around 1974. In these notes we further discuss the so-called Linkwitz-Riley (LR4) and Critically Damped (CD4) discrete alignments. Each discrete alignment defines a specific 4\ :sup:`th`-order filter with fixed coefficients :math:`(a_1,a_2,a_3)` along with properties that are broadly suitable for vented aligments. The coefficients are

Butterworth B4
..............

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.B4

   .. image:: images/alignment/B4-amp.png
   .. image:: images/alignment/B4-poles.png

   B4 amplitude and poles.

In the limit of no losses, the Butterworth (B4) response corresponds to

.. math::
   \qts   & = \cos\frac{3\pi}{8} \simeq 0.3827 \\
   h      & = 1 \\
   \alpha & = \sqrt{2} \simeq 1.414

The Butterworth filter was introduced in 1930 by Stephen Butterworth :cite:`butterworth:1930`. It offers a maximally-flat frequency response (with no ripple in the passband) with the sharpest knee point towards the roll-off region and thus the most extended bandwidth. In relation to bass reflex loudspeakers, B4 was a very popular target response for many years, and several (non-discrete) alignment *families* ultimately develops from B4. The filter coefficients depend on cosines of the pole locations, and have the exact values

.. math::
   a_1 = 2 \cos\frac{\pi}{8} + 2 \cos\frac{3\pi}{8}
   \qquad
   a_2 = 2+4 \cos\frac{\pi}{8} \cos\frac{3\pi}{8}
   \qquad
   a_3 = a_1

The remarkable vanishing of all coefficients :math:`(A_1,A_2,A_3)` when calculating the squared modulus demonstrates the maximally-flat property via

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{\omega^8}{\omega^8 + 1} \; ,


Linkwitz-Riley LR4
..................

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.LR4

   .. image:: images/alignment/LR4-amp.png
   .. image:: images/alignment/LR4-poles.png

   LR4 amplitude and poles (two double poles).

In the limit of no losses, the Linkwitz-Riley (LR4) response corresponds to

.. math::
   \qts   & = 1/\sqrt{8} \simeq 0.3536 \\
   h      & = 1 \\
   \alpha & = 2

In 1976, some years after Thiele’s work, Linkwitz-Riley filters for use in electronic crossover design were described by Siegfried H. Linkwitz in a series of articles :cite:`linkwitz:1976,linkwitz:1978`. Linkwitz obtained the 2\ :sup:`nd`- and 4\ :sup:`th`-order filters by squaring the 1\ :sup:`st`- and 2\ :sup:`nd`-order Butterworth filters, respectively. In the 4\ :sup:`th`-order case,

.. math::
    G_\mathrm{H}(s) = \frac{ s^4 } { \left(s^2 + \sqrt{2} s + 1 \right)^2 } \; .

An important property of the combined high-pass and low-pass sections is that the resulting crossover sums to unit magnitude, with the outputs in phase at the crossover frequency. Linkwitz originally proposed filters with these characteristic for solving lobing issues with noncoincident transducers. Of course, the application to crossovers is unrelated to bass-reflex design, which may partly explain why the literature seems to contain no recorded use of the Linkwitz-Riley filter as a discrete target alignment. In relation to bass reflex alignment, LR4 exhibits desirable features like fast settling time (controlled impulse response) similar to :ref:`Bessel BL4` but with a more extended frequency response. The response coefficients are

.. math::
   a_1 = \sqrt{8} \simeq 2.828
   \qquad
   a_2 = 4
   \qquad
   a_3 = a_1 \; .

Although the Linkwitz-Riley alignment was never explicitly mentioned anywhere prior to the article in Voice Coil Magazine, it is a specific instance of the :ref:`Boombox BB4` family of alignments for :math:`\zeta = 1/\sqrt{2}`.  The LR4 alignment was first presented in the Voice Coil Magazine, June 2024. Later the article became Open Access when AudioXpress released an `LR4 article <https://audioxpress.com/article/the-lr4-bass-reflex-alignment>`_.

Inter-Order Butterworth IB4
...........................

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.IB4

   .. image:: images/alignment/IB4-amp.png
   .. image:: images/alignment/IB4-poles.png

   IB4 amplitude and poles (the pole on the x-axis is a double pole).

In the limit of no losses, the Inter-order Butterworth (IB4) response corresponds to

.. math::
   \qts   & \simeq 0.3398 \\
   h      & \simeq 1.106 \\
   \alpha & \simeq 2.107

Thiele defined IB4 as a combination of a general second-order filter and two identical first-order filters :cite:`thiele:1974`

.. math::
    G_\mathrm{H}(s) = \frac{ s^4 } { \left( s^2 + \lambda s + \beta \right) \left(s + 1\right)^2 } \; ,

where :math:`\lambda` and :math:`\beta` are free parameters to be chosen according to the flatness condition

.. math::
   :label: eq.flat
	
   \left\| \left( s^2 + \lambda s + \beta \right) \left(s + 1\right)^2 \right\|^2
   = 1 + 4 \omega^6 + 3 \omega^8 \; .

In these equations, :math:`s = i\omega` and :math:`\omega` are not yet properly normalized. Note that on the righthand side of :eq:`eq.flat`, the coefficients of :math:`\omega^2` and :math:`\omega^4` have been set to zero. This implies that IB4 is a special case of QB3 (referred to in this work as B4Q). By solving :eq:`eq.flat` we can deduce the required coefficients

.. math::
   \lambda & = \sqrt{2 \left(\sqrt{3} - 1\right)} \; , \\
   \beta   & = \sqrt{3} \; . \\

Then, bringing the high-pass filter into canonical form, the polynomial coefficients :math:`a_1`, :math:`a_2`, and :math:`a_3` are expressed as

.. math::
   a_1 = \frac{2+\lambda}{\beta^{1/4}}
   \qquad
   a_2 = \frac{1+2\lambda+\beta}{\beta^{1/2}}
   \qquad
   a_3 = \frac{\lambda+2\beta}{\beta^{3/4}}

The Inter-Order Butterworth (IB4) alignment is rarely talked about. It was mentioned briefly by Richard Small :cite:`small:1973c`. Bullock :cite:`bullock:1981` published a table for this discrete alignment, and the tables are reproduced in The Loudspeaker Design Cookbook by Vance Dickason. The IB4 alignment was first presented in Voice Coil Magazine, July 2024. Later the article became Open Access when AudioXpress released an `IB4 article <https://audioxpress.com/article/the-ib4-bass-reflex-alignment>`_.


Bessel BL4
..........

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.BL4

   .. image:: images/alignment/BL4-amp.png
   .. image:: images/alignment/BL4-poles.png

   BL4 amplitude and poles.

In the limit of no losses, the Bessel response corresponds to

.. math::
   \qts   & \simeq 0.3162 \\
   h      & \simeq 0.9759 \\
   \alpha & \simeq 2.333

The filter coefficients can be written in terms of the 4\ :sup:`th`-order Bessel polynomial

.. math::
   y_4(x) = 105 x^4 + 105 x^3 + 45 x^2 + 10 x + 1 \; .

Bringing the high-pass response function into the canonical form :eq:`eq.response` shows that

.. math::
   a_1 = \frac{105}{105^{3/4}} \qquad a_2 = \frac{45}{105^{1/2}} \qquad a_3 = \frac{10}{105^{1/4}} \; .

Bessel polynomials arise in the theory of Bessel functions and are named after Friedrich Wilhelm Bessel (1784-1846) in tribute to his systematic study of Bessel's differential equation. The practical application to filters was worked out by W.E. Thomson in 1949 in a scientific article titled *Delay Networks Having Maximally Flat Frequency Characteristics*. Thomson described this filter function applied to delay lines. A frequency range with flat group delay implies nearly linear phase response and hence minimal phase distortion of the signal. Low-pass Bessel filters are characterized by the fastest settling time and maximally flat group delay of the form

.. math::
   \tau_g = -\frac{d\phi}{d\omega} \sim 1 + O(\omega^8)

.. comment:
   We cannot end this section with a low-pass equation. It appears incomplete. Bass reflex = high-pass.

Critically damped CD4
.....................

.. comment:
   Jeff - I don't think this is true: We remind ourselves that a bass reflex system consists of two oscillators: 1) the driver in the box, and 2) the port in the box
   Claus - it is true.

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.CD4

   .. image:: images/alignment/CD4-amp.png
   .. image:: images/alignment/CD4-poles.png

   CD4 amplitude and poles (one quadruple pole).

In the limit of no losses, the critically damped response corresponds to

.. math::
   \qts   & = 0.25 \\
   h      & = 1 \\
   \alpha & = 4

A critically-damped response has all 4 poles at :math:`s=-1`, such that the response function is

.. math::
   G_\mathrm{H}(s) = \frac{ s^4 } { (s + 1)^4 } = \frac{s^4}{s^4 + 4 s^3 + 6 s^2 + 4 s + 1} \; .

Because of the reality of the poles, the step response for a CD4 aligment is non-oscillatory (no overshoot). Thus, CD4 is the most extended frequency response of all alignments with no overshoot. In relation to bass reflex design, however, this alignment is not commonly used due to the early roll-off in the frequency response. We remark that CD4 is also a special case of the :ref:`Boombox BB4` family for :math:`\zeta = 1`. CD4 is also equivalent to two cascaded 2\ :sup:`nd`-order filters each with :math:`\qfilt = 0.5`, where :math:`\qfilt` is the filter-Q

.. math::
   s^2+s/\qfilt+1 \; .

In the lossless case :math:`\ql \rightarrow \infty`, the CD4 alignment corresponds to a driver with :math:`\qts = 0.25`.  A discussion of the CD4 alignment was presented in Voice Coil Magazine in August 2024. Later the article became Open Access when AudioXpress released a `CD4 article <https://audioxpress.com/article/the-cd4-bass-reflex-alignment>`_.

Comparison
..........

:numref:`fig.all` shows the (normalized) amplitude response and group delay of the above mentioned discrete alignments.

.. subfigure:: AB
   :width: 80%
   :gap: 6px
   :align: center
   :name: fig.all

   .. image:: images/alignment/all-amp.png
   .. image:: images/alignment/all-delay.png

   The normalized amplitude response :math:`|G_\mathrm{H}|` (left) and group delay :math:`\omega_0 \tau_g = -d\phi/d\omega` (right) of the five discrete alignments.

Note: These graphs are **not** normalized relative to the driver's resonance frequency, but :math:`\omega_0 \doteq \sqrt{\wpb \, \ws} = \sqrt{h} \, \ws`. Below, we tabulate each of the five discrete alignments as a function of the enclosure loss :math:`\ql`. The python source code used is also shown.


.. collapse:: CLICK HERE to expand discrete alignment source code

   .. literalinclude::
      example_code/print_qt.py

.. literalinclude::
   images/alignment/print_qt.txt


Modification of discrete alignments
-----------------------------------

For the five discrete alignments described above, :math:`\qts` is not a free parameter. This suggests that a particular alignment cannot be achieved with an arbitrary driver. Thus we are faced with the problem of *misalignment*.

.. admonition:: misalignment

		If the driver :math:`\qts` does not match that required by your desired target alignment, the driver is said to be *misaligned*.

In the sections below we will describe three approaches to deal with misalignment.

Method 1: Ignorance
...................

The simplest solution is to ignore the fact that the driver :math:`\qts` is far from the target :math:`\qts`. This we call the method of ignorance, because you ignore the fact that :math:`\qts` is wrong. Speakerbench denotes this approach by adding a trailing 'i' to the name: B4i, LR4i and BL4i. In this case, the suggested :math:`h` and :math:`\alpha` are **unaffected** by the driver :math:`\qts` (the fact that :math:`\qts` is not correct is ignored). The method of ignorance **is not recommended for actual use**, but is included for reference. Despite the name, we suspect the method was commonly used in the past.

Method 2: Compliance alteration
...............................

A second and better approach to handling misalignment (i.e., approximating a desired discrete alignment for which the driver :math:`\qts` does not match the alignment :math:`\qts`) is **compliance alteration**. In this case we imagine that the driver compliance starts out at a value for which the driver :math:`\qts` matches the alignment :math:`\qts`. A box and port are designed with the required :math:`h` and :math:`\alpha`. We call these the *reference values*: :math:`Q_\mathrm{TS,ref}`, :math:`\alpha_\mathrm{ref}` and :math:`h_\mathrm{ref}`. Then, overnight, the suspension softens or hardens such that the driver obtains the value :math:`\qts`. Compliance alteration then shifts :math:`\alpha` and :math:`h` according to

.. math::
   \alpha & = \alpha_\mathrm{ref} \left( \frac{Q_\mathrm{TS,ref}}{\qts} \right)^2 \; , \\
   h      & = h_\mathrm{ref} \left( \frac{Q_\mathrm{TS,ref}}{\qts} \right) \; .

In Speakerbench, when we apply this method, the alignment acronym is followed by CA as in B4CA, LR4CA and BL4CA. Below we tabulate sample alignments for :math:`\ql = 10`


.. collapse:: CLICK HERE to expand compliance alteration source code

   .. literalinclude::
      example_code/print_ca.py

.. literalinclude::
   images/alignment/print_ca.txt

Compliance Alteration was first presented in Voice Coil Magazine from October 2024. Later, the article became Open Access when AudioXpress released an `Compliance Alteration article <https://audioxpress.com/article/bass-reflex-alignments-compliance-alteration>`_. The method can be applied to any desired discrete target alignment. This method is particularly interesting if your driver :math:`\qts` is a bit too high, because with the compliance alteration technique, the box calculation is then treated as if the suspension is a bit too stiff. Fortunately, the driver suspension will experience aging (or burn-in) over time and will soften. When this happens, the provided equations dictate that your system will, over time, move toward the desired target response, and if softened enough to reach :math:`Q_\mathrm{TS,ref}`, the system response will match the target without any error. If the softening does not happen, the system response will deviate slightly from the target.

Method 3: Generalized quasi-alignment
.....................................

In a design process based on alignments, we consider :math:`(\ql,\qts)` as given inputs and :math:`(\alpha,h)` as output parameters to be computed by the alignment. Since we have two free parameters, it follows that we can specify only two of the three values :math:`(A_1,A_2,A_3)`. The approach taken is to relax (i.e., ignore) the condition on :math:`A_3`; that is, we match the behaviour in the pass-band :math:`(A_1)` and mid-band :math:`(A_2)` but **not** the stop-band :math:`(A_3)`. This is described in more detail for so-called QB3 (although we prefer B4Q because the order of the filter is 4) lossless case by Benson :cite:`benson:1993` (page 188).

By defining :math:`G = \left( \alpha+1+h^2 \right)/h`, we can rewrite these two conditions as

.. math::
  \begin{eqnarray}
  A_1 &=& \frac{q^2}{h} - 2G + \epsilon^2 q^2 h \; , \\
  A_2 &=& \left( G + \epsilon q^2 \right)^2 + 2-2q^2\left[ 1+\epsilon^2+\epsilon (h+1/h) \right] \; .
  \end{eqnarray}

where :math:`q = 1/\qts` and :math:`\epsilon = \qts/\ql \ll 1` is a small parameter.

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

.. collapse:: CLICK HERE to expand quasi-alignment source code

   .. literalinclude::
      example_code/print_quasi.py

.. literalinclude::
   images/alignment/print_quasi.txt

In Speakerbench, when we apply this method, the alignment acronym is followed by Q as in B4Q, LR4Q and BL4Q. Thus, B4Q in Speakerbench is the same as what is known in classical theory as the QB3 alignment. We remark that Bullock :cite:`bullock:1981` defines SQB3 as a subset of QB3 for drivers with :math:`0.56 > \qts > 0.4`.

Alignment families
------------------

Beyond discrete aligments, for which :math:`(a_1,a_2,a_3)` have explicit numerical values, well-known **alignment families** exist for which :math:`(a_1,a_2,a_3)` depend upon a free parameter. The term **alignment family** is derived from the mathematical definition of a `family of response curves <https://en.wikipedia.org/wiki/Family_of_curves>`_.
An alignment family allows one to cover a range of driver :math:`\qts` values rather than just a single value. The B4Q quasi-alignment described above is in the loudspeaker industry considered an alignment family. Small and others refer to this family as QB3 (references).

Boombox BB4
...........

The Boombox family of alignments was first described in a convention article by W.J.J. Hoge in 1976, later in the JAES :cite:`hoge:1977`. This alignment is relatively simple, and cascades two identical 2\ :sup:`nd`-order polynomials according to

.. math::
   G(s) = \frac{ s^4 } { \left( s^2 + 2 \, \zeta \, s + 1 \right)^2 }

where the free parameter :math:`\zeta` is the **damping ratio**, which is directly related to the driver's :math:`\qts`-value. For a chosen :math:`\qts` and :math:`\ql`, we have

.. math::
   \zeta  & = \frac{1}{4} \left( \frac{1}{\qts} + \frac{1}{\ql} \right) \\
   \alpha & = \frac{1}{4} \left( \frac{1}{\qts} - \frac{1}{\ql}\right)^2 \\
   h      & = 1

Bullock :cite:`bullock:1981` presents tables for :math:`\ql \geq 3`-value, which is exceptionally lossy and seems unlikely for practical use. Hoge was focused on a suitable alignment for instrument loudspeakers, e.g., for electric guitars, and was seeking a bass reflex alignment option for the high :math:`\qts` drivers of the time that could provide an alternative to :ref:`Chebyshev C4`. Choosing to cascade two identical 2\ :sup:`nd`-order polynomials gives double poles with reasonably fast settling time for an impulse. Unfortunately, this alignment creates a peak before roll-off which led Hoge to satirically name it the Boombox alignment, or BB4. Hoge only defined the BB4 alignment for driver :math:`\qts` above roughly 0.37, and he identified the peak with :math:`\ql = 7` for a driver :math:`\qts = 0.72` to be around +6 dB. For high :math:`\qts` drivers, the peak becomes large, which you might accept in favor of the impulse stopping quicker than a similar peaky Chebyshev response. Besides, the single peak of a BB4 alignment is easier to equalize electronically, than the ripples of a Chebyshev alignment. On the other hand, a Chebyshev alignment with a similar driver :math:`\qts` results in 1.3 - 1.4 dB ripple. Finally, when driver :math:`\qts` is this high, one may consider a large closed box. Bullock realized that the equations also work well for drivers with lower :math:`\qts`, and in this case there is no peak in the frequency response. He coined the term Sub-Boombox for these alignments, or SBB4, and his tables go as low as :math:`\qts = 0.20`. It is therefore reasonable to say that the BB4-SBB4 alignment works for driver :math:`\qts` in the range of 0.20-0.72, although mathematically it can be applied outside these limits. Note finally that both LR4 and CD4 are special cases of BB4 for :math:`\zeta = 1/\sqrt{2}` and :math:`\zeta = 1` respectively.

Transitional B4-LR4
...................

Speakerbench supports a so-called Transitional B4-LR4 alignment family, which moves smoothly between Butterworth B4 and Linkwitz-Riley LR4. The construction is fairly trivial by comparing locations of LR4 and B4 poles. We can write a one-parameter family of alignments that contains both B4 and LR4 as specific cases using

.. math::
   a_1 &= \sqrt{8} \cos\epsilon \\
   a_2 &= 4 \cos^2 \epsilon \\
   a_3 &= a_1

where :math:`\epsilon` is an angle in the range :math:`0 \leq \epsilon \leq \pi/8`. Evidently

.. math::
   \cos\epsilon = \frac{1}{\sqrt{8}} \left( \frac{1}{\qts} + \frac{1}{\ql} \right)


Importantly, :math:`\epsilon = 0` gives LR4 and :math:`\epsilon = \pi / 8` gives B4. In general, the four poles of the response function lie on the unit circle at

.. math::
   \theta & = \frac{3\pi}{4} \pm \epsilon \\
   \theta & = -\frac{3\pi}{4} \pm \epsilon

To the best of our knowledge, the concept of Transitional Alignments was never explored in relation to loudspeaker (Bass Reflex) boxes until it was presented in the Voice Coil Magazine, September 2024. Later the article became Open Access when AudioXpress released an online
`Transitional alignment <https://audioxpress.com/article/transitional-bass-reflex-alignments>`_ article. Notably, R.M. Golden and J.F. Kaiser :cite:`golden:1971` described the roots of normalized Butterworth and Bessel-Thomson low-pass transfer functions, from which Small :cite:`small:1973c` derived the polynomial coefficients of the fourth-order highpass Bessel alignment. Golden and Kaiser also described a transitional filter design where a chosen balance between the two is realized.

With the calculated transition from LR4 to B4, we have obtained a subtle improvement over continuing with the Boombox alignment. For drivers with :math:`\qts` values above the LR4-:math:`\qts`, the Boombox alignment will have a (small) peak in its frequency response before roll-off. By transitioning towards the B4 alignment, we avoid this peak, and the frequency response remains monotonic. Transitioning between B4 and LR4 is only relevant for drivers with :math:`\qts` in the approximate range :math:`0.37 < \qts < 0.40`. Speakerbench only shows this option if your driver's :math:`\qts`-value is within this range. Although Speakerbench only supports this one transitional alignment, in the Alignment Chart you can click anywhere between known alignments to achieve an effective transitional alignment.

Chebyshev C4
............

Perhaps the most remarkable of all vented alignments is the Chebyshev C4 method because of the systematic way in which it defines an entire family (in the parameter k) that controls ripple and simultaneously connects to B4. Chebyshev-like alignments for loudspeakers were exploited as early as 1956 by F.J. van Leeuwen :cite:`vanleeuwen:1956`. These alignments have also been discussed by Thiele and Small, and in detail by Benson following the treatment by Weinberg (expand). The alignment is named after Pafnuty Chebyshev because the amplitude response is written in terms of the Chebyshev polynomial of the first kind. Consider the 4\ :sup:`th`-order low-pass case,

.. math::
   \left| G_\mathrm{H}(i\omega) \right|^2 = \frac{1}{1+\varepsilon^2 T_4^2 (x)}

where :math:`x = \omega/\omega_c` and :math:`\omega_c` is the critical frequency above which the filter becomes non-oscillatory, and

.. math::
   T_4(x) = 8 x^4 - 8 x^2 + 1 \quad \text{such that} \quad T_4(\cos\phi) = \cos(4\phi)

Thus, in the region :math:`x \leq 1` the properties of polynomial ensure that the amplitude is bounded by

.. math::
   \frac{1}{1+\varepsilon^2} \leq \left| G_\mathrm{H}(i \omega) \right|^2 \leq 1 \; .

Thus, :math:`\varepsilon` is a measure of the passband ripple. It provides the degree of freedom required for drivers of varying :math:`\qts`. Note however that the response functions above are not yet written in the canonical form of Eq. :eq:`eq.response`. Using the properties of the Chebyshev polynomials one can determine the locations of the poles :math:`u = i x = i \cos\phi` (the analog of :math:`s = i\omega`) by finding the roots of

.. math::
   1+\varepsilon^2 \cos\left(4\phi\right)^2 = 0

After some algebra we can write the roots as

.. math::
   u_m = i\cos\phi_m = - \sinh(\varphi)\sin\theta_m + i \cosh(\varphi)\cos\theta_m \quad\text{for} \quad m = 1,\cdots,4

where :math:`\theta_m = (2m-1)\pi/8` and

.. math::
   \varphi = \frac{1}{4}\,  \mathrm{arcsinh}\left( \frac{1}{\varepsilon} \right)

We can further simplify by defining :math:`s = u/\cosh\varphi` to give

.. math::

   s_m = -k \sin\theta_m + i \cos\theta_m

where :math:`k = \tanh\varphi < 1`. These are evidently the poles of the B4 alignment, but with the real part multiplied by :math:`k`, which is consistent with a comment by Small. The algebra required to simplify is straigthforward but tedious. Some partial steps are illuminating, specifically

.. math::
   (s-s_1)(s-s_4) & = s^2 + 2 k s \sin\frac{\pi}{8} + 1 + (k^2-1)\sin^2\frac{\pi}{8} \\
   (s-s_2)(s-s_3) & = s^2 + 2 k s \cos\frac{\pi}{8} + 1 + (k^2-1)\cos^2\frac{\pi}{8} \\

.. math::
   \prod_{m-1}^4 (s-s_m) = s^4 + k c_0 \, s^3  + \left[ 1+k^2(1+\sqrt{2}) \right] s^2 + k c_0 \left( 1+\frac{k^2-1}{\sqrt{8}} \right) s + D(k)

where :math:`c_0 = \sqrt{4+\sqrt{8}}`. Finally we can renormalize to find the forms reported by Small for the high-pass function

.. math::
   a_3 & = \frac{c_0 k}{D^{1/4}} \\
   a_2 & = \frac{1+k^2(1+\sqrt{2})}{D^{1/2}} \\
   a_1 & = \frac{c_0 k}{D^{3/4}} \left( 1+\frac{k^2-1}{\sqrt{8}} \right)

Evidenty, these functions can be analytically continued triivally to the region :math:`k \geq 1`. The region :math:`k < 1` has passband ripple, the special case :math:`k = 1` is the B4 alignment, and the region :math:`k > 1` is monotonic.

.. collapse:: CLICK HERE to expand Chebyshev C4 source code

   .. literalinclude::
      example_code/print_c4.py

.. literalinclude::
   images/alignment/print_c4.txt

Second-order alignments
-----------------------

One can take the limit :math:`h \rightarrow 0` in :eq:`eq.a` to recover the limit of a closed box. However, there is a subtlety related to :math:`\ql` which is apparent from the definition

.. math::
   \ql \doteq \frac{h}{\alpha} \rml \cms \, \ws \; .

This definition is unsuitable for the case of small :math:`h` and, arguably, unsuitable in general. To properly retain loss in a sealed enclosure we introduce :math:`\qlc` via :math:`\ql \doteq h \, \qlc`. After some algebra, and using :math:`\qlc` in place of :math:`\ql`, we can derive the 3rd-order leaky-sealed-box response

.. math::
   \frac{u^3}{\displaystyle u^3
   + \left( \frac{1}{\qts} + \frac{1}{\qlc} \right) u^2
   + \left( \alpha+1+\frac{1}{\qts\qlc} \right) u
   + \frac{1}{\qlc}} \; ,

where :math:`u = i \omega/\ws`. In reality, the actual leakage loss :math:`\ql` is negligible for any reasonably-constructed sealed box. Finite :math:`\ql` has historically been used in alignment theory to provide a crude but analytically tractable description of losses, whereas real losses in the system result in corrections that cannot be treated in the context of 4\ :sup:`th`-order filter theory. So, taking :math:`\qlc \rightarrow \infty`, we are left with the classic 2\ :sup:`nd`-order box response

.. math::
   :label: eq.closedu

   G_\mathrm{H}(u) = \frac{u^2}{\displaystyle u^2 + \frac{u}{\qts} + \left( \alpha+1 \right)} \; .

Simulation of a closed box in Speakerbench in triggered by zeroing the port tuning frequency: :math:`\fpb = 0`. Losses in this case will vanish because Speakerbench accepts input for :math:`\ql` rather than :math:`\qlc`. To arrive at the canonical form for a closed box, we write :math:`u = \sqrt{\alpha+1} \, s` to find

.. math::
   :label: eq.closed

   G_\mathrm{H}(s) = \frac{s^2}{\displaystyle s^2 + \frac{s}{\qtc} + 1}

where

.. math::
   \qtc & \doteq \sqrt{\alpha+1} \, \qts \; , \\
   \wcb & \doteq \sqrt{\alpha+1} \, \ws \; \\

where :math:`s = i \omega/\wcb`. A closed box system has one free design parameter :math:`\alpha = \cms / \cmb = \vas / \vb`. In the Speakerbench alignment chart, there are two dots shown at :math:`h = 0`. These represent the second-order Bessel (:math:`\qtc = 1 / \sqrt{3} \simeq 0.577`) and Butterworth (:math:`\qtc = 1 / \sqrt{2} \simeq 0.707`) responses, respectively. A critically damped 2\ :sup:`nd`-order closed box would require :math:`\qtc = 0.5`.

These 2\ :sup:`nd`-order results are useful when designing vented box systems, in which the user may plug the port, essentially converting the system into a closed box design. In principle, one could also show other known alignments, e.g., the second-order Linkwitz-Riley (:math:`\qtc = 0.5`), but targets outside the range between Bessel and Butterworth are rarely used when designing vented box systems. In other words, the volume of a vented box system (:math:`\alpha`) is typically chosen such that the driver in box :math:`Q` is between the Bessel and the Butterworth second-order alignment. This observation is almost valid even for the extreme case of a CD4 alignment, where in practice the box volume when the port is closed will give a system :math:`Q \approx 0.55` (the exact value depend on leakage :math:`\ql`). Any second order response where the system :math:`Q > 0.707` is considered a Chebyshev C2 alignment, even if there is not any equal ripple since a second-order response will just have a peak.

In classical theory, closed boxes are divided into the infinite baffle (IB) type and the acoustic suspension (AS) type. It is considered of the acoustic suspension type when :math:`\cmb` dominates over :math:`\cms` such that :math:`\fcb \geq 2 \fs`, which gives :math:`\alpha \geq 3`.

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
