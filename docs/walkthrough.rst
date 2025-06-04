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

Extracting and plotting data
============================

The main class needs a set of attributes passed in before we can extract or plot data.  
Internally this set is provided by default, and the columns can be viewed by calling the line below.  
A full description of each attribute is provided in :ref:`tab:plotattrs`.

.. code-block:: python

    In [5]: spirals.plotattrs_default
    Out[5]: 
    {'plot': False,
     'markersize': 3,
     'coordsys': 'HC',
     'linewidth': 0.5,
     'linestyle': '-',
     'armcolour': '',
     'markSunGC': True,
     'xmin': '',
     'xmax': '',
     'ymin': '',
     'ymax': '',
     'polarproj': False,
     'polargrid': False,
     'colour_contour': 'black',
     'dataloc': '/Users/shouryapro/Documents/GitHub/SpiralMapping_package/datafiles'}

+----------------+---------------------+---------+---------------------------------------------+
| Column         | Options (type)      | Default | Description                                 |
+================+=====================+=========+=============================================+
| plot           | Boolean             | False   | Whether to generate a plot or just extract data |
+----------------+---------------------+---------+---------------------------------------------+
| markersize     | float               | 3       | Marker size for plotting                    |
+----------------+---------------------+---------+---------------------------------------------+
| coordsys       | ``HC`` / ``GC`` (str)| HC      | Coordinate system: heliocentric or galactocentric |
+----------------+---------------------+---------+---------------------------------------------+
| linewidth      | float               | 0.5     | Line width for plotting arms                |
+----------------+---------------------+---------+---------------------------------------------+
| linestyle      | string              | '-'     | Line style for plotting arms                |
+----------------+---------------------+---------+---------------------------------------------+
| armcolour      | string              | ''      | Color override for arms                      |
+----------------+---------------------+---------+---------------------------------------------+
| markSunGC      | Boolean             | True    | Whether to mark the Sun in GC plots         |
+----------------+---------------------+---------+---------------------------------------------+
| xmin           | string              | ''      | Minimum x-axis limit                         |
+----------------+---------------------+---------+---------------------------------------------+
| xmax           | string              | ''      | Maximum x-axis limit                         |
+----------------+---------------------+---------+---------------------------------------------+
| ymin           | string              | ''      | Minimum y-axis limit                         |
+----------------+---------------------+---------+---------------------------------------------+
| ymax           | string              | ''      | Maximum y-axis limit                         |
+----------------+---------------------+---------+---------------------------------------------+
| polarproj      | Boolean             | False   | Whether to use polar projection (R vs. ϕ)  |
+----------------+---------------------+---------+---------------------------------------------+
| polargrid      | Boolean             | False   | Whether to overplot a polar grid             |
+----------------+---------------------+---------+---------------------------------------------+
| colour_contour | string              | 'black' | Contour line color                           |
+----------------+---------------------+---------+---------------------------------------------+
| dataloc        | string              | os.getcwd()+'/datafiles' | Directory location for data files |
+----------------+---------------------+---------+---------------------------------------------+


The most important attributes to set here are:

- ``plot``: (True or False)
- ``coordsys``: ``HC`` / ``GC`` for heliocentric or galactocentric frames.
- ``polargrid``: To overplot a polar grid on top of the HC or GC frame.
- ``polarproj``: To plot using a polar projection (R vs. ϕ).

Let's say we are interested in the ``Drimmel_Ceph_2024`` model, which has four unique arms that one could extract data for and plot individually. To do so, we use the **readout** function which needs the name of the model and the arm of interest. It also requires a dictionary called **plotattrs**, i.e., the plot attributes. In the example below, we read out the ``Sag-Car`` arm from the ``Drimmel_Ceph_2024`` model without returning a plot:

.. code-block:: python

    # Reading (only) a particular arm from a model
    Rsun = 8.277
    spirals = sp.main_(Rsun=Rsun)
    use_model = 'Drimmel_Ceph_2024'
    spirals.getinfo(model=use_model)
    plotattrs = {'plot': False}
    spirals.readout(plotattrs, model=use_model, arm='Sag-Car')

This generates a dictionary called ``dout`` which contains the cartesian and polar trace of the arm:

.. code-block:: python

    In [16]: list(spirals.dout.keys())
    Out[16]: ['xhc', 'yhc', 'xgc', 'ygc', ....]

To plot this particular arm, we add more arguments to **plotattrs**. In the example below, we plot it in ``HC``, ``GC`` frames, and also in the ``GC`` frame with a polar grid overplotted (see :ref:`fig:single_arm_demo`). For each arm there are preset colours, but the user can also provide a colour in **plotattrs**:

.. code-block:: python

    # Plotting a single arm together in HC, GC, GC (with polar grid) styles
    Rsun = 8.277
    spirals = sp.main_(Rsun=Rsun)
    use_model = 'Drimmel_Ceph_2024'
    use_arm = 'Sag-Car'
    spirals.getinfo(model=use_model)
    
    import matplotlib.pyplot as plt

    plt.close('all')
    fig = plt.figure(figsize=(8, 3))

    fig.add_subplot(1, 3, 1)
    plotattrs = {'plot': True, 'coordsys': 'HC', 'markersize': 15, 'markSunGC': True}
    spirals.readout(plotattrs, model=use_model, arm=use_arm)

    fig.add_subplot(1, 3, 2)
    plotattrs = {'plot': True, 'coordsys': 'HC', 'markersize': 15, 'markSunGC': True, 'polargrid': True}
    spirals.readout(plotattrs, model=use_model, arm=use_arm)

    fig.add_subplot(1, 3, 3)
    plotattrs = {'plot': True, 'coordsys': 'GC', 'markersize': 15, 'markSunGC': True, 'polargrid': True}
    spirals.readout(plotattrs, model=use_model, arm=use_arm)

    fig.suptitle(use_model + ' (' + use_arm + ')')
    fig.tight_layout()
