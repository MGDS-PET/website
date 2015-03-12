3D Printed Bands
==================================================


:slug: 3DprintedBands
:url: pages/components/bands/3DprintedBands
:save_as: pages/components/bands/3DprintedBands.html

.. image:: /images/components/bands/3Dprinted/P1130870.jpg
	:alt: 3D printed band 1
	:width: 25%

.. image:: /images/components/bands/3Dprinted/P1130624.jpg
	:alt: 3D printed band 2
	:width: 25%

Description
--------------------------------------------------

3D printed bands are made using a MakerBot_ Replicator 2 3D printer. Initially, these designed with radial symmetry with channels to accommodate wiring between electronic components. 

Components
--------------------------------------------------

- 3D printed PLA hard plastic material
- Elastic thread

Discussion
--------------------------------------------------

These bands were designed using the open-source CAD software OpenSCAD_. This software is very useful in designing fully parameterized 3D CAD models. For simple geometric forms, such as these bands, this approach worked well. For more complex, or less geometric designs that use fewer simple shapes, OpenSCAD is less appropriate. 

The advantages of a parameterized model is the ease at which it can 'tweaked' after the fact. Adjustments of fractions of a millimeter are common in band design iterations. Such tweaks can make a big difference in accommodating the size of components. Fully parameterized models make such adjustments trivial. However, more effort may be required at the front end for such CAD models.

.. _MakerBot: http://www.makerbot.com
.. _OpenSCAD: http://www.openscad.org
