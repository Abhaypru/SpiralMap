.. SpiralMap documentation master file, created by
   sphinx-quickstart on Mon Jun  9 23:19:51 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to SpiralMap's documentation!
=====================================



We present a Python library of the Milky Way's major spiral arm models and maps. Over the years several independent studies conducted across wavelengths have revealed rich spiral structure in the Galaxy. Here, we have tried to compile the major models and maps in a user friendly manner. 
Most users are interested in simply extracting the trace or overplotting the spiral arms on another plot of interest, for example while comparing substructure in the velocity field to the location of spiral arms. 
To this end, with `SpiralMap` one can:

+ Access 8 independent spiral arm models from literature. List of the available models is :doc:`here </models_available>`.
+ Extract the trace of individual or all spiral arms from a particular model.
+ Directly overplot spiral arms with choice of Cartesian or Polar coordinates, and in Heliocentric or Galactocentric frames.


For a quick demonstration please see the accompanying `Jupyter Notebook <https://github.com/Abhaypru/SpiralMap/blob/main/demo_spiralmap.ipynb>`_. here


.. figure:: ../../src/SpiralMap/movie_.gif

   A gallery of the various models included in this version, in this case in polar projection and in Galactocentric coordinates with 
   the locations of the Sun and the Galactic center (star) marked.
   
   
.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   install
   models_available
   citation  
   api



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
