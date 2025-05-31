Walkthrough
===========

Import Packages
---------------

To get started, import the main `SpiralMap` package and set the Galactocentric position of the Sun.  
Here, we adopt the value from *Gravity Collaboration (2021)*.

.. code-block:: python

    # Import main & set Xsun
    from SpiralMap import *
    import SpiralMap as sp
    import matplotlib as mpl

    Rsun = 8.277

This automatically imports the following useful packages via the internal module `dtools.py`:

.. code-block:: python

    # Packages loaded internally in dtools.py
    import os, sys
    import numpy as np
    from astropy.table import Table
    import pandas as pd
    import matplotlib.pyplot as plt
    from scipy.interpolate import CubicSpline
