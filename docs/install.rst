Installation and Quickstart
===========================

The **SpiralMap** package is available through  `PyPI <https://test.pypi.org/project/SpiralMap/>`_and `GitHub <https://github.com/Abhaypru/SpiralMap>`_ .
To install SpiralMap with pip from PyPI, run:

.. code-block:: bash

   pip install SpiralMap

To install SpiralMap directly from GitHub, run:

.. code-block:: bash

   pip install git+https://github.com/Abhaypru/SpiralMap.git

Alternatively, clone the repository and install locally:

.. code-block:: bash

   git clone https://github.com/Abhaypru/SpiralMap.git
   cd SpiralMap
   python -m pip install .

(Optional) Create a virtual environment before installation to avoid dependency conflicts:


Quickstart: Plotting Spiral Arm Models
--------------------------------------

Here's a minimal example that demonstrates how to load and visualize a spiral arm model using **SpiralMap**:

.. code-block:: python

   import SpiralMap as sp
   import matplotlib.pyplot as plt
   import os
   Rsun=8.277
   spirals = sp.main_(Rsun=Rsun,print_=False)

   # Load a specific spiral arm model (e.g., 'Taylor_Cordes_1992')
   
   use_model = 'Taylor_Cordes_1992'

   # Plot in Galactocentric coordinates
   spirals = sp.main_(xsun=xsun)
   plotattrs = {'plot':True,'coordsys':'GC','markersize':15,'polargrid':True}
   spirals.readout(plotattrs,model=use_model,arm='all')  

This will generate a 3d projection of the Milky Way spiral arms based on the selected model.

.. image:: src/SpiralMap/figdir_primer/map_0png.png
   :width: 600

