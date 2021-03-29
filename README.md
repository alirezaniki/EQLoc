EQLoc (V 1.2.1)
---------

An automated P-phase picking procedure and a grid-search/inversion-based method to locate (local) events. 

In the current version, the normalized data and their corresponding sta/lta diagram are used to enhance the phase picking procedure.


Requirements
------------

1- Sac

2- GMT (Version 5.x)

3- Pyrocko (on python3)

4- Obspy (on python3)


Note:
-----

At your first test, run "bash Locate -h" to get instructed.

Supply the Input/ directory with vertical components of different stations.

Two files are required by this program; (1) station info file (see the example file stations.dat; do not change the file name), and (2) velocity model (see the example file; set the file name to VM_Name parameter). 

In this version, we use the STA/LTA diagram instead of the common STA/LTA sliding window to accelerate and simplify the picking procedure. The results from this process will be stored into the sac files to be used in location procedure. Adjuct the related parameters (e.g., LTA_P and LTA_P) within the main code then run the phase picking process (bash Locator -p).

After doing so, you can start the locating process by issuing "bash Locator -l". This command does both picking and locating procedures. If P arrivals are already determined in advance (e.g., manually added to the original data headers), one can set the Autopick parameter to "False" to force the program skip the picking process and read the arrivals from the original SAC files.

This code is only tested for local events.

Please feel free to contact me in case of an error of any kind.

