.. |dmn| mathmacro:: \Delta_{mn}
.. |ca| mathmacro:: C_\mathrm{A}
.. |ma| mathmacro:: M_\mathrm{A}
.. |sd| mathmacro:: S_\mathrm{D}
.. |ad| mathmacro:: a_\mathrm{D}
.. |sdp| mathmacro:: S_\mathrm{P}
.. |adp| mathmacro:: a_\mathrm{P}
.. |sbx| mathmacro:: S_\mathrm{B}
.. |caf| mathmacro:: C_\mathrm{af}
.. |cth| mathmacro:: C_\mathrm{th}
.. |cua| mathmacro:: C_\mathrm{ua}
.. |raf| mathmacro:: R_\mathrm{af}
.. |rth| mathmacro:: R_\mathrm{th}
.. |cfu| mathmacro:: C^*_\mathrm{A}
.. |rfu| mathmacro:: R^*_\mathrm{A}
.. |ws| mathmacro:: \omega_s
.. |ve| mathmacro:: \eta_v

.. _box_theory:
		    
Speakerbench Box Theory
=======================

History of enclosure models
---------------------------

The standard theory of loudspeaker enclosures was popularized by Small :cite:`small:1972a,small:1972b,small:1973b`, although the equivalent theory was presented by Benson in greater detail in his series of articles *Theory and Design of Loudspeaker Enclosures* :cite:`benson:1993`

.. figure:: images/small_vented.png
            :width: 50 %
	    :alt: small_vented
	    :align: center

	    Circuit diagram for vented loudspeaker as presented by Small in Ref. :cite:`small:1973b`.



Acoustical impedances for unfilled box
--------------------------------------

In Eq. (7.131) of Beranek :cite:`beranek:2019`, the acoustical impedances for an unfilled enclosure are derived by solving the Helmholtz equation in an unfilled rectangular enclosure. Although Beranek attempts to treat the effect of back-wall lining, we consider infinite (rigid) back-wall impedance. To extract the effective compliance and mass, we expand :math:`Z_{pq}` in powers of :math:`s` to obtain

.. math::
   Z_{pq} \sim \frac{1}{s \ca } + s \ma \, \epsilon_{pq} \; .

Here, :math:`\epsilon_{pq}` is a dimensionless :math:`2\!\times\!2` array

.. math::
   :label: eq_eps
	   
   \begin{equation}	   
   \epsilon_{pq} = \frac{1}{3} + \frac{4}{\pi} \sum_{m,n} \gamma_{mn} \frac{\coth(\pi \dmn)}{\dmn} \cos\left(\theta_p\right) \cos\left(\theta_q\right) \frac{J_1\left(\beta_p \right)}{\beta_p}  \frac{J_1\left(\beta_q \right)}{\beta_q} \; ,
   \end{equation}

where in Eq. :eq:`eq_eps` we have defined

.. math::
   :label: eq_defs
	   
   \begin{align}
	   \theta_p = &~ \frac{n \pi y_p}{l_y} \\
	   \beta_p = &~ \frac{\pi a_p}{l_z}\dmn \\
	   \dmn^2 = &~ \left( \frac{m l_z}{l_x} \right)^2 + \left( \frac{n l_z}{l_y} \right)^2 . \\
	   \gamma_{mn} = &~ 4-2 \left( \delta_{m0}+\delta_{n0} \right)
   \end{align}

The index :math:`p=1` corresponds to the driver (subscript :math:`D`) and :math:`p=2` corresponds to the port (subscript :math:`P`). We have chosen simple normalizing acoustic compliance and mass,

.. math::
   :label: eq.units
	   
	   \begin{align}
	   \ca = &~ \frac{V}{\rho c^2} = C_\mathrm{MB} \sd^2 \; , \\
	   \ma = &~ \frac{\rho \, l_z}{\sbx} \; , 
	   \end{align}

where :math:`\sbx = l_x \, l_y` is the baffle area, :math:`l_z` is the enclosure depth, :math:`\sd = \pi \ad^2` is the driver area, and :math:`V= l_x \, l_y \, l_z` is the enclosure volume. The circuit diagram for a low-frequency T-network system for an undamped vented box (box connected to a tube) is illustrated in Fig. fig.genbox.

.. figure:: images/box_port_q.png
            :width: 60 %
	    :alt: circuit
	    :align: center

	    Circuit diagram for low-frequency unfilled box (BOX) connected to
	    transmission-line tube (PORT), which radiates into free air.

Connection to Beranek factor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The end-correction factor :math:`B`, first introduced by Beranek in his 1954 book :cite:`beranek:1954`, is related to the piston self-interaction coefficient :math:`\epsilon_{11}` and defines the acoustic mass :math:`M` when the port is blocked:

.. math::
   M_{11} \doteq \epsilon_{11} \ma =  \frac{B \rho}{\pi \, \ad} \; .

Thus, we can define :math:`B` in terms of :math:`\epsilon_{11}` as

.. math::
   B = \pi \epsilon_{11} \frac{l_z \ad}{l_x l_y} \; .

End correction due to box mass
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The interior of the box provides an end correction to the port mass. In the case where the port is *external* to the box (internal flange), the exterior end correction is the usual unflanged value

.. math::
   \Delta l_\mathrm{port} = 0.6 \, \adp

whereas the internal correction is

.. math::
  \Delta l_\mathrm{port} = \frac{\epsilon_{22}-\epsilon_{21}}{l_x l_y} \, l_x \sdp

Losses due to enclosure fill
----------------------------

To incorporate box absorption, we consider the parallel circuit treated by Futtrup :cite:`futtrup:2011` based on the earlier work by Leach :cite:`leach:1989`

.. figure:: images/q_futtrup.png
            :width: 60 %
	    :alt: fillq
	    :align: center

	    Reproduction of Fig.~3 from :cite:`futtrup:2011`.

To extract the essential acoustic compliance and resistance of this circuit, we short the masses and take :math:``R_\mathrm{mf} \gg R_\mathrm{af}``. By Taylor-expanding the impedance, we can calculate the series combination of compliance :math:`\cfu` and resistance :math:`\rfu` as

.. math::
   \begin{align}
   \cfu =&~ \caf + \cth + \cua \\
   \rfu =&~ \raf \left(\frac{\caf+\cth}{\cfu}\right)^2 + \rth \left(\frac{\cth}{\cfu} \right)^2
   \end{align}

These results suggest that we can describe the effect of fill with two empirical parameters: :math:`Q_a` and :math:`\ve`. :math:`Q_a` is an analog of the box absorption of the classical Benson/Small theory, and :math:`\ve` is an effective volume expansion coefficient which is normally expected to lie in the range :math:`1.0 < \ve < 1.4`. The precise definitions are

.. math::
   \begin{align}
   \ve \doteq &~ \frac{\cfu}{\ca} \; , \\
   Q_a \doteq &~ \frac{1}{\ws \ca \rfu} \; .
   \end{align}

Thus we can generalize the classic theory with only a single new added parameter, :math:`\ve`, which characterizes the volume expansion due the conversion from adiabatic to isothermal expansion. The Futtrup theory provides estimates for :math:`\ve` and :math:`Q_a` for different materials and fill percentages, as illustrated in Fig.~\ref{fig.qgamma}. Further, in Fig.~\ref{fig.qg2}, we compare the predicted relationship of :math:`Q_a` versus $\ve$ against experimental measurement in a real filled box.

.. figure:: images/qgamma.png
            :width: 60 %
	    :alt: fillq
	    :align: center
		    
	    Theoretical :math:`Q_a` and :math:`\ve` versus amount of fill inside a test box.
	    

.. figure:: images/qg2.png
            :width: 60 %
	    :alt: fillq
	    :align: center

	    Theoretical :math:`Q_a` versus :math:`\ve` compared with measured data.
