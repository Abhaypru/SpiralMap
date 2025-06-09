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
date: 02 June 2025
bibliography: paper.bib
---


# Statement of need
Mapping the structure of the Galaxy has been an ongoing endeavour for several decades, thanks to which we have come to piece together the components it is made up of such as the discs/bulge/halo and so on [@jbhreview2016]. 
Of particular interest is also the signature of non-axisymmetry in the disc, principally present in the form of the central Galactic bar, the warp, and various spiral like features fanning across a large portion of the disc.
 Over the years, various groups have surveyed the Galaxy across wavelengths (Radio to optical) and have deduced the rich variety of spiral structure present in the disc. 
While some of the papers in literature provide machine readable data to trace out the spiral arms in their model, often this can be a cumbersome exercise for a user simply interested in extracting the coordinates and/or overplotting the spiral arms on another plot of interest, such as while comparing the locations of the arms to features in the velocity field [@Khanna:2023; @Poggio:2024]. 


With `SpiralMap` we present a library of the major spiral arm models (and maps) of the Galaxy. 
The package is written in `Python`, and allows the user to both extract the 2D trace and overplot the spiral arms in cartesian/polar coordinates in both Heliocentric (HC) and Galactocentric (GC) frames.
A summary of the models currently included is provided in the Table below, where we have tried to include models from across the electromagnetic spectrum, and based on various tracers (gas/stars etc.). 
Other models can easily be included on request. In the near future, we anticipate the availability of 3D spiral arm traces for the Galaxy in literature which can also be included in `SpiralMap`.

| Model  | Description   |
|----------|------------------------------------|
| `Taylor_Cordes_1992`  | Model based on HII [@Taylor:1993].  |
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



# Availability

The source code for ``SpiralMap`` is available on [GitHub](https://github.com/Abhaypru/SpiralMap), and the 
full documentation is hosted on [Read the docs](https://spiralmap.readthedocs.io/en/latest/#api-docs).

# Acknowledgements

SK acknowledges support from the European Union's Horizon 2020 research and innovation program under the GaiaUnlimited project (grant agreement No 101004110). 
We thank Ronald Drimmel \& Eloisa Poggio for useful suggestions.

# References

