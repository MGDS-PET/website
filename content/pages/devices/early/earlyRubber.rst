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


Description
--------------------------------------------------

These simple and rather primitive devices were designed early in the project to test ideas for wrist-wearables in which vibrating motors and LED lights create interesting patterns of light and vibrations, and might provide useful non-intrusive notifications. Components are simple and exposed. These devices are controlled externally by an Arduino board. Vibrating motors on the band are programmed to play various vibrational patterns at various intensities. 

One interesting offshoot of this work is that we discovered that it is possible to create patterns using music composition techniques and standard musical notation (for example, the musical notation application `Lilypond <http://www.lilypond.org/>`_ exports MIDI data which can be used by the device). Using this technique it is possible to compose music control data using standard musical notation, which the Arduino board uses to recreate rhythmic patterns. 


Hardware components used
--------------------------------------------------

- Rubber band (cut and fashioned from recycled conveyor-belt material)
- 8 vibrating motors (their original use is as vibrators for mobile phones)
- 7 LED lights
- Arduino Mega 2560 microcontroller board (power for device comes via this board by USB cable to a computer)
- wiring that connects components


Motivation for building devices
--------------------------------------------------

For application to transmedia games, the idea arose early in the project that players would benefit from non-intrusive notifications that vibrating components against the skin provide. This early band explored how simple vibrating patterns feel against the skin and wrist and whether an array of vibrating components might have the potential of conveying information. 

We were motivated to build these devices to explore the following research questions:

- How do simple non-intrusive vibrating patterns feel on the wrist?
- Are these wrist sensations enjoyable to the touch?
- Can the wrist distinguish between simple patterns?
- Does an array of simple vibrating patterns create a richer sensation, or does it become unpleasant?
- Can symbolic information (e.g textual messages) be represented using vibrating patterns?
- Can directional information (e.g 'go the left') be transmitted using this means?


Use Cases / User stories
--------------------------------------------------

User stories pattern: "As a <role>, I want to <goal/desire> so that <benefit occur>"

Actor: game player, child aged 7-12
..................................................

#. Wear the wrist device
	"As a game player I want to wear the device so I can feel the device's vibrations against my wrist"

#. Recognize a vibrating pattern to help play the game more effectively
	"As a game player I want the device to provide me guidance to play the game better"
	Game designer will create vibrational patterns embedded in the game's content, cued to arise at appropriate moments during the game.


Actor: content creator
..................................................

#. Compose a simple, sequential rhythmic pattern
	"As a content creator I want to be able to create interesting vibrating patterns that could in various narrative situations"
	Incorporate vibrating motors and LED lights. These patterns are designed on a computer and then loaded onto the microcontroller board with a USB cable.

#. Load composed pattern from computer onto the attached Arduino controller board
	""
	The band is controlled using an external board. These boards come in various sizes and can be made quite small. The computational demands placed on the board by this device is minimal. 


Discussion and results
--------------------------------------------------

Vibrating patterns on the wrist
..................................................

Using MIDI to compose patterns
..................................................







