OCAD University Research Summary
#####################################
:slug: research

Adam Tindale
Michael Cumming
2014-8-27

Vibrotactile Arrays for Haptic Information Display
==================================================

Description
-----------

Haptic arrays can be at various resolutions and serve various purposes.
The body only has so much capacity to perceive discrete haptic
stimulation, therefore with a wrist-worn device there is limited
real-estate to place tactors and only so much density that haptic arrays
can achieve. This influences the type of information that be represented
using haptic arrays.

Progress
--------

Two wrist device have been built with haptic arrays. Two rubber
wristbands, one consists of 1x 8 tactor array and another with a 3x8
tactor array with buttons and LEDs. Two felt bands, one with a 1x8
tactor array, and another with a single tactor. The user interfaces are
basic in all these bands. One is automatically controlled from an
Arduino, one has buttons corresponding to tactors, two have variations
of ‘Simon Says’ games using buttons as user input.

Notation For Vibrotactile Arrays
================================

Description
-----------

Haptic arrays consist of many tactors, often in grid configurations.
Each motor can vibrate in time with a given intensity. The function of
these arrays is varied: they can be used to notify wearers of incoming
messages on social media, to tell when the wearer is geographically near
a point of interest, or for showing directions to a desired destination.
They can also be used to entertain the wearer with stimulating patterns
that evolve over time, similar to musical structure.

Authoring and programming such arrays can be difficult because of the
lack of a standardized notational system and standard file format.
Typically, each implementation of haptic arrays uses bespoke
programming, and much effort is duplicated unnecessarily. We propose
that standard musical notation is appropriate and useful for the design
of patterns utilizing such arrays. The implementation on the
microcontroller is provided using the MIDI format: a standard digital
format with a strong ability to represent time and discrete events,
which fulfills the criteria to control each motor effectively.

It would be advantageous if a wide variety of people, including those
with music composition backgrounds, could author these patterns rather
than wearable device technologists who are likely unfamiliar with
musical patterns and both standardized and innovative approaches to
their notation. The feedback from embodied patterns to musical
expression is an area of future investigation.

Using standard musical notation and associated techniques affords
several interesting possibilities, including: opportunities to represent
patterns in more sophisticated ways, to offer a canonical method for
researchers and technologists to exchange haptic patterns, and to apply
this knowledge to non-musical, or quasi-musical devices.

Progress
--------

There are two problems to address: 1. How to notate the haptic
activations such that they appear similar to Standard Musical Notation
(SMN) so that similar musical techniques can be applied to this
progress. 2. how to take this notation and play it on the device,
automatically or semi-automatically. Fortunately, modern musical
engraving software can accomplish both of these at the same time:
provide an authoring environment as well as automatically create the
Midi code that controls to the designed activations. The connection
between the notation and the device is via Arduino and the Arduino Midi
library package. The notation software is called Lilypond (and a related
front-end interface application called Frescobaldi). Lilypond is a
text-based engraving engine, that is, software for producing traditional
sheet music in SMN.

Tactors used in devices can be represented either as pitched or
unpitched notations. Tactors appear to be more like unpitched
instruments, where the notation needs to describe hitting or activating
the instrument but without concern for pitch. However, using pitched
notation has the advantage of being able to represent more things at the
same time, since each individual note has a related Midi number that can
be easily mapped to an individual tactor, or groups of tactors.  If
using unpitched notation, then you don’t have information on pitch and
must create information with channels other than pitch, including note
or part annotations that can be converted into tactor-appropriate data.

Using Midi for Haptic Activation on Devices
===========================================

Description
-----------

Vibe bracelets need activation patterns to operate. It is unclear how to
design such patterns in a standardized way. One obvious way is to use
the Midi control language to activate these devices. Two issues are: how
to compose rhythmic patterns that can be played on a vibrotactile band,
and how to translate these patterns into a form that the band
understands using Midi control data. One way of creating midi control
patterns is to compose music in such a way that midi data describing the
music is produced as a side-effect. This, of course, is standard
procedure in modern music production. One way of producing midi is by
using the text-based music engraving and compositional tool Lilypond.

Progress
--------

Tactors can be seen as a type of percussion instrument. Their activation
has timing and intensity but they lack the pitch of pitched instruments.
Pitched notes in musical notation when represented in midi each have a
Midi number corresponding to its pitch. This Midi number can be used to
distinguish one tactor from another. Therefore, even when driving an
unpitched tactor, representing notes as pitched is useful. It is not
clear however, if this is the useful method for design tactor rhythmic
patterns. An alternative approach would be to recognize tactor as arrays
of identical percussion instruments and to notate them in a similar way
to musical compositions for many percussion instruments, in which there
be few staves when these instruments play in unison and many staves when
they are play separate parts. This increases the complexity compared to
the pseudo-pitched note approach above, but means there might be less
information redundancy. It is unclear which of these two general
approaches is more suitable.

3D printing of components for devices
=====================================

Description
-----------

OCADU has 3D printing facilities. 3D printing is extremely useful for
creating quick prototypes for components suitable for wrist-wearable
devices including battery enclosures, LED mounts, and bracelet
components. 3D printing typically prints things using rigid plastic.
This material  is generally unsuitable for final production versions of
wearable components. 3D printing depends crucially on the quality of the
input files. These files (of type .STL) are generated by 3D CAD
applications. Once a suitable drawing CAD file is created then the
actual printing process is fully automated when using the MakerBot
Replicator 2 printer.

Progress
--------

The question then becomes how to draw CAD files efficiently, suitable
for wearable devices. There are two general approaches: draw visually in
a 3D space (say be using
`Sketchup <http://www.google.com/url?q=http%3A%2F%2Fwww.sketchup.com%2F&sa=D&sntz=1&usg=AFQjCNGJkjJjoeiWC2mhQZVJL5Y2zGVcjA>`__),
or draw analytically in a more abstract mathematical space. Our
experience seems to favour the second approach using an application
called
`OpenSCAD <http://www.google.com/url?q=http%3A%2F%2Fwww.openscad.org%2F&sa=D&sntz=1&usg=AFQjCNGZ0yFEjMi1NEzSm852Hi5xPknkuQ>`__.
The advantages of this approach is that often complex geometries are
more easily described, parameterized models are much easier to create,
and finally, it is much easier to refine and tweak a CAD model in which
variables are explicitly defined. Drawing this way requires thinking in
terms of `Constructive Solid
Geometry <http://www.google.com/url?q=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FConstructive_solid_geometry&sa=D&sntz=1&usg=AFQjCNEESRBY--cjuhmi01O9reR9R_Orww>`__ (CSG),
which creation of form is based on simple mathematical operations such
as union, difference and intersection.

Extending the Nexus Data Exchange Format (NDEF) Specification                 
==============================================================================

                

The Nexus Data Exchange Format (NDEF) is an Open Sound Control (OSC)
namespace specification designed to make development of OSC-based
systems easier by allowing for the identification of OSC nodes and the
exchange of OSC messages among nodes. In order to make NDEF more useful
for these tasks, new message types have been added to the namespace.
Node management has been improved with the addition of messages to
handle the pinging of nodes to determine their status. New namespace
addi- tions allow nodes to change messages on other nodes.

                         
                                                         

When musicians can spend less time on the configuration and setup of
their computer-based performance systems, it is obvious that they can
then spend more time on their ac- tual performances. Yet it is often the
case that the setup of computer music performance systems ends up taking
time away from what performers should focus on, rehearsing and
performing their actual music. This can be especially acute in the setup
of laptop orchestras with large numbers of per- formers or in
internet-based network performances, to name just two scenarios. Even
when the technology works flaw- lessly, both scenarios often require so
much time for setup that rehearsals are either rushed or do not happen
at all. In general, networked performance systems could benefit from
tools that make setup easier.                         

                        

Published: New Interfaces for Musical Expression 2014. London, England.

Notation For Vibrotactile Arrays
================================

.. raw:: html

   <div>

.. raw:: html

   </div>

