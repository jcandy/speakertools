.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

==================
Advanced Model Fit
==================

.. note::
   **STEP 2**: This section will show you how to fit the Z-file data from :doc:`STEP 1 <collect>` into a parameter file (ADV-file).

This app uses the data stored in the previously generated JSON data container to generate a nonlinear fit to the advanced driver model. The free-air impedance in this model is given by

.. math::
   Z = \re + s \leb + \left( \frac{1}{\rss} + \frac{1}{s \le}
   + \frac{1}{\sqrt{s} \ke} \right)^{-1} + \frac{\bls}{\mathbb{Z}_{\rm mot}} \; ,

where :math:`\mathbb{Z}_{\rm mot}` is the mechanical impedance of the transducer

.. math::
   \mathbb{Z}_{\rm mot} = s \mms + R_0 + \displaystyle \frac{1}{C_0} \left[ 1+\beta\ln(1+\omega_0/s)\right] \; .

The equivalent electrical circuit for the driver in free air is

.. figure:: images/elec_total.png
            :width: 60%
	    :alt: electrical circuit
	    :align: center

	    Electrical-equivalent circuit for transducer in free air, where :math:`\mathbb{Z}_{\rm mot}`
	    is the mechanical impedance of the suspension

The parameter :math:`\omega_0` is a transition frequency, chosen to be :math:`\omega_0 = 1.5 \, \ws = 3 \pi \fs`, such that :math:`\fs` (the driver resonant frequency in Hz) will be determined by the fitting process. Some aspects of the *dual-added-mass* algorithm are described in our 2017 AES article :cite:`candy:2017`, whereas other aspects are proprietary. The fit procedure is complicated, but provides a robust and accurate estimation of the model parameters. The advanced model utilizes what we consider to be the best analytic forms for both the *electrical impedance* (the
Thorborg-Futtrup inductance model :cite:`thorborg:2011`) and the *mechanical impedance* (the Knudsen-Jensen LOG model of viscoelasticity :cite:`knudsen:1993`), with the added Retardation Spectra function as described by Agerkvist and Ritter :cite:`agerkvist:2010`. The fit parameters are suitable for high-accuracy loudspeaker box simulations (for designing loudspeaker systems). Please note that all information (including input variables and results) is stored in your browser and nothing is saved to the server (not even temporary data). At the end you should export the data and save the results to your local hard drive. If you don't and close the browser window, the data will be lost.

To compute the fit, simply upload the JSON container of the previous section into the app. The fit analyzes your data and the fit result and provides you with a quality rating: Excellent, Good, Fair or Sorry.

We published an article in the *Loudspeaker Industry Sourcebook 2020* about Speakerbench :cite:`LIS:2020` which explains some aspects of the fitting and how to analyze the results. More background information can be found in our ALMA International Symposium 2017 presentation :cite:`futtrup:2017`.
