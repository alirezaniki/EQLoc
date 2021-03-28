EQLoc (V 1.2.1)
---------

An automated P-phase picking procedure and a grid-search/inversion-based method to locate (local) events. 

In the current version, the normalized data and their corresponding sta/lta plot are used to enhance the phase picking procedure.


Requirements
------------

1- Sac

2- GMT (Version 5.x)

3- Pyrocko (on python3)

4- Obspy (on python3)


Note:
-----

At your first test, run "bash Locate -h" to get instructed.

In this version both MSEED (.mseed) and SAC (.sac) data are supported (set the input format with "data_f" parameter). Supply the Input/ directory with vertical components of different stations.

Two files are required by this program; (1) station info file (see the example file stations.dat; do not change the file name), and (2) velocity model (see the example file; set the file name to VM_Name parameter). 

At first, set a large and small value for P_WTh (e.g., 10-15) and Wth_I (e.g., 0.5-1.0) parameters, respectively, and use the program's phase-picking module (-p flag) to get an idea of optimal value for STA/LTA parameters. Afterward, you can adjust these parameters more wisely and move forward to the next step. The results from this process will be stored into the sac files to be used in location procedure.

After doing so, you can start the locating process by issuing "bash Locator -l". This command does both picking and locating procedures. If P arrivals are already determined in advance (e.g., manually added to the original data headers), one can set the Autopick parameter to "False" to make the program skip the picking process and read the arrivals from the original SAC files (MSEED data is not supported in this case).

This code is only tested for local events.

Please feel free to contact me in case of an error of any kind.

