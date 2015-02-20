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

.. sectnum::
	:depth: 3


Description
--------------------------------------------------

These simple and rather primitive devices were built early in the project to test ideas for wrist-wearables in which vibrating motors and LED lights create interesting patterns of light and vibration. A use case for them would be to provide useful non-intrusive notifications for game players. Components are simple and exposed. These devices are controlled externally by an Arduino board. Vibrating motors on the band are programmed to play various vibrational patterns at various intensities. 

One interesting offshoot of this work is that we discovered that it is possible to create patterns using music composition techniques and standard musical notation (for example, the musical notation application `Lilypond <http://www.lilypond.org/>`_ exports MIDI data which can be used by the device). Using this technique it is possible to compose music control data using standard musical notation, which the Arduino board uses to recreate rhythmic patterns. 


Design and research questions
--------------------------------------------------

For application in transmedia games, the idea arose early in the project that players would benefit from non-intrusive notifications that vibrating components placed near, or against, the skin could provide. This early band explored how simple vibrating patterns feel against the skin and wrist and whether arrays of vibrating components could convey symbolic information. 

We were motivated to build these devices in order to explore the following research questions:

- How do vibrating patterns feel on the wrist?
- Does an array of simple vibrating patterns create a richer sensation, or does it become unpleasant?
- Can the wrist distinguish between simple patterns?
- Can directional information (e.g 'go the left') be communicated using this means?
- Can symbolic information (e.g textual messages) be represented using vibrating patterns?


Components
--------------------------------------------------

- Rubber band (cut and fashioned from recycled conveyor-belt material)
- 8 vibrating motors (their original use is as vibrators for mobile phones)
- 7 LED lights
- Arduino Mega 2560 microcontroller board (power for device comes via this board by USB cable to a computer)
- wiring that connects components


User stories / Use cases
--------------------------------------------------

**Pattern used for composing user stories**: "As a **<role>**, I want to **<goal/desire>** so that **<benefit occur>**"

Actor: game player, child aged 7-12
..................................................

#. Wear the wrist device
	"As a game player I want to wear the device so I can feel the device's vibrations against my wrist"

	The player wants a device that fits her wrist and provides sensations, which are novel, pleasant and feel good. This band design, of course, is too primitive to fulfill this purpose since it has an inappropriate-for-children 'Gothic' or industrial style. However, as a platform for testing ideas it was quite successful. 

#. Recognize a vibrating pattern to help play the game more effectively
	"As a game player I want the device to guide me and help me play the game better"

	Game designer will create vibrational patterns embedded in the game's content, cued to arise at appropriate narrative points during the game.

Actor: content creator
..................................................

#. Compose a simple, sequential rhythmic pattern
	"As a content creator I want to be able to create interesting vibrating patterns that could be used in various narrative situations"
	
	Incorporate vibrating motors and LED lights. These patterns are designed on a computer and then loaded onto the microcontroller board with a USB cable.

#. Load composed vibrational pattern from computer so that device can use it
	"As a content creator I want to be able to transmit a composed pattern onto the device"
	
	The wrist device is controlled by an Arduino microcontroller board. These boards, which provide the device's 'brains,' come in various sizes and can be made quite small. The computational demands placed on the microcontroller by the device is minimal. 


Discussion and results
--------------------------------------------------

The feel of vibrating patterns on the wrist
..................................................

Vibrating patterns on the wrist are not uncomfortable, but they do take time to get used to. Some people are sensitive to such stimulation. If you expect the vibration, as for instance in the course of game-play, then it likely is less intrusive than if it is unexpected.


Distinguishing between simple patterns by wrist
..................................................

Pattern can made be rhythmically distinct and people have little difficulty in distinguishing them. This would depend on the length of the pattern and its repetition. The literature states that the tactile resolution is a fraction of aural resolution using the ears.


Directional information using vibrational arrays
..................................................

These devices encircle the wrist. Therefore, their orientation is not fixed on any plane. It is unclear whether they could be used to point in various directions and provide useful orienteering information. 


Representing symbolic information using vibrating patterns
............................................................

Given that the tactile resolution on the wrist is modest if doubtful that such a device could provide useful transmittal of symbolic information without extensive user training. The blind reading braille generally use their finger tips, which are much better able to perceive differences in texture and pattern.


