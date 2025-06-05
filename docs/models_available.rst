
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

   

Taylor_Cordes_1992
------------------
This class implements the model from :cite:`Taylor_Cordes_1992` which is based on free-electron density distributions in the Milky Way. 
This formulation uses empirical fits to pulsar dispersion measures to delineate the spiral arms, and we have utilized the data presented in Table 1 of :cite:`Taylor_Cordes_1992`
 to generate the corresponding plots.
