Box Simulation
==============

.. note::
   **STEP 4**: You can use data created or imported from :doc:`STEP 3 <create>`, or imported from the `Loudspeaker Database <https://loudspeakerdatabase.com>`_.

The point of measuring the driver and determining the parameters is to be able to simulate (predict) the behavior in a box before it is actually built. Here we offer a powerful box simulator that can calculate various quantities of interest using the advanced parameter model, or with the legacy Thiele-Small model.

To load parameters for a driver into the box simulator, you need to use the :doc:`Datasheet Creator <create>`. When the data visible in the Datasheet Creator generates a JSON output, the data is stored in your local browser memory and automagically shows up in the box simulator. Hereafter you are able to adjust box parameters in the *Settings* tab and simulate the system behavior.

Enclosure Options
-----------------

The box models supported by Speakerbench are:

**Simple**
    Beranek-Mellow transmission matrix formulation :cite:`beranek:2012` with a simple (classic) compliance model for the box matrix. Damping material settings are ignored. 

**Futtrup**
   Low-frequency circuit model for enclosures with added damping material as described in :cite:`futtrup:2011`. In the no-fill limit this still includes acoustic mass effects.

**T-net**
   Beranek-Mellow transmission matrix formulation with a low-frequency 2-port model for the box matrix including acoustic mass and compliance. When fill is added, the impedance and wavenumber are replaced by the complex (lossy) values from Tarnow :cite:`tarnow:2002`. This method has been checked against measurements and we believe it is the most accurate.

All the enclosure models are reliable only for the low-frequency range, below the first box resonance. With either the T-net or the Futtrup model you can choose between a number of different damping materials, either from Polyester or PET fiber, or from Glass wool (the number indicates the density in kg/m3).

Port Options
------------

For bass reflex simulation, Speakerbench supports two port models

**Simple**
   The classic circuit model (mass and resistance)

**T-line**
   Transmission-line that includes reflections and pipe resonance. The dissipation in the vent is chosed to match the simple theory at low frequency.

Time Domain
-----------

In addition to the usual frequency-domain plots of SPL, velocity and displacement, Speakerbench can also calculate the step-response, enabled by switching on the *Time domain* toggle in the Settings tab. This is more computationally intensive, so we recommend to leave it off until the step response is desired. Two plots are given: (1) the step response and (2) the contour map of the transfer function. Since Speakerbench implements an advanced transducer model, with viscoelasticity and semi-inductance, the time domain response is calculated with a contour integral algorithm as documented in :cite:`candy:2018`.
