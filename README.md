EQLoc (V 1.2.1)
---------

An automated P-phase picking procedure and a grid-search/inversion-based method to locate (local) events. 

In the current version, the normalized data and their corresponding sta/lta diagram are used to enhance the phase picking procedure.


Requirements
------------

1- Sac

2- GMT (Version 5.x)

3- Pyrocko (on python 3.x)

4- Obspy (on python 3.x)


Note:
-----

At your first test, run "bash Locate -h" to get instructed.

Supply the Input/ directory with vertical components of different stations. Data must be in SAC format containing at least "$LTA_P" seconds of noise length before P arrival.

Two files are required in advance; (1) station info file (see the example file stations.dat; do not change the file name), and (2) velocity model (see the example file; set the file name to VM_Name parameter). 

In this version, we use the STA/LTA diagram instead of the common STA/LTA sliding window to accelerate and simplify the picking procedure. The results will be stored in the sac files to be used in the location procedure. Adjust the related parameters (e.g., LTA_P and LTA_P) within the main code then run the phase picking process (bash Locator -p). Before going to the next step, make sure the picks are fine.

After doing so, you can start the locating process by issuing "bash Locator -l". This command does both picking and locating procedures. If P arrivals are already determined in advance (e.g., manually added to the original data or using -p flag), one can set the Autopick parameter to "False" to force the program to skip the picking process and read the arrivals from the original SAC files. In the end, there will be a .ps file within the Input/ directory.

This code is only tested for local events.

Please feel free to contact me in case of an error of any kind.

