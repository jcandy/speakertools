.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,impedance,measurement,simulation,port
   :description: Speakerbench Documentation

==============
Box Simulation
==============

.. note::
   **STEP 4**: You can perform box simulations using data created (or imported) in :doc:`STEP 3 <create>`. You can also import data from the massive |speakerdata|!

.. |speakerdata| raw:: html

   <a href="https://loudspeakerdatabase.com" target="_blank">Loudspeaker Database</a>

The purpose of measuring the driver impedance (STEP 0) and determining the advanced parameters (STEPS 1-3) is to accurately predict the behavior in a box before it is built. Speakerbench offers a powerful box simulator that can calculate various quantities of interest using the advanced parameter model, or with the legacy Thiele-Small model.

To load parameters for a driver into the box simulator, you need to use the :doc:`Datasheet Creator <create>`. When the data visible in the Datasheet Creator generates a JSON output, the data is stored in your local browser memory and automagically shows up in the box simulator. Thereafter, box parameters can be varied in the *Settings* tab to simulate the system behavior. A detailed description of the underlying theory is also summarized in the :ref:`box_theory` section.

Enclosure Options
-----------------

Two enclosure options supported by Speakerbench are:

**classic**
     The classic series resistance-compliance model for the enclosure as described by Small :cite:`small:1972a`, Benson :cite:`benson:1993` and others.

**Beranek**
   A low-frequency 2-port model for the enclosure matrix that includes rigorous acoustic mass elements derived by solving the Helmholtz equation. Losses and volume expansion due to fill are included. The mass elements computed by this model depend on the box geometry.

The Beranek-Mellow transmission matrix formulation :cite:`beranek:2012` is used to implement both options. The calculated results are reliable only for the low-frequency range, below the first box resonance.

Port Options
------------

For bass reflex simulation, Speakerbench supports two port models

**classic**
   The classic series mass-resistance model for vent impedance as described by Small, Benson and others.

**T-line**
   An arbitrary-frequency transmission-line model that includes reflections and pipe resonance. The dissipation in the vent is chosen to match the classic theory at low frequency.

Alignments
----------

To facilitate choosing the box volume and vent tuning, Speakerbench will propose values based on standard 4th-order bass-reflex alignments :cite:`small:1973c`. A comprehensive description is given in the :ref:`Classic Vented Alignments` section.

Transient Response
------------------

In addition to the usual frequency-domain plots of SPL, velocity and displacement, Speakerbench can also calculate the step response, enabled by switching on the *Time domain* toggle in the Settings tab. This is more computationally intensive, so we recommend to leave it off until the step response is desired. Two plots are given: (1) the step response and (2) the contour map of the transfer function. Since Speakerbench implements an advanced transducer model, with viscoelasticity and semi-inductance, the time domain response is calculated with a contour integral algorithm as documented in :cite:`candy:2018`.
