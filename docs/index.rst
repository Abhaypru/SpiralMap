.. You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SpiralMap
===========================================

We present a Python library of the Milky Way's major spiral arm models and maps. Over the years several independent studies conducted across wavelengths have revealed rich spiral structure in the Galaxy. Here, we have tried to compile the major models and maps in a user friendly manner. 
Most users are interested in simply extracting the trace or overplotting the spiral arms on another plot of interest, for example while comparing substructure in the velocity field to the location of spiral arms. 
To this end, with `SpiralMap` one can:

+ Access 8 independent spiral arm models from literature. 
+ Extract the trace of individual or all spiral arms from a particular model.
+ Directly overplot spiral arms with choice of Cartesian or Polar coordinates, and in Heliocentric or Galactocentric frames.



.. figure:: ../src/SpiralMap/movie_.gif

   A gallery of the various models included in this version, in this case in polar projection and in Galactocentric coordinates with 
   the locations of the Sun and the Galactic center (star) marked.
   
A list of the available models is  :doc:`here </models_available>`.
   

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

