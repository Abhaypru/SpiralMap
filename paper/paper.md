---
title: 'SpiralMap: A Python library for the spiral arms of the Milky Way'
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


# SpiralMap as a Python module
To be used as a Python module, 


![Left: posterior distribution of an event in log10(timescale)-log10(parallax) space, overlaid on 'star', 'white dwarf', 'neutron star' and 'black hole' contours. Right: bars showing probabilities of that event belonging to each of the lens populations.\label{spiral}](spiral.png)

\begin{table}
\caption{Basic summary of the spiral arm models included in \textit{SpiralMap} . \label{tab:modsummary}}
\begin{tabular}{lll}
\hline
\hline
Model	& Reference	& Description \\
\hline
taylorcordes & \cite{Taylor:1993} &  Based on free-electron density distributions fitted to pulsar dispersion measures to trace spiral arms. \\ 
drimmelnir & \cite{drimmel2000} & Based on Galactic plane emission in the NIR. \\ 
levine &\cite{Levine:2006} & Based on HI (21 cm) survey line data to trace the gaseous structure of the Milky Way spiral arms. \\
houhan & \cite{Hou:2014} &  Adopts a logarithmic spiral framework , based on HII/ GMC/methanol Maser observations.  \\ 
reid & \cite{Reid:2019} 
 & Based on high-precision parallax measurements of MASERS.  \\ 
poggio & \cite{Poggio:2021} & \textit{Gaia}-based model tracing stellar over-densities in the Galactic disk. \\ 
Gaia collaboration &  & \textit{Gaia}-based model tracing stellar over-densities in the Galactic disk. \\ 
Drimmel\_ceph\_2024 & \cite{Drimmel:2024} & Uses Cepheid variables to model the young stellar spiral structure. \\ 
\hline
\end{tabular}
\end{table}
%============================ 


# Availability

``SpiralMap`` is a GPL licensed software and the source code is available at https://github.com/Abhaypru/SpiralMap. The full documentation is available at https://astrom-tom.github.io/dfitspy/build/html/index.html .

# Acknowledgements

SK acknowledges support from the European Union's Horizon 2020 research and innovation program under the GaiaUnlimited project (grant agreement No 101004110).


# References

