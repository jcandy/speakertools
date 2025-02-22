.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

=====================
Impedance Measurement
=====================

.. note::
   **STEP 0**: This section describes how to measure impedance data required by Speakerbench. You will need to do this on your own using a measurement system. Once done, you can :doc:`create a data object <collect>`.

`Thiele-Small parameters <https://en.wikipedia.org/wiki/Thiele/Small_parameters>`_ are classically determined by adding mass to the moving part (cone) of the loudspeaker. Then, by comparing the weighted to the unweighted free-air impedance measurements, one can compute all model parameters. In the present case, to extract parameters for the new advanced model, the fitting procedure will require **three impedance measurements**

1. with a large added mass :math:`m_2`
2. with a small added mass :math:`m_1` (roughly half :math:`m_2`)
3. without added mass

Ideally, :math:`m_2` will be in the same ballpark as the moving mass of the speaker you're measuring. Ballpark meaning it's not critical to be exact. The added-masses (in grams) will need to be entered into the data-collecting app.

.. important::
   It is important to measure on a precision scale and specify the masses as accurately as possible.

These three impedance data files must be uploaded to the web app in ZMA file format, which lists 3 columns of data: frequency (column 1), impedance magnitude (column 2) and impedance phase (column 3). Acceptable ZMA files may contain header data (ignored) marked with an asterisk (*). Ideally the steady-state impedance measurements will be logarithmic, range from about 10 Hz to 20 kHz, and contain several hundred data points. However, linear frequency measurements with
thousands of data points is also acceptable. Since the goal is to determine the advanced model parameters as accurately as possible, we recommend that :math:`m_2` consist of 4 masses and that :math:`m_1` consist of half these masses (with the other half removed from the cone). The four masses are placed in a cross-pattern (equally spaced) in a mechanically stable way near the voice coil and with a good physical connection to the voice coil. All 4 masses should be of approximately the same weight, yet for high precision they are individually marked and their weight measured individually before applied to the cone. This is illustrated in :numref:`fig.mass`.

.. figure:: images/mass.jpg
            :width: 95 %
            :alt: Drivers with and without added mass
            :align: center
            :name: fig.mass

	    Driver with (1) with added mass :math:`m_2`, (2) with added mass :math:`m_1`, (3) without added mass
	
Measure the impedance with all 4 mass-loads (:math:`m_2`, left panel) and save this data to the **first ZMA file**. Now very gently remove the two diagonal masses, leaving the remaining masses balanced and rocking modes prevented during the measurement of the speaker. Remeasure the impedance with the remaining two masses (:math:`m_1`, middle panel) and save this data to a **second ZMA file**. Now very gently remove the two masses leaving the bare cone (right panel). Measure the impedance of the unweighted cone and save this data to a **third ZMA file**.

To add mass we use `Blu Tack <https://en.wikipedia.org/wiki/Blu_Tack>`_, with a **non-magnetic** metal nut or coin optionally embedded for increased density. Be aware that magnetic materials can interact with the magnet system giving spurious results. As the masses are removed from the cone, it is good practice remeasure their weight to ensure that you know how much mass you've removed from the cone. These masses should be the values you measured before. The reason we measure in reverse order, as described above, is because applying the masses to the speaker may stress the mechanical suspension parts, which alters the viscoelastic properties. It is easier to remove the masses without stressing the parts and potentially without the cone moving at all. This will ensure the highest possible precision in determining all parameters, including the viscoelastic :math:`\beta` value.

Some examples of measurement equipment, which support saving impedance measurements in the ZMA file format, are

- `Smith & Larson Woofer Tester Pro <https://audioxpress.com/article/voice-coil-spotlight-the-smith-larson-audio-analyzers>`_ (verified to work, highly recommended)
- `ARTA LIMP <http://www.artalabs.hr>`_ (software only)
- `Room EQ Wizard (REW) <https://www.roomeqwizard.com>`_, using `Text Export <https://www.roomeqwizard.com/help/help_en-GB/html/file.html#filewritemeasured>`_ (software only)
- `Dayton Audio DATS V3 <https://www.daytonaudio.com/product/1650/dats-v3-computer-based-audio-component-test-system>`_

We recommend either a stepped-sine signal measurement such that all frequency points are measured under steady-state conditions, or a Farina sweep :cite:`farina:2000` with sufficiently long duation (10s) to resolve low frequencies. Note that REW and DATS V3 both use a sweep.
