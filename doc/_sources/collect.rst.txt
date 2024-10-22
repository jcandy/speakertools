.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

Impedance Data Object
=====================

.. note::
   **STEP 1**: This section describes how to create an impedance data object (Z-file).

We provide a web app to collect the previous impedance measurements (and masses) into a single file. This single (JSON) object can be stored on your computer locally and later uploaded into the parameter fitting app. In principle this step is only a required step because we felt is was a practical way to store measurements, a practical way to feed the data to the fitter, and should anything strange occur, a practical way for you to share the data with us so we can potentially investigate.

The data collection app requires the following input:

1. ZMA file containing impedance measurement of unweighted driver
2. ZMA file containing impedance measurement of driver with added mass :math:`m_1`
3. ZMA file containing impedance measurement of driver with added mass :math:`m_2`
4. The value of :math:`m_1` in grams
5. The value of :math:`m_2` in grams

This app also provides an optional comment field. We recommended that you type the driver name into this field. An optional field for specification of the input voltage is also available. Specifying the voltage is not a requirement either, but it's good practice to record this because we know that the suspension compliance will depend on the input
level. Remember to fill out these optional fields before you complete entering the five inputs.

The comment field is the first entry in the data object such that if you open up the file in a text editor, you can read your comment in plain text (at the top). This will help you identify the measurement. When measuring your driver, we recommend that you follow steps outlined in :doc:`measure`.

.. important::
   All three measurements in the ZMA files must contain the same number of datapoints at the same measurement frequencies.


















