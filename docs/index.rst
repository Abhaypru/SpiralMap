.. You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SpiralMap
===========================================

`SpiralMap` is a Python library of the Milky Way's major spiral arm models and maps. 

Mapping the structure of the Milky Way has been a central pursuit in astronomy for many decades. Through extensive observations, astronomers have developed a detailed understanding of the Galaxy’s main components, including the disc, bulge, and halo. Features that break the Galaxy's symmetry—such as the central bar and sweeping spiral arms—are of particular interest.

Numerous surveys, spanning radio to optical wavelengths, have revealed the rich and varied spiral structure of the Milky Way. However, even when machine-readable data for spiral arm models are available, extracting coordinates or overlaying spiral arms on custom plots can be a challenge for users.

The ``spiralmap`` package addresses these challenges by providing a convenient and unified interface to major spiral arm models published in the literature. With ``spiralmap``, users can easily extract cartesian coordinates and overplot spiral arms in commonly used coordinate frames, including heliocentric, galactocentric, and polar projections.



Features
--------

+ Access 8 independent spiral arm models from literature. 
+ Extract the trace of individual or all spiral arms from a particular model.
+ Directly overplot spiral arms with choice of Cartesian or Polar coordinates, and in Heliocentric or Galactocentric frames.


Acknowledgements
----------------


If you make use of `SpiralMap`, please cite the accompanying paper (submitted to JOSS). Additionally, please also cite the individual spiral arm model/map used. 
Relevant references are provided in BibTeX form in the :doc:`How to cite </citation>` section.


Contributors
------------

Abhay Kumar Prusty (IISER Kolkata) &
Shourya Khanna (INAF-Torino)


.. toctree::
   :maxdepth: 1
   :caption: Contents:

   introduction
   models_available
   install
   walkthrough
   citation



.. toctree::
   :maxdepth: 1
   :caption: Tutorials and illustrated examples:

   demo_spiralmap.ipynb

