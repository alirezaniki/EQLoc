from pyrocko import cake
import numpy as num
km = 1000.

# Load builtin 'prem-no-ocean' model ('.m': medium resolution variant)
model = cake.load_model('/home/alireza/Desktop/Grid_Search/Velmodel.tvel')

# Source depth [m].
source_depth = 10 * km

# Distances as a numpy array [deg].
distances = num.linspace(295.97,295.97,1) * km * cake.m2d

# Define the phase to use.
Phase = cake.PhaseDef('P')

# calculate distances and arrivals and print them:
for arrival in model.arrivals(distances, phases=Phase, zstart=source_depth):
    print '%13g %13g' % (arrival.x*cake.d2m/km, arrival.t)

    
    
