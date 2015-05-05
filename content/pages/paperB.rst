Paper B: Design Processes with Changing Requirements Containing Cycles
======================================================================

:slug: paperB
:url: pages/paperB
:save_as: pages/paperB.html

Abstract
--------------------------------------------------

Multi-disciplinary design team processes are required to design complex artifacts that span various areas of expertise. It is difficult to arrive at integrated understandings of what the final design should be because of the diversity of the design team. Design team members might have a detailed conception of a sub-section or module on which they're working, but may lack an overall conception of what the whole should be like. Diversity, which is so useful in solving specialized problems in specific domains, makes communication on a unified level difficult. This paper discusses aspects of the question whether unified conceptions of complex devices that span between disciplines are required, or possible, when designing complex devices.

Introduction
--------------------------------------------------

This paper describes research that involves the design of a wrist-wearable device. There were several teams involved in the design, which have specialized expertise in diverse fields such as hardware engineering suitable for wearables, software that runs on this hardware, material and industrial design, game design, user interaction design, marketing research and market positioning for the device. These teams could talk easily amongst themselves in the specialized lexicons and conceptual underpinnings of their various domains. 

Design requirements
--------------------------------------------------

Design requirements are the starting point in most design processes, yet, design processes in which requirements are fixed and well-understood at the beginning are quite rare; design requirements often evolve over time and become part of the design process.  The designed artifact that results can be tested as to how well it satisfies these requirements. Things become a little more complex when the design requirements themselves are dependent on results from a design process. This creates circular dependencies between design requirements and design results. This paper describes the nature of these circular dependencies in the design process of a wearable wrist device intended for wearer interaction within transmedia narratives.


The main requirements for the wearable device are (see also: `Haptic Pattern Representation using Music Technologies` [link_]):

.. _link: Haptic Pattern Representation using Music Technologies, 2014.

- Interpret wrist gestures and recognize overall physical activity of the wearer,
- notify the wearer when crystals and treasure are earned,
- offer vibrotactile clues about where crystals and treasures can be found (in a real physical environment),  
- provide aesthetically attractive and evocative vibe and light displays corresponding to narrative points in a story, and
- create a wristband that is stylistically coherent with the existing transmedia property TimeTremors.

Discussion of these requirements
--------------------------------------------------

Some describe requirements that require technical solutions, such as:

- specialized hardware, such as accelerometers and GPS sensors that sense position and movement,
- specialized software that interprets data from these sensors,
- specialized actuators that notify the wearer in various ways and
- software that tracks game-specific entities such as crystals and treasures.


These sorts of requirements are quite technical, in that their implementation are well-defined, the metrics for their success is well-defined, and there is a linear relationship between requirements and their satisfaction. 

However, the last two requirements have a different character: they are hard to define, hard to measure (in any objective way) and 

Wicked problems in design
--------------------------------------------------

Wicked problems in design refer to those in which design requirements have complex dependencies that interact in non-linear ways. Such problems may be more common than supposed since design processes both attempt to satisfy design requirements as well as understand what these requirements mean. It may form a type of the whack-a-mole game in which as soon as one gains a understanding of a particular requirement, another springs up and effects interactions in the network of design alternatives and their requirements. 

This is an effect that speaks of the interdependencies between requirements. If a design can be modularized in which systems or sub-components can function independently from others then this effect is less pronounced.  

Example of this network effect
--------------------------------------------------

The opposite of an interdependent wicked-type problem are ones in which systems are separate. In the case of our wearable the components were:

- sensors and actuators
- processors and computational components
- user interfaces
- gaming components
- enclosure components (that are worn on the wrist)
- fashion components 

These components are not independent











