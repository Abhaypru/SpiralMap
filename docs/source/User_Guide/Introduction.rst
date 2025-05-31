.. _introduction:

Introduction
============
Description
-----------

Understanding the structure of the Milky Way has been a central focus of Galactic astronomy for decades,
leading to a detailed picture of its main components—including the disc, bulge, and halo \citep{jbhreview2016}.
Among these, the non-axisymmetric features of the disc, such as the central Galactic bar and the intricate spiral arms,
are of particular interest. Extensive surveys across the electromagnetic spectrum, from radio to optical, have
revealed a rich diversity of spiral arm structures mapped by different tracers and methods.
Despite this progress, accessing and utilizing published spiral arm models can be challenging. While some
studies provide machine-readable tables, extracting coordinates or visualizing spiral arms in a user’s preferred 
frame often requires significant effort and technical know-how.
The \spiralmap{} package addresses this gap by offering a unified and user-friendly interface to the major spiral 
arm models available in the literature. It allows users to extract cartesian coordinates and overplot spiral arms
in commonly used coordinate systems—including heliocentric, galactocentric, and polar frames—with minimal setup.
A summary of the models currently included in the package is provided in \autoref{tab:modsummary}. While this list
is not exhaustive, it encompasses the principal approaches and tracers that underpin our present understanding of 
the Milky Way’s spiral structure. We welcome suggestions for additional models and encourage community contributions.
The following sections provide a walkthrough of \spiralmap{}’s features and usage. If you prefer, you can jump
directly to the quickstart guide in \autoref{sec:quickstart}.