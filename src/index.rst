.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

============
Speakerbench
============

..
   .. figure:: images/speaker_scaled.png
      :width: 20% :alt: speaker
      :align: left

`Speakerbench <https://www.speakerbench.com>`_ is a free, web-based application for modeling loudspeakers. A novel feature of the software is the use of an **advanced transducer model** that includes motor semi-inductance and suspension viscoelasticity.

This documentation extensively explains a lot of intricate details about how features and calculations under the hood are implemented in Speakerbench. As such, the documentation is for users who are looking for knowledge, for programmers who wish to interact with Speakerbench, and for ourselves to remember what we did, how, and why.

For a simple and quick one-page overview of **how to use** Speakerbench, please have a look at the `Manual <https://www.speakerbench.com/manual/index.html>`_.

Why use Speakerbench?
---------------------

Speakerbench provides a new framework for **higher-accuracy** driver simulation. Corrections to the traditional Thiele-Small approach resolve systematic errors in the description of driver losses and system impedance. For example, as shown in :numref:`impedance`, maxima in vented systems are correctly predicted with Speakerbench.

.. figure:: images/impedance.png
            :width: 80 %
	    :name: impedance
	    :align: center

            The Speakerbench advanced model (magenta) correctly predicts the impedance peak offset for
	    a woofer in a vented box. Classical Thiele-Small theory (black) misses this effect.

With a physically accurate specification of impedance and losses, you can build a loudspeaker and precisely verify the performance and power dissipation versus applied voltage. With the traditional model, losses that originate in the loudspeaker suspension are typically **misattributed** to ficticuous box leakage or port losses. With the advanced model, one can obtain a correct physical attribution of the losses.

Speakerbench workflows are separated into 4 apps:

.. admonition:: **Collect**

   1. Merge three impedance measurements into a json data container

.. admonition:: **Fit**

   2. Analyze impedance data container to compute advanced model parameters

.. admonition:: **Create**

   3. Create a standard driver datasheet

.. admonition:: **Box**

   4. Simulate the system response in an enclosure

Speakerbench doesn't do the actual impedance measurements for you; rather, you will need to do this with external hardware as outlined in this document.

.. toctree::
   quickstart
   :hidden:

.. toctree::
   :caption: Impedance
   :hidden:

   measure
   collect
   fit

.. toctree::
   :caption: Box Modeling
   :hidden:

   create
   box

.. toctree::
   :caption: Theory Notes
   :hidden:

   deltamass_theory
   box_theory
   alignment_theory
   time_theory

.. toctree::
   :caption: Resources
   :hidden:

   sampledata
   youtube
   json-docs
   glossary
   zreferences

.. image:: images/poweredbyrackhosting.png
   :width: 260px
   :target: https://rackhosting.dk/
