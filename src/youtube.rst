.. meta::
   :author: Jeff Candy and Claus Futtrup
   :keywords: speakerbench,loudspeaker,driver,parameter,json,design,calculator,impedance,measurement,simulation,software,free,audio
   :description: Speakerbench Documentation

YouTube
=======

We have youtube videos that address the relevant steps:

- `STEP 0: Impedance Measurement (14:09)`_.
- `STEP 1: Impedance Data Object (5:58)`_.
- `STEP 2: Advanced Model Fit (8:10)`_.
- `STEP 3: Create Datasheet (7:40)`_.
- `STEP 4: Box Simulation (11:55)`_.

For more videos, please visit https://www.youtube.com/@Speakerbench

STEP 0: Impedance Measurement (14:09)
-------------------------------------

.. youtube:: 70iuj20HKSc?si=VcpcR9yAYP5JNkku

|

+-----------+------------------------------------------+
| Timestamp | Synopsis                                 |
+-----------+------------------------------------------+
| 0:04      | The purpose of the video                 |
+-----------+------------------------------------------+
| 0:40      | Required equipment                       |
+-----------+------------------------------------------+
| 2:08      | Driver tested                            |
+-----------+------------------------------------------+
| 2:53      | How to add mass to the driver            |
+-----------+------------------------------------------+
| 4:07      | Step 1: 4 masses                         |
+-----------+------------------------------------------+
| 6:25      | Step 2: 2 masses                         |
+-----------+------------------------------------------+
| 9:41      | Step 3: 0 masses                         |
+-----------+------------------------------------------+
| 11:15     | Saving / exporting to ZMA file           |
+-----------+------------------------------------------+
| 12:04     | Weighing the added masses, m2 and m1     |
+-----------+------------------------------------------+
| 13:38     | Summary                                  |
+-----------+------------------------------------------+

|
|

STEP 1: Impedance Data Object (5:58)
------------------------------------

.. youtube:: j37yA-Vcue0?si=57qmvYndPv9pP9LX

|

+-----------+------------------------------------------+
| Timestamp | Synopsis                                 |
+-----------+------------------------------------------+
| 0:14      | Start with prepared measurement data     |
+-----------+------------------------------------------+
| 0:38      | Explaining the ZMA input file format     |
+-----------+------------------------------------------+
| 0:57      | Load speakerbench into a browser         |
+-----------+------------------------------------------+
| 1:17      | Select the Collect Data application      |
+-----------+------------------------------------------+
| 1:35      | Getting context sensitive help           |
+-----------+------------------------------------------+
| 2:00      | Entering data into the Collect Data app  |
+-----------+------------------------------------------+
| 3:04      | Selecting  measurement files             |
+-----------+------------------------------------------+
| 4:12      | Green flags, JSON container download     |
+-----------+------------------------------------------+
| 4:59      | Looking inside the JSON output file      |
+-----------+------------------------------------------+

|
|

STEP 2: Advanced Model Fit (8:10)
---------------------------------

.. youtube:: 0ryUscAKNhE?si=aLMnD0_bQ0wL7itk

|

+-----------+------------------------------------------+
| Timestamp | Synopsis                                 |
+-----------+------------------------------------------+
| 0:22      | Choose the Fit Data app                  |
+-----------+------------------------------------------+
| 0:37      | Drop data object into the app            |
+-----------+------------------------------------------+
| 0:49      | Fitting done, evaluate fit quality       |
+-----------+------------------------------------------+
| 1:00      | Getting context sensitive help           |
+-----------+------------------------------------------+
| 1:45      | Different error ratings                  |
+-----------+------------------------------------------+
| 2:17      | Saving the ADV JSON file w. the results  |
+-----------+------------------------------------------+
| 2:29      | Looking inside the JSON output file      |
+-----------+------------------------------------------+
| 3:27      | See the resulting parameters             |
+-----------+------------------------------------------+
| 4:03      | Analysis, the Z0 tab and the Phase tab   |
+-----------+------------------------------------------+
| 4:48      | Analysis, the Zm motional impedance tab  |
+-----------+------------------------------------------+
| 5:03      | Analysis, the Ze electrical data tab     |
+-----------+------------------------------------------+
| 5:57      | Analysis, the Model Test tab             |
+-----------+------------------------------------------+
| 6:57      | Analysis, the calculated Bl value tab    |
+-----------+------------------------------------------+
| 7:45      | The README tab                           |
+-----------+------------------------------------------+

|
|

STEP 3: Create Datasheet (7:40)
-------------------------------

.. youtube:: gJ8unx38gJs?si=nV-H3lOROoAwgkrH

|

+-----------+------------------------------------------+
| Timestamp | Synopsis                                 |
+-----------+------------------------------------------+
| 0:22      | Choose the Datasheet Creator app         |
+-----------+------------------------------------------+
| 0:37      | The General tab                          |
+-----------+------------------------------------------+
| 1:01      | Drag/drop the ADV JSON File from fitter  |
+-----------+------------------------------------------+
| 1:18      | Information not filled out by import     |
+-----------+------------------------------------------+
| 2:13      | Tooltips                                 |
+-----------+------------------------------------------+
| 2:26      | Entering data into Datasheet Creator     |
+-----------+------------------------------------------+
| 3:42      | Advanced sheet: fill out Dd (or Sd)      |
+-----------+------------------------------------------+
| 4:07      | Simple tab: fill out Xmax                |
+-----------+------------------------------------------+
| 4:36      | Output SBD JSON file for download        |
+-----------+------------------------------------------+
| 4:46      | The JSON Summary tab                     |
+-----------+------------------------------------------+
| 5:05      | Copy-paste JSON summary into VituixCAD   |
+-----------+------------------------------------------+
| 5:37      | The README tab                           |
+-----------+------------------------------------------+
| 5:50      | JSON container download                  |
+-----------+------------------------------------------+
| 6:18      | The IMPORT tab                           |
+-----------+------------------------------------------+

|
|

STEP 4: Box Simulation (11:55)
------------------------------

.. youtube:: NE-SvRN7bMo?si=Tsprj_MIxAUfXZ2d

|

+-----------+------------------------------------------+
| Timestamp | Synopsis                                 |
+-----------+------------------------------------------+
| 0:15      | You cannot use BOX simulation w/o data   |
+-----------+------------------------------------------+
| 1:29      | No upload area for box simulation        |
+-----------+------------------------------------------+
| 1:48      | Start in the Datasheet Creator app       |
+-----------+------------------------------------------+
| 2:01      | Datasheet Creator accepts SBD files      |
+-----------+------------------------------------------+
| 3:45      | Switching to the BOX simulation          |
+-----------+------------------------------------------+
| 4:02      | The DRIVER tab in the box simulator      |
+-----------+------------------------------------------+
| 4:10      | Initialized input for box simulation     |
+-----------+------------------------------------------+
| 4:58      | Top-down setting of input parameters     |
+-----------+------------------------------------------+
| 5:14      | The INFO tab                             |
+-----------+------------------------------------------+
| 6:20      | The SPL response tab w. port output      |
+-----------+------------------------------------------+
| 6:42      | The box mode indicator (vertical line)   |
+-----------+------------------------------------------+
| 7:18      | The SPL BOX and Xmax limit response      |
+-----------+------------------------------------------+
| 7:46      | The Impedance response                   |
+-----------+------------------------------------------+
| 7:50      | The Excursion plot                       |
+-----------+------------------------------------------+
| 8:22      | The port air Velocity plot               |
+-----------+------------------------------------------+
| 8:48      | The Group Delay plot                     |
+-----------+------------------------------------------+
| 9:41      | The Step response and how to activate it |
+-----------+------------------------------------------+
| 10:35     | The Pole-Zero plot in the STEP tab       |
+-----------+------------------------------------------+

