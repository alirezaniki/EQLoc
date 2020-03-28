EQLoc
-----

An automated P-phase picking procedure and a grid-search/inversion based method to locate (local) events.

Requirements
------------

1- Sac

2- GMT (Version 5.x)

3- Pyrocko


Note:

- In this release you have the choice on picking procedure to be manual or automated. If you chose the automated one then try to use some (e.g. 5 to 10) good-quality SAC data (vertical components) to avoid any kind of errors in picking procedure. Otherwise, You need to manually pick the first P arrivals in SAC data and save them.

- This code is only tested for local events.

