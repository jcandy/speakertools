.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

Sample Data
===========

The following datafiles can be used to test all Speakerbench modules.

.. csv-table:: **Sample Data**
   :header: Object, Datafile, Needed by
   :widths: 25, 15, 15

   Driver unweighted,          :download:`ZMA file <data/L16RNX_0g_242_27mV.zma>`,Collect data (1)
   Driver plus 8.017 grams,    :download:`ZMA file <data/L16RNX_8_017g_242_27mV.zma>`,Collect data (1)
   Driver plus 16.048 grams,   :download:`ZMA file <data/L16RNX_16_048g_242_27mV.zma>`,Collect data (1)
   Full 3-measurement dataset, :download:`JSON Z-file <data/Z_L16RNX.json>`,Calculate fit (2)
   Fit parameters,             :download:`JSON ADV-file <data/ADV_L16RNX.json>`,Datasheet creator (3)


For examples of SBD-files (Speakerbench datasheet in JSON format) you can use the Import tab in the Datasheet creator.
