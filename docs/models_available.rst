
Available Spiral Arm Models
===========================

The following table provides a summary of the spiral arm models included in **SpiralMap**.

+------------------------+--------------------------------------------------------------------------+
| **Model**              | **Description**                                                          |
+========================+==========================================================================+
| Taylor_Cordes_1992     | Model based on HII regions :cite:`Taylor_Cordes_1992`.                   |
+------------------------+--------------------------------------------------------------------------+
| Drimmel_NIR_2000       | Based on Galactic plane emission in NIR.                                 |
+------------------------+--------------------------------------------------------------------------+
| Levine_2006            | Based on HI (21 cm) data                                                 |
+------------------------+--------------------------------------------------------------------------+
| Hou_Han_2014           | Logarithmic spiral using HII/GMC/Maser data                              |
+------------------------+--------------------------------------------------------------------------+
| Reid_2019              | MASER parallax model                                                     |
+------------------------+--------------------------------------------------------------------------+
| Poggio_cont_2021       | Map based on Upper Main Sequence stars                                   |
+------------------------+--------------------------------------------------------------------------+
| GaiaPVP_cont_2022      | OB star map from Gaia Collaboration                                      |
+------------------------+--------------------------------------------------------------------------+
| Drimmel_Ceph_2024      | Based on Cepheid variables                                               |
+------------------------+--------------------------------------------------------------------------+


`Castro-Ginard et al. 2023 <https://ui.adsabs.harvard.edu/abs/2023arXiv230317738C/abstract>`_


`Taylor & Cordes et al. 1993 <https://ui.adsabs.harvard.edu/abs/1993ApJ...411..674T/abstract>`_

`Levine et al. 2006 <https://www.science.org/doi/10.1126/science.1128455>`_
`Hou et al. 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...569A.125H/abstract>`_


Taylor_Cordes_1992
------------------
This class implements the model from `Taylor & Cordes et al. 1993 <https://ui.adsabs.harvard.edu/abs/1993ApJ...411..674T/abstract>`_ which is based on free-electron density distributions in the Milky Way. 
This formulation uses empirical fits to pulsar dispersion measures to delineate the spiral arms, and we have utilized the data presented in their Table 1 to generate the corresponding plots.


Drimmel_NIR_2000
----------------


Levine_2006
-----------

This class adopts a logarithmic spiral framework as described in `Levine et al. 2006 <https://www.science.org/doi/10.1126/science.1128455>`_
 based on HI observations. This classical approach robustly represents the four major spiral arms, providing a structural framework anchored in the neutral hydrogen distribution.


Hou_Han_2014 
-------------

This class is built upon the polynomial-logarithmic formulation introduced by `Hou et al. 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...569A.125H/abstract>`_. 
Its flexible parameterization allows for a detailed reconstruction of the spiral structure, making it particularly useful for studies of Galactic dynamics and morphology. 
The resulting plots are consistent with the visualizations presented in `Hou et al. 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...569A.125H/abstract>`_.
