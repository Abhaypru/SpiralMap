Walkthrough
===========

Import Packages
---------------

To get started, import the main ``SpiralMap`` package and set the Galactocentric position of the Sun.  
Here, we adopt the value from *Gravity Collaboration (2021)*.

.. code-block:: python

    # Import main & set Rsun
    from SpiralMap import *
    import SpiralMap as sp
    import matplotlib as mpl

    Rsun = 8.277

This automatically imports the following useful packages via the internal module ``dtools.py``:

.. code-block:: python

    # Packages loaded internally in dtools.py
    import os, sys
    import numpy as np
    from astropy.table import Table
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.interpolate import CubicSpline

Exploring Spiral Models
------------------------

Next, initialize the main class by passing in the Galactocentric radius of the Sun (``Rsun``).  
This will also print out the list of spiral models currently available in the package.

.. code-block:: python

    In [3]: spirals = sp.main_(Rsun=Rsun)

    try self.getinfo(model) for more details
    +----+----------------------------+---------------------------+
    |    | Available models & maps:   | Description               |
    |----+----------------------------+---------------------------|
    |  0 | Taylor_Cordes_1992         | H II                      |
    |  1 | Drimmel_NIR_2000           | NIR emission              |
    |  2 | Levine_2006                | H I                       |
    |  3 | Hou_Han_2014               | Hou_Han_2014              |
    |  4 | Reid_2019                  | MASER parallax            |
    |  5 | Poggio_cont_2021           | Upper main sequence (map) |
    |  6 | GaiaPVP_cont_2022          | OB stars (map)            |
    |  7 | Drimmel_Ceph_2024          | Cepheids                  |
    +----+----------------------------+---------------------------+

You can also extract the same information explicitly using:

.. code-block:: python

    In [3]: spirals.getinfo()

    try self.getinfo(model) for more details
    +------------------------+--------------------------------------------------------------------------+
    | **Model**              | **Description**                                                          |
    +========================+==========================================================================+
    | Taylor_Cordes_1992     | Model based on HII regions .                         |
    +------------------------+--------------------------------------------------------------------------+
    | Drimmel_NIR_2000       | Based on Galactic plane emission in NIR .             |
    +------------------------+--------------------------------------------------------------------------+
    | Levine_2006            | Based on HI (21 cm) data .                             |
    +------------------------+--------------------------------------------------------------------------+
    | Hou_Han_2014           | Logarithmic spiral using HII/GMC/Maser data .             |
    +------------------------+--------------------------------------------------------------------------+
    | Reid_2019              | MASER parallax model .                                   |
    +------------------------+--------------------------------------------------------------------------+
    | Poggio_cont_2021       | Map based on Upper Main Sequence stars .               |
    +------------------------+--------------------------------------------------------------------------+
    | GaiaPVP_cont_2022      | OB star map from Gaia Collaboration .              |
    +------------------------+--------------------------------------------------------------------------+
    | Drimmel_Ceph_2024      | Based on Cepheid variables .                          |
    +------------------------+--------------------------------------------------------------------------+


To get detailed information about a specific model — such as number of arms, their names, and associated colors — you can pass the model name to ``getinfo()``.  
For example, to get info about the ``Drimmel_Ceph_2024`` model:

.. code-block:: python

    In [4]: spirals.getinfo(model='Drimmel_Ceph_2024')

    #####################
    Model = Drimmel_Ceph_2024

    ------------------------
      Arm     list Colour
    0   Scutum     C3
    1  Sag-Car     C0
    2    Orion     C1
    3  Perseus     C2
    ------------------------
