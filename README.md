SpiralMap
======

**Spiral arm maps and models of the Milky Way**

Installation
-------------

Install the latest released version using ``pip``:

..  code-block:: python

   import mwdust
   drimmel= mwdust.Drimmel03(filter='2MASS H')
   combined= mwdust.Combined15(filter='2MASS H')
   combined19= mwdust.Combined19(filter='2MASS H')
   sfd= mwdust.SFD(filter='2MASS H')

   pip install SpiralMap

Acknowledging ``SpiralMap``
---------------------------------------

Please cite the accompanying JOSS paper (arxiv link), as well as the individual spiral models used. We provide a BibTex file with the relevant citations in 'datafiles/spiral.bib'.

