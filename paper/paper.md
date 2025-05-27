---
title: 'dfitspy: a dfits|fitsort implementation in python'
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
 - name: IISER Kolkata, India
   index: 1
 - name: INAF Torino, Italy
   index: 2 
date: 28 May 2025
bibliography: paper.bib
---

# Summary
The Milky Way is known 


# dfitspy as a Python module
To be used as a Python module, ``dfitspy`` must be imported. Then a set of command have to be used in order to produce the final list of filenames/keywords/values. In short, three main commands must be used:

``+----+----------------------------+---------------------------+``
``|    | Available models & maps:   | Description               |``
``|----+----------------------------+---------------------------|``
``|  0 | Taylor_Cordes_1992         | HII                       |``
``|  1 | Drimmel_NIR_2000           | NIR emission              |``
``|  2 | Levine_2006                | HI                        |``
``|  3 | Hou_Han_2014               | HII/GMC/Masers            |``
``|  4 | Reid_2019                  | MASER parallax            |``
``|  5 | Poggio_cont_2021           | Upper main sequence (map) |``
``|  6 | GaiaPVP_cont_2022          | OB stars (map)            |``
``|  7 | Drimmel_Ceph_2024          | Cepheids                  |``
``+----+----------------------------+---------------------------+``


And the list of keywords must be prepared, and eventually the grepping values:\
``listkeys = ['author', 'number', 'type']``\
``grepping = ['2dspec']``

Finally, we can fitsort the files and eventually grep.\
``fitsortgrep = dfitspy.dfitsort(listfiles, listkeys, grepping)``

The final output is stored as a dictionnary of files for which each keywords/values is given. It can also be displayed in the same way as for the terminal output (see above).

# Availability

``dfitspy`` is a GPL licensed software and the source code is available at https://github.com/astrom-tom/dfitspy. The full documentation is available at https://astrom-tom.github.io/dfitspy/build/html/index.html .

# Acknowledgements

The author would like to thank the Journal of Open Source Software to give the opportunity to researchers to publish their softwares and to the referee of this paper for helpful comments.

# References

