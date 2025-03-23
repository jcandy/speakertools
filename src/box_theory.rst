.. _box_theory:

=======================		
Speakerbench Box Theory
=======================

History of enclosure models
---------------------------

The standard theory of loudspeaker enclosures was popularized by Small :cite:`small:1972a,small:1972b,small:1973b`, although the equivalent theory was presented by Benson in greater detail in his series of articles *Theory and Design of Loudspeaker Enclosures* :cite:`benson:1993`

.. subfigure:: AB
   :name: fig.bensonsmall
   :width: 90%
   :gap: 80px
   :align: center
   :subcaptions: below

   .. image:: images/box/small_vented.png
      :alt: Acoustical circuit (Small)
   .. image:: images/box/benson_vented.png
      :alt: Mechanical circuit (Benson)

   Acoustical circuit for vented loudspeaker as presented by Small in Ref. :cite:`small:1973b` (left) compared with equivalent mechanical circuit by Benson :cite:`benson:1993` (right).

DRIVER: the advanced model
--------------------------

The *blocked electrical* and *motional* impedances of the driver are modified from the standard Theile-Small expressions according to

.. math::
   :label: eq.oldnew
	
   \begin{align*}	
   \ze & = & \re + s L_3 & \longrightarrow & \re + s \leb + \left( \frac{1}{\rss} + \frac{1}{s \le}
   + \frac{1}{\sqrt{s} \ke} \right)^{-1} \; , \\
   \mathbb{Z}_{\rm mot} &=& s \mms + \rms + \frac{1}{s\cms} & \longrightarrow &
   s \mms + R_0 + \displaystyle \frac{1}{s C_0 \left[ 1+\beta\ln(1+\omega_0/s)\right]} \; .
   \end{align*}

The equivalent electrical circuit for the driver in free air is given in :numref:`fig.elec_total`.

BOX: T-network enclosure model
------------------------------

The classic form for the acoustic impedance of enclosure is

.. math::
   Z_\mathrm{box} =  \frac{1}{s \cab} + \rab

where :math:`\cab` is the acoustic compliance and :math:`\rab` is the box absorption. There is no model for the classical absorption and so it is purely an empirical parameter.

A vented enclosure is represented not by a single circuit element but rather by a 2-port network. In Eq. (7.131) of Beranek :cite:`beranek:2019`, the acoustical network impedances for an unfilled enclosure are derived by solving the interior Helmholtz equation. Although Beranek attempts to treat the effect of back-wall lining, we consider infinite (rigid) back-wall impedance. To extract the effective compliance and mass, we expand :math:`Z_{pq}` in powers of :math:`s` to obtain the network impedances

.. math::
   :label: eq.zpq
	
   Z_{pq} = \frac{1}{s \cab } + s \mab \, \epsilon_{pq} \; .

In this expression we have ignored terms of order :math:`s^2` and higher. By ignoring these terms we limit the applicability of the theory to the frequency range where the neglected terms are small. Note that in this section, all masses and compliances are assumed to be in acoustic units. When mechanical units are used, a lower-case :math:`m` subscript will be added. The quantity :math:`\epsilon_{pq}` is a dimensionless :math:`2\!\times\!2` array

.. math::
   :label: eq.eps
	
   \begin{equation}	
   \epsilon_{pq} = \frac{1}{3} + \frac{4}{\pi} \sum_{m,n} \gamma_{mn} \frac{\coth(\pi \dmn)}{\dmn} \cos\left(\theta_p\right) \cos\left(\theta_q\right) \frac{J_1\left(\beta_p \right)}{\beta_p}  \frac{J_1\left(\beta_q \right)}{\beta_q} \; ,
   \end{equation}

where in Eq. :eq:`eq.eps` we have defined

.. math::
   :label: eq.defs
	
   \theta_p      & = \frac{n \pi y_p}{L_y} \; , \\
   \beta_p       & = \frac{\pi a_p}{L_z}\dmn \; , \\
   \dmn          & = \sqrt{\left( \frac{m L_z}{L_x} \right)^2 + \left( \frac{n L_z}{L_y} \right)^2} \; , \\
   \gamma_{mn}   & = 4-2 \left( \delta_{m0}+\delta_{n0} \right) \; .

The indices :math:`p=(1,2)` correspond to the driver and port

.. math::
   \begin{array}{cll}
   p = 1 & \ap = \text{Port radius}   & \yp = \text{Port height} \\
   p = 2 & \ad = \text{Driver radius} & \yd = \text{Driver height} 
   \end{array}
   
We have chosen simple normalizing acoustic compliance and mass,

.. math::
   :label: eq.units
	
   \cab & = \frac{\vb}{\rho c^2} = C_\mathrm{MB} \sd^2 \; , \\
   \mab & = \frac{\rho \, L_z}{\sb} \; ,

where :math:`\sb = L_x \, L_y` is the baffle area of the enclosure (inside the box), :math:`L_z` is the enclosure depth, :math:`\sd = \pi \ad^2` is the driver area, and :math:`\vb = L_x \, L_y \, L_z` is the enclosure volume. The 2-port circuit diagram for a vented box at low frequency is illustrated in :numref:`fig.box`.

.. subfigure:: AB
   :name: fig.box
   :width: 90%
   :gap: 80px
   :align: center
   :subcaptions: below

   .. image:: images/box/box_classic.png
   .. image:: images/box/box_q.png

   Comparison of T-network circuit for classic (left) model versus T-network circuit for Beranek (right) model.
	
In the model shown in :numref:`fig.box`, we have retained the empirical box absorption which can be equivalently written as an absorption Q:

.. math::
   \qa \doteq \frac{1}{\ws \cab \rab} \; .

The compliance :math:`\cfu` is a modified compliance that accounts for volume expansion due the conversion from adiabatic to isothermal expansion. This effect is decribed by Futtrup :cite:`futtrup:2011` and also in the earlier work by Leach :cite:`leach:1989`. A more rigorous treatment of wave propagation in porous media outside the context of loudspeaker enclosures is given by Wilson :cite:`wilson:1993`, Tarnow :cite:`tarnow:2002` and others.
The definition is

.. math::
   \cfu \doteq \deltv \, \cab \; ,

where :math:`1.0 < \deltv < 1.4`. The factor of 1.4 corresponds to :math:`\gamma = C_P/C_V`. At this time, there is no general theory which can connect material properties of fill to precise values of :math:`\rab` and :math:`\deltv`. For an unfilled enclosure, :math:`\deltv=1`, whereas for an enclosure densely filled with fiberglass, :math:`\deltv \simeq 1.4` in the limit, when operating isothermal.

Connection to Beranek factor
............................

The end-correction factor :math:`B`, first introduced by Beranek in his 1954 book :cite:`beranek:1954`, is related to the piston self-interaction coefficient :math:`\epsilon_{11}` and defines the acoustic mass :math:`M` when the port is blocked:

.. math::
   M_{11} \doteq \epsilon_{11} \mab =  \frac{B \rho}{\pi \, \ad} \; .

Thus, we can define :math:`B` in terms of :math:`\epsilon_{11}` as

.. math::
   B = \pi \epsilon_{11} \frac{L_z \, \ad}{L_x \, L_y} \; .


PORT: T-network port model
--------------------------

The classic form for the acoustic impedance of the port is

.. math::
   Z_\mathrm{port} =  \rap + s \map

This model for the port also contains an empirical loss factor :math:`\rap` that cannot be computed from first-principles but can only be empirically determined. This form is also valid only for wavelengths much longer than the port length.

.. subfigure:: AB
   :name: fig.port
   :width: 90%
   :gap: 80px
   :align: center
   :subcaptions: below

   .. image:: images/box/port_classic.png
   .. image:: images/box/port_q.png
	
   T-network diagrams for classic (left) and T-line (right) ports. Here, :math:`\zeta` is a complex propagation constant defined in :eq:`eq.zeta`, :math:`Z = \rho c/\sp` is the specific acoustic impedance of air in the vent, :math:`M_\mathrm{API}` is the inner port radiation mass, and :math:`M_\mathrm{APO}` is the outer port radiation mass.

The complex propagation constant used in Speakerbench is

.. math::
   :label: eq.zeta
	
   \zeta = \left( s+\frac{\wb}{\qps} \right) \frac{\lpp}{c} \; .

We use a star to denote a modified form of :math:`\qp` used as the Speakerbench input for both classic and transmission line ports. This modified definition is done for convenience and is related to the traditional definition according to

.. math::
   :label: eq.qp
	
   \qps \doteq \frac{\lpp}{\lp} \frac{1}{\wb\cab\rap} = \frac{\lpp}{\lp} \qp \; ,

where :math:`\lpp` is the physical port length, and :math:`\lp` is the effective port length.

End corrections
...............

Because there is no precise theory for the effective port length, :math:`\lp`, in terms of the physical port length, :math:`\lpp`, it is customary to first define the effective length in terms of the resonant frequency :math:`\wpb` as

.. math::
   \wpb^2 = \frac{1}{\cab \map} = \frac{\sp \, c^2}{\vb \lp} \; .

To derive this result we have used

.. math::
   \map = \frac{\mmp}{\sp^2} = \frac{\rho\vp}{\sp^2} = \frac{\rho \,\lp}{\sp} \; .

The interior of the box provides an end correction to the port mass. In the case where the port is *external* to the box (internal flange), the exterior end correction is the usual unflanged value radiation mass :math:`M_\mathrm{rad} = \rho \, \lpo/\sp` where

.. math::
   \lpo = 0.6 \, \ap

The volume velocity through the radiation mass represents the sound exiting the vent, whereas the velocity through the :math:`\mathrm{csch}` branch is associated with reflections and compression in the tube. The internal correction is

.. math::
  \lpi = \frac{\epsilon_{22}-\epsilon_{21}}{\sb} \sp \, L_z

Thus, the effective length of the port is given by

.. math::
   \lp = \lpi + \lpp + \lpo

Summary of acoustic masses
--------------------------

The identification and calculation of acoustic masses is complicated and depends strongly on geometry. In an effort to clarify the physical interpretation, we tabulate the relevant acoustic masses in :numref:`tab.mass` below.

.. csv-table:: **Box and vent acoustic masses**
   :align: center
   :header: "", *outer*, *intrinsic*,*inner*
   :widths: 25, 25, 25, 25
   :name: tab.mass

   port,":math:`\displaystyle \left(0.6 \, \ap\right)\frac{\rho}{\sp}`",":math:`\displaystyle \frac{\rho \, \vp}{\sp^2}`",":math:`\displaystyle \left(\epsilon_{22}-\epsilon_{12}\right)\,\mab`"
   box,":math:`\displaystyle \left(0.6 \, \ad\right) \frac{\rho}{\sd}`",":math:`\displaystyle \frac{\mmd}{\sd^2}`",":math:`\displaystyle \epsilon_{11} \, \mab`"

The **outer** masses result from radiation into free space. For both the driver and port, the coefficient of 0.6 applies to unflanged radiation. Note that for flanged radiation (infinite baffle) the coefficient is 0.85. The **intrinsic** box and port masses are the moving masses of the driver, and port air plug, respectively. For the driver, it is assumed that the outer mass is already contained in the advanced model :math:`\mms` whereas for the port, we assume it is mounted externally to justify the unflanged assumption. The **inner** masses, finally, require numerical evaluation of the Helmholtz matrix elements :math:`\epsilon_{pq}` via Eq. :eq:`eq.eps`.
