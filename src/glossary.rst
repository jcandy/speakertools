.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

===================
Glossary of symbols
===================

.. csv-table:: Glossary of symbols
   :align: center
   :header: symbol,definition
   :widths: 10,50
   :name: tab.glossary

   ":math:`p`", "Air pressure"
   ":math:`T`", "Air temperature"
   ":math:`V`", "Air volume"
   ":math:`\rho_0`", "Air density (=1.20 :math:`\kgm`)"
   ":math:`c`", "Velocity of sound in air (=344 :math:`\mps`)"
   ":math:`\eta_0`", "Reference efficiency, often in \%"
   ":math:`\gamma`", "Ratio of specific heat capacities :math:`= C_p / C_V`"
   ":math:`C_p`", "Constant pressure specific heat capacity of air, in :math:`\heatcap`"
   ":math:`C_V`", "Constant volume specific heat capacity of air, in :math:`\heatcap`"


.. csv-table:: Glossary, driver parameters
   :align: center
   :header: symbol,definition
   :widths: 10,50

   ":math:`\re`", "Electrical (DC) resistance of driver voice coil"
   ":math:`\leb`", "Electrical inductance of driver voice coil, in series with :math:`\re`"
   ":math:`\le`", "Electrical parallel inductance of driver voice coil (advanced parameter)"
   ":math:`\ke`", "Electrical parallel semi-inductance of driver voice coil (advanced parameter)"
   ":math:`\rss`", "Electrical parallel resistance of driver voice coil (advanced parameter)"
   ":math:`\bl`", "Motor strength force factor in N/A (or Tm)"
   ":math:`\fs`", "Effective free air resonant frequency of the loudspeaker driver, in :math:`\hz`"
   ":math:`\ws`", "Resonant frequency of the loudspeaker driver :math:`= 2 \pi\fs`, in rad/s"
   ":math:`\qts`", "Driver total :math:`Q` (Thiele/Small parameter)"
   ":math:`\qes`","Driver electrical :math:`Q` (T/S parameter)"
   ":math:`\qms`", "Driver mechanical :math:`Q` (T/S parameter)"
   ":math:`\mmd`", "Intrinsic moving mass of driver, without air load"
   ":math:`\mms`", "Moving mass of driver, including air load in free air"
   ":math:`\cms`", "Effective mechanical compliance of driver suspension"
   ":math:`\cas`", "Effective acoustical compliance of driver suspension :math:`=\cms \, \sd^2`"
   ":math:`\vas`", "Acoustical volume of air, equivalent to driver suspension compliance :math:`=\rho_0 \, c^2 \, \cms \, \sd^2`"
   ":math:`\rms`", "Effective mechanical damping resistance"
   ":math:`\rml`", "Effective mechanical resistance due to enclosure leak"
   ":math:`\lambda_K`", "Mechanical viscoelastic log-model (base 10) parameter used by many (e.g. Knudsen, Klippel)"
   ":math:`\beta`", "Mechanical viscoelastic log-model (base e) parameter used in Speakerbench (advanced parameter)"
   ":math:`\clog`", "Mechanical viscoelastic compliance parameter of driver (advanced parameter)"
   ":math:`\rlog`", "Mechanical viscoelastic damping parameter of driver (advanced parameter)"
   ":math:`\flog`", "Mechanical viscoelastic resonant frequency parameter of driver (advanced parameter)"
   ":math:`\sd`", "Effective surface area of driver diaphragm (the shadow area)"
   ":math:`\xmax`", "Max peak linear excursion (displacement) of driver diaphragm"
   ":math:`L_3`", "Effective inductance defined at +3dB impedance (half power)"


.. csv-table:: Glossary, system parameters
   :align: center
   :header: symbol,definition
   :widths: 10,50

   ":math:`B`", "Beranek mass loading factor"
   ":math:`\fpb`", "Resonant frequency of the vented enclosure, i.e., loudspeaker port in box (system), in Hz"
   ":math:`\wpb`", "Resonant frequency of the loudspeaker (ported) system :math:`= 2 \pi\fpb`, in rad/s"
   ":math:`h`", "System tuning ratio :math:`= \wpb/\ws` or :math:`= \omega_B/\ws`"
   ":math:`R_\mathrm{S}`", "Electrical series resistance"
   ":math:`M_{AB}`", "Acoustic mass related to the baffle (and Beranek factor) :math:`= \rho_0 \, \vb /\sb^2 = \rho_0 \, L_Z/\sb`"
   ":math:`\qa`", "Box fill absorption loss :math:`Q`"
   ":math:`\ql`", "Box leakage loss :math:`Q`"
   ":math:`\mmf`", "Mass of air radiation load on front side of driver diaphragm when mounted in a box"
   ":math:`\mmr`", "Mass of air radiation load on rear side of driver diaphragm when mounted in a box"
   ":math:`\mmp`", "Mass of port air slug :math:`= M_\mathrm{AP} \sd^2`"
   ":math:`\cmb`", "Box mechanical compliance from air in the box"
   ":math:`\cab`", "Acoustical compliance of air in the box :math:`= \vb/(\rho_0 \, c^2)`"
   ":math:`\fcb`", "Resonant frequency of the loudspeaker driver in closed box, in :math:`\hz`"
   ":math:`\qtc`", "Total :math:`Q` of driver in closed box"
   ":math:`\alpha`", "Compliance ratio :math:`=\cas / \cab = \vas / \vb`"

Converting between domains
--------------------------

In loudspeaker theory, it is common to represent the parameters in electrical equivalent circuits and convert between the electrical, the mechanical and the acoustical domains by transformation with :math:`\bl` and :math:`\sd` such that the same parameter can be represented in several domains. In the table below we show a few parameters and their domain transformations:

+------------------------+----------------------------------------------------+---------------------------------------------------+-----------------------------------------------------+
| Name                   | Electrical                                         | Mechanical                                        | Acoustical                                          |
+========================+====================================================+===================================================+=====================================================+
| Voice coil resistance  | :math:`\re`                                        | :math:`R_\mathrm{ME} = \frac{\bls}{\re}`          | :math:`R_\mathrm{AE} = \frac{R_\mathrm{ME}}{\sd^2}` |
+------------------------+----------------------------------------------------+---------------------------------------------------+-----------------------------------------------------+
| Suspension resistance  | :math:`\res = \frac{\bls}{\rms}`                   | :math:`\rms`                                      | :math:`R_\mathrm{AS} = \frac{\rms}{\sd^2}`          |
+------------------------+----------------------------------------------------+---------------------------------------------------+-----------------------------------------------------+
| Enclosure Air Leakage  | :math:`R_\mathrm{EL} = \frac{\bls}{R_\mathrm{ML}}` | :math:`R_\mathrm{ML} = \sd^2 \cdot R_\mathrm{AL}` | :math:`R_\mathrm{AL}`                               |
+------------------------+----------------------------------------------------+---------------------------------------------------+-----------------------------------------------------+

The transformation between the mechanical and acoustical domain is straightforward with :math:`\sd^2` whereas the transformation between the electrical and mechanical domain with :math:`\bls` brings the parameter in the denominator (inverting). For resistance this remains a resistance, but for masses (represented by inductors in mechanical equivalent circuits) they transform into capacitors in the electrical domain, and for compliance (represented by capacitors in mechanical equivalent circuits) they transform into inductors in the electrical domain:

+------------------------+------------------------------------------+-----------------------------------+--------------------------------------------+
| Name                   | Electrical                               | Mechanical                        | Acoustical                                 |
+========================+==========================================+===================================+============================================+
| Driver moving mass     | :math:`\cmes = \frac{\mms}{\bls}`        | :math:`\mms`                      | :math:`M_\mathrm{AS} = \frac{\mms}{\sd^2}` |
+------------------------+------------------------------------------+-----------------------------------+--------------------------------------------+
| Suspension compliance  | :math:`\lces = \bls \cdot \cms`          | :math:`\cms`                      | :math:`\cas = \cms \cdot \sd^2`            |
+------------------------+------------------------------------------+-----------------------------------+--------------------------------------------+
| Enclosure compliance   | :math:`L_\mathrm{CEB} = \bls \cdot \cmb` | :math:`\cmb = \frac{\cab}{\sd^2}` | :math:`\cab`                               |
+------------------------+------------------------------------------+-----------------------------------+--------------------------------------------+

For the electrical equivalents of these reactive components, we add additional letters in the subscript indicating their origin.
