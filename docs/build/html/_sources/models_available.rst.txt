===========================
Available Spiral Arm Models
===========================

The following table provides a summary of the spiral arm models included in **SpiralMap**.

+------------------------+----------------------------------------------+
| **Model**              | **Description**                              |
+========================+==============================================+
| Taylor_Cordes_1992     | Model based on HII regions                   |
+------------------------+----------------------------------------------+
| Drimmel_NIR_2000       | Based on Galactic plane emission in N        |
+------------------------+----------------------------------------------+
| Levine_2006            | Based on HI (21 cm) data                     |
+------------------------+----------------------------------------------+
| Hou_Han_2014           | Logarithmic spiral using HII/GMC/Maser data  |
+------------------------+----------------------------------------------+
| Reid_2019              | MASER parallax model                         |
+------------------------+----------------------------------------------+
| Poggio_cont_2021       | Map based on Upper Main Sequence stars       |
+------------------------+----------------------------------------------+
| GaiaPVP_cont_2022      | OB star map from Gaia Collaboration          |
+------------------------+----------------------------------------------+
| Drimmel_Ceph_2024      | Based on Cepheid variables                   |
+------------------------+----------------------------------------------+



`Taylor_Cordes_1992`
-----------------
	* Class implementing the model from `Taylor & Cordes et al. 1993 <https://ui.adsabs.harvard.edu/abs/1993ApJ...411..674T/abstract>`_ 
	  which is based on radio and optical observations of H II regions. 	  
	* We use the model parameters presented in their Table 1.	
	* There are four arms in this model (Arm1, Arm2, Arm3, Arm4).

`Drimmel_NIR_2000`
-----------------
	* Class implementing the model from `Drimmel 2000 <https://iopscience.iop.org/article/10.1086/321556>`_, which is based on Galactic plane emission profiles in the K band using COBE data. 
	* Model publicly available. 
	* There are two arms (1_arm, 2_arm) and two inter-arm regions (3_interarm, 4_interarm) in this model. 

`Levine_2006`
-----------
	* Class implementing the logarithmic spiral framework as described in `Levine et al. 2006 <https://www.science.org/doi/10.1126/science.1128455>`_ based on HI observations. 
	* Model taken from their Table 1.
	* There are four arms in this model (Arm1, Arm2, Arm3, Arm4).

`Hou_Han_2014`
-------------
	* Class built upon the polynomial-logarithmic formulation introduced by `Hou et al. 2014 <https://ui.adsabs.harvard.edu/abs/2014A%26A...569A.125H/abstract>`_, based on a combination of 
	  H II, giant molecular clouds, and methanol MASER catalogs. 	
	* Model publicly available.
	* There are six arms in this model (Norma, Scutum-Centaurus, Sagittarius-Carina, Perseus, Local, Outer).

`Reid_2019`
---------
	* Class implementing the model by `Reid et al. 2019 <https://ui.adsabs.harvard.edu/abs/2019ApJ...885..131R/abstract>`_ based on radio astrometry of MASERS. 
	* Model taken from their Table 2.
	* There are seven arms in this model (3-kpc, Norma, Sct-Cen, Sgr-Car, Local, Perseus, Outer).
	
	
`Poggio_cont_2021`
-------------
	* Class used to extract the 2D contour maps of upper-main sequence stars by `Poggio et al. 2021 <https://www.aanda.org/articles/aa/abs/2021/07/aa40687-21/aa40687-21.html>`_.
	  The maps are based on Gaia EDR3 astrometry.
	* Data is available publicly, and also included in the package with their permission.

`GaiaPVP_cont_2022`
-------------
	* Class used to extract the 2D contour maps of OB  stars by `Gaia collaboration et al. 2022 <https://www.aanda.org/articles/aa/full_html/2023/06/aa43797-22/aa43797-22.html>`_.
	  The maps are based on Gaia DR3 astrometry & astrophysical parameters.
	* Data is available publicly, and also included in the package with their permission.


`Drimmel_Ceph_2024`
-------------
	* This class implements the model by `Drimmel et al. 2024 <https://ui.adsabs.harvard.edu/abs/2024arXiv240609127D/abstract>`_. 
	  It is based on a sample of 2857 dynamically young Milky Way Cepheids.
	* Model is publicly available but also included in the package as a userfriendly pickle file, with their permission.
	* There are four arms in this model (Scutum, Sag-Car, Orion, Perseus).
	
