
Available Spiral Arm Models
===========================

The following table provides a summary of the spiral arm models included in **SpiralMap**.

+------------------------+--------------------------------------------------------------------------+
| **Model**              | **Description**                                                          |
+========================+==========================================================================+
| Taylor_Cordes_1992     | Model based on HII regions                                               |
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



`Taylor_Cordes_1992`
---------------------
	* Class implementing the model from `Taylor & Cordes et al. 1993 <https://ui.adsabs.harvard.edu/abs/1993ApJ...411..674T/abstract>`_ 
	  which is based on radio and optical observations of H II regions. 	  
	* We use the model parameters presented in their Table 1.	
	* There are four arms in this model: Arm1, Arm2, Arm3, Arm4.

`Drimmel_NIR_2000`
-----------------
* Class implementing the model from `Drimmel 2000 <https://iopscience.iop.org/article/10.1086/321556>`_, which is based on Galactic plane emission profiles in the K band using COBE data.
 
* There are two arms (1_arm, 2_arm) and two inter-arm regions (3_interarm,4_interarm) in this model. 
* Model publicly available 

Levine_2006
-----------
This class adopts a logarithmic spiral framework as described in `Levine et al. 2006 <https://www.science.org/doi/10.1126/science.1128455>`_
based on HI observations. This classical approach robustly represents the four major spiral arms, providing a structural framework anchored in the neutral hydrogen distribution.
Model taken from their Table 1.

Hou_Han_2014 
-------------
This class is built upon the polynomial-logarithmic formulation introduced by `Hou et al. 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...569A.125H/abstract>`_. 
Its flexible parameterization allows for a detailed reconstruction of the spiral structure, making it particularly useful for studies of Galactic dynamics and morphology. 
Model taken from 

Reid_2019
---------
This class implements `Reid et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019ApJ...885..131R/abstract>`_ .  This model leverages high-precision maser parallax measurements.
Model taken from their Table 2.

Poggio_cont_2021
-------------
This class is based on the EDR3 map UMS stars by `Poggio et al. 2021 <https://www.aanda.org/articles/aa/abs/2021/07/aa40687-21/aa40687-21.html>`_. 
Data is included in the package with their permission.

GaiaPVP_cont_2022
-------------
This class is based on the map of OB stars `Gaia collaboration et al. 2022 <https://www.aanda.org/articles/aa/full_html/2023/06/aa43797-22/aa43797-22.html>`_. 
Data is included in the package with their permission.


Drimmel_Ceph_2024
-------------
This class implements the model by `Drimmel et al. 2024 <https://ui.adsabs.harvard.edu/abs/2024arXiv240609127D/abstract>`_. It is based on Cepheids.
Model taken from their Table 1 and made available as a userfriendly pickle file with their permission.
