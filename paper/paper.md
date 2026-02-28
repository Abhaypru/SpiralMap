---
title: "SpiralMap: A Python library of the Milky Way's spiral arms"
tags:
  - galactic structure
  - Python
  - Astronomy
authors:
  - name: Abhay Kumar Prusty 
    orcid: 0009-0009-6412-4460
    affiliation: 1
  - name: Shourya Khanna 
    orcid: 0000-0002-2604-4277
    affiliation: 2 
affiliations:
 - name: Indian Institute of Science Education and Research Kolkata, Mohanpur 741246, West Bengal, India
   index: 1
 - name: INAF - Osservatorio Astrofisico di Torino, via Osservatorio 20, 10025 Pino Torinese (TO), Italy
   index: 2 
date: 11 June 2025
bibliography: paper.bib
---

# Summary
Mapping the structure of the Galaxy has been an ongoing endeavour for several decades, thanks to which we have come to piece together the components it is made up of such as the discs/bulge/halo and so on [@jbhreview2016]. 
Of particular interest is also the signature of non-axisymmetry in the disc, principally present in the form of the central Galactic bar, the warp, and various spiral like features fanning across a large portion of the disc.
 Over the years, various groups have surveyed the Galaxy across wavelengths (Radio to optical) and have deduced the rich variety of spiral structure present in the disc. 
While some of the papers in literature provide machine readable data to trace out the spiral arms in their model, often this can be a cumbersome exercise for a user simply interested in extracting the coordinates and/or overplotting the spiral arms on another plot of interest, such as while comparing the locations of the arms to features in the velocity field [@Khanna:2023; @Poggio:2024]. 
With `SpiralMap` we present a library of the major spiral arm models (and maps) of the Galaxy. 

# Statement of need
The `SpiralMap` package is written in `Python`, and allows the user to both extract the 2D trace and overplot the spiral arms in cartesian/polar coordinates in both Heliocentric (HC) and Galactocentric (GC) frames.
A summary of the models currently included is provided in the Table below, where we have tried to include models from across the electromagnetic spectrum, and based on various tracers (gas/stars etc.). 
Other models can easily be included on request. In the near future, we anticipate the availability of 3D spiral arm traces for the Galaxy in literature which can also be included in `SpiralMap`.

| Model  | Description   |
|----------|------------------------------------|
| `Taylor_Cordes_1992`  | Model based on HII [@Taylor:1993].  |
| `Vallee_1995`  | Model based on Galactic magnetic field/Dust/stars [@Vallee:1995].  |
| `Drimmel_NIR_2000`  | Model based on Galactic plane emission in the NIR [@drimmel2000].  |
| `Levine_2006`  | Model based on HI (21 cm) [@Levine:2006].  |
| `Hou_Han_2014`  | Logarithmic spiral model based on HII/ GMC/methanol Maser observations [@Hou:2014].  |
| `Reid_2019`  | Model based on parallax measurements of MASERS [@Reid:2019].  |
| `Poggio_2021`  | Map based on Upper Main sequence stars [@Poggio:2021].  |
| `Gaia_2022`  | Map based on OB stars [@gaiacollab22].  |
| `Drimmel_Ceph_2024`  | Model based on Cepheid variables  [@Drimmel:2024].  |

A few example plots that can be generated using the package are included below. For more details, we point to the following links:
a) Documentation: [`readthedocs`](https://spiralmap.readthedocs.io/en/latest/), b) Demonstration: [`Jupyter notebook`](https://github.com/Abhaypru/SpiralMap/blob/main/demo_spiralmap.ipynb), and c) [`Github repository`](https://github.com/Abhaypru/SpiralMap).

![Cartesian projection of the `Drimmel_Ceph_2024` model shown for a particular arm (`Sag-Car`). We show this arm in HC (a), HC with a polar grid in the background (b), and in GC frame with a polar grid in the background (c).\label{single_arm_single_model}](figures/single_arm_single_model.png)


![Cartesian projections of multiple models plotted together with a polar grid in the background. We show the `Taylor_Cordes_1992` & `Poggio_2021` models in HC (a) and GC (b) frames, and similarly, the `Drimmel_NIR_2000` & `Poggio_2021` models in HC (c) and GC (d) frames.\label{multiple_models_cartesian}](figures/multiple_models_cartesian.png)

![Polar projections of multiple models plotted together. We show the `Taylor_Cordes_1992` & `Poggio_2021` models in HC (a) and GC (b) frames, and similarly the tiple models plotted together with a polar grid in the background and similarly, the `Drimmel_NIR_2000` & `Poggio_2021` models in HC (c) and GC (d) frames.\label{multiple_models_polar}](figures/multiple_models_polar.png)

# State of the field
To the best of our knowledge, there is no other publicly available package providing similar tools to the community. We acknowledge the individual surveys and papers that have mapped out the spirality of the Milky Way, however
we have also observed that it is quite easy to miss out on historically derived models, likely because there is no standard way of publishing a spiral arm model. Some papers provide datafiles, others provide large tables 
which still require individual users to extract the data, and doing so for several papers can be a cumbersome exercise. With our package having all the major models under one umbrella interface allows for an easier comparison 
between the various tracers (stars, gas, etc) of such non-axisymmetry, and also facilitates fair visibility of the various efforts carried out over decades.
Indeed with `SpiralMap` we intend to address this gap, by providing a user-friendly interface encompassing all 
the major spiral arm models and maps currently offering traces in 2D, and very soon to extend this to 3D. 


# Software Design

The main motivation behind `SpiralMap` is to provide a Python3 based user-friendly, object-oriented API that allows users to generate spatial traces of the various Spiral arm maps and models of the Milky Way, available in literature. 
The package relies on a minimal set of dependencies, including on well maintained community tools such as Astropy. 
While most of the models currently included in the package are analytical, i.e. the code generates the spiral trace for the user, in a few select cases these are read from 
pre-generated files, which are provided in user-friendly formats such as `pickle` or `FITS` files. The individual spiral arm models are all available in literature but in disparate forms (datafiles, analytical descriptions, etc). 
Our aim here is to provide the user with a one-stop python class where the application of the various spiral models can be homogenised, in particular accessing both heliocentric and galactocentric coordinates of the spiral tracers,
the ability to quickly plot both cartesian or polar projections, or to select which (or all) spiral arms to plot for a particular model etc. Additionally, the user still has access to the raw forms of the spiral models as were presented in 
literature, except here in a machine readable form. 


# Research Impact Statement
`SpiralMap` has been available to the community since June 2025. `PyPI` stats shows that the package has been downloaded about 1500 times since release, averaging about 200 downloads per month. 
The supporting document on the `arXiv` has also been cited by two peer reviewed papers (ex: Trentin et al. 2025) as of Feb 2026, with at least 3 other papers in prep that have requested particular model updates.
To this end, we pushed a new version in February 2026 with additional spiral arm models appended to the package, and expect another update in March 2026 which will include the first 3D spiral arm model. 


# AI usage disclosure

No generative AI tools were used in the development of this software, writing of this manuscript, or the preparation of supporting materials.

# Example Scientific application
As an example of a science case, we reproduce figures from @khanna2024 (hereafter K24) where `SpiralMap` was used. 
In particular, K24 constructed a model for the stellar density distribution in Red Clump stars in the Milky Way, and then compared the residuals of their best-fit models
 with the locations of non-axisymmetric structures such as spiral arms. The figures below show two of their residual plots overlaid with spiral models
 ( `Drimmel_NIR_2000`, `Drimmel_Ceph_2024`, & `Reid_2019`) using `SpiralMap`.


![An example science case where `SpiralMap` can be useful. Here we show two figures reproduced from K24 (with permission), comparing the residuals between a best-fit model and data, and the locations of spiral arm models in the Milky Way. This figure shows the `Drimmel_NIR_2000`, `Drimmel_Ceph_2024`, & `Reid_2019` overplotted together, shown in polar projection.\label{example_science_a}](figures/residuals_polar_3.png)


![Same as above, but showing only the `Drimmel_NIR_2000` model.\label{example_science_b}](figures/residuals_polar_0.png)


A very basic example of using `SpiralMap` is shown below, where we access all information about one particular arm ( `Sag-Car`) in one particular model `Drimmel_Ceph_2024`,


	##################################################
	##### Readout a single arm from a single model ###
	##################################################
	import SpiralMap as sp
	from SpiralMap import polar_style
	
	Rsun=8.277
	spirals = sp.main_(Rsun=Rsun)	
	use_model = `Drimmel_Ceph_2024'
	spirals.getinfo(model=use_model)
	plotattrs = {`plot':False}
	spirals.readout(plotattrs,model=use_model,arm=`Sag-Car')    
	
	##################################################
	
More common examples are shown in the accompanying [`Jupyter notebook`](https://github.com/Abhaypru/SpiralMap/blob/main/demo_spiralmap.ipynb). 


# Availability

The source code for ``SpiralMap`` is available on [GitHub](https://github.com/Abhaypru/SpiralMap), and the 
full documentation is hosted on [Read the docs](https://spiralmap.readthedocs.io/en/latest/#api-docs).

# Acknowledgements

SK acknowledges support from the European Union's Horizon 2020 research and innovation program under the GaiaUnlimited project (grant agreement No 101004110). 
We thank Ronald Drimmel \& Eloisa Poggio for useful suggestions.

# References

