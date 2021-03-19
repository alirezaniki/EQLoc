EQLoc (V 1.2)
---------

An automated P-phase picking procedure and a grid-search/inversion based method to locate (local) events. 

In the current version the envelope function is used to enhance the phase picking procedure.

Requirements
------------

1- Sac

2- GMT (Version 5.x)

3- Pyrocko (on python2)


Note:
-----

In this release you have the choice on picking procedure to be manual or automated. If you chose the automated method then try to use some (e.g. 5 to 10) good-quality SAC data (only vertical components) to avoid any kind of errors in picking procedure. Otherwise, You need to manually pick the first P arrivals in SAC data and store them into the input directory.

This code is only tested for local events.

Please feel free to contact me in case of error of any kinds.

