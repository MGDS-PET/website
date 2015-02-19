Early Rubber Vibrotactile Devices
==================================================

:slug: earlyRubber
:url: pages/devices/early/earlyRubber
:save_as: pages/devices/early/earlyRubber.html

.. image:: /images/devices/early/rubber/P1130386.RW2.jpg
	:alt: early rubber device 1
	:width: 25%

.. image:: /images/devices/early/rubber/P1130396.RW2.jpg
	:alt: early rubber device 2
	:width: 25%

.. contents::


Design and research questions
--------------------------------------------------

- How do simple non-intrusive vibrating patterns feel on the wrist?
- Are these wrist sensations enjoyable to the touch?
- Can the wrist distinguish between simple patterns?
- Can symbolic information (e.g textual messages) be transmitted using this means?


Description
--------------------------------------------------

These are devices designed early in the project to test ideas for wrist-wearables in which vibrating motors and LED lights provide non-intrusive notifications. The device was built to test how 

Components are simple and exposed. These devices are controlled externally by an Arduino board. 

Vibrating motors on the band are programmed to play with various vibrational patterns and at various intensities. Composition of these patterns using MIDI data is also possible. 

It is possible to create patterns using music composition techniques and standard musical notation (in musical notation applications such as `Lilypond <http://www.lilypond.org/>`_, which exports MIDI data), Using this technique it is possible to compose music control data using standard musical notation, which the Arduino board can use to recreate these patterns. 

Components
--------------------------------------------------

- Rubber band (cut and fashioned from recycled conveyor-belt material)
- 8 vibrating motors (their original use is as vibrators for mobile phones)
- 7 LED lights
- Arduino Mega 2560 microcontroller board


Use Cases
--------------------------------------------------

- Compose a simple, sequential rhythmic pattern 
	Incorporating vibrating motors and LED lights. These patterns are designed on a computer and then loaded onto the microcontroller board with a USB cable.

- Load this pattern onto the attached Arduino controller board
	The band is controlled using an external board. These boards come in various sizes and therefore can be made quite small. The computational demands placed on the board by this device is minimal. 

Discussion
--------------------------------------------------





