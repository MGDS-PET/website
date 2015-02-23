Infinity Band
==================================================

:slug: infinityBand
:url: pages/devices/later/infinityBand
:save_as: pages/devices/later/infinityBand.html

.. image:: /images/devices/later/infinityBand/P1140028.JPG
	:alt: infinity band 1
	:width: 25%

.. image:: /images/devices/later/infinityBand/P1140029.JPG
	:alt: infinity band 2
	:width: 25%

.. image:: /images/devices/later/infinityBand/P1140030-003.JPG
	:alt: infinity band components
	:width: 25%


.. contents::

.. sectnum::
	:depth: 3


Description
--------------------------------------------------

The Infinity Band is a sci-fi wearable toy designed to entertain children while encouraging them to stay active and fit. Worn on the wrist, the band enables children to play a magical collection game. This game encourages them be physically active and to engage in a variety of active movements from low to high intensity. Players are able to compete with other players, trade their finds and explore an exciting story-world opened up by their collection via an accompanying smart phone app.


The transmedia story
..................................................

The Infinity Band is a 'future artifact' created by the Time Keepers to locate and collect past and future Time Treasures. These objects have been, or will be, instrumental in shaping the path of history. The Infinity Band was stolen from the Time Vault of the Time Agents in 3015, and smuggled back to the present day once it became apparent that an evil force known as Bugly, was intent on the complete destruction to the very fabric of time and space.


Design and research questions
--------------------------------------------------

- What is its intended functionality (to integrate it with the transmedia game *Time Tremors*)?
- What are suitable components for this kind of functionality?
- What is the best way of fitting its required electronics components within a robust, wearable device?
- How can the size of the device be reduced such that is fits onto the small wrists of its intended wearers (pre-teen children aged 7-12)?
- How can the design of the device connect with the style of the transmedia series *Time Tremors*?

Components
--------------------------------------------------

- 3D printed plastic case
- Laser-etched leather band
- LightBlue Bean WiFi-enabled microprocessor
- LED light ring: 12 x RGB LED with Integrated Drivers (by NeoPixel)
- Heart rate (HR) sensor
- Galvanic skin response (GSR) sensor
- LiPo battery (110 mAh min.)
- LiPo battery charging connector unit


Introduction to device functions 
--------------------------------------------------------------------------------------
(Based on *Time Tremors* transmedia game concepts).

The Infinity Band works by translating kinetic energy into Time Energy when activated in the correct way. It enables the wearer to reach through time and grab a Time Treasure from the future or past.


Generating Time Energy through physical activity
..................................................

The Infinity Band generates Time Energy through persistent motion. This Time Energy is stored in a circular band that surrounds the centerpiece of the device. The more walking, running or other exercise a child does the quicker their time energy will accumulate. It takes approximately 90 minutes of physical activity to fill up the Time Energy from empty.

The centerpiece of the device will light up depending on the players progress towards greater physical activity. This are split into three achievement levels, or progress milestones: the colours bronze, sliver and gold. Time wise this could be split into 40, 60 and 90 minutes of moderate movement. When each level is reached, the device will vibrate. Once for 40 minutes, twice for 60 minutes, and three times for 90 minutes.

Activity detection uses a combination of a heart rate monitor and accelerometer measurements to ensure that the player has is being active enough and is not just shaking the device with their wrist. The level of achievement will dictate the variety of the the treasure to be collected.

The player must reach gold to unlock a Time Treasure. If they have accomplished bronze or silver, then they will be awarded with power ups to use in the *Time Tremors* Infinity Game.


Retrieving a Treasure
..................................................

Treasures are awarded at the beginning of each day following a day of activity. This way, kids will look forward to opening the app with anticipation to discover what they have won. Once the treasure has been awarded, they receive encouragement for the activity for the day ahead. By connecting the device to the Infinity Band app, the player is able to view all of their collection including the Time Treasures they have just discovered, which will animate into the player’s collection board. 

By touching any of these treasures they are able to view a 3D explorable version of the Time Treasure, read about its back-story or trade the Time Treasure, and check Leader Boards.


Leader Boards
..................................................

Leaders Boards exist for the player’s global collection as well as for each Mission they have undertaken. They are crucial for keeping a sense of competition across games. Fictional characters also occur in the leader boards, so players can compete against Time Mutants or Ms. Bugly, to test whether they can retrieve treasures quicker than they can.


Heart rate measurements
..................................................

There is a small hear shape light on the wrist band. When lit up, the player will receive an increased rate of time energy accumulation that goes above 60% to 70% of of their maximum heart rate, the cardio zone (A formula that appropriately estimates maximum heart rate is subtracting a persons age from 220. Although not exact, this formula works for most people in most conditions, player’s age will need to be acquired via app).

It is at this point and beyond that the player will achieve more health benefits such as fat burning. Trading and Treasure Fusing


User stories / Use cases
--------------------------------------------------

**Pattern used for composing user stories**: "As a **<role>**, I want to **<goal/desire>** so that **<benefit occur>**"

Actor: game player, child aged 7-12
..................................................

#. Wear the Infinity Band wrist device
	"As a game player I want to wear the device and do interesting things with the device such as measure time and keep track of things about my body such as my heart rate"

#. Play the *Time Tremors* game (using the Infinity Band wrist device)
	"As a game player I want to play the *Time Tremors* game in an interactive way so I can earn points and progress enjoyably within the game"

#. Generate Time Energy
	"As a game player I want to use physical activity to generate Time Energy, because Time Energy is the game's currency and it enables me to continue playing the game"

#. Earn and unlock a Treasure
	"As a game player I want to earn a Treasure, so that I can learn more about the history that surrounds the Treasure"


Actor: content creator
..................................................

#. Create a treasure
	"As a content creator I want to create a treasure that the game player will find informative, interesting and worthwhile to collect"

#. Create a collections of treasures
	"As a content creator I want to create a set of treasures that is coherent and that interests players"

#. Define how much physical activity is required to unlock a treasure
	"As a content creator I want to create a sensible relationship between energy expended and the value of treasure obtained as a result"

#. Create levels of achievement
	"As a content creator I want to create a coherent system of levels so players can measure their achievements"


Actor: system designer
..................................................

#. Measure player's overall physical activity
	"As a system designer I want to combine real-time sensor data into an accurate representation of the wearer's overall physical activity"




Discussion and results
--------------------------------------------------

Band as a wearable device
..................................................

Playing the *Time Tremors* game on the device
..................................................

Converting sensor data into an aggregate measure of overall physical activity
...............................................................................

Content creation: treasures and treasure collections
........................................................

Content creation: achievement levels
..................................................

System integration: aggregating sensor data
.................................................



Visual Resources and Inspiration
--------------------------------------------------

.. figure:: /images/devices/later/infinityBand/Page_1.jpg
	:alt: infinity band page 1
	:figwidth: 32%

	Leather work and buckles.

-------

.. figure:: /images/devices/later/infinityBand/Page_2.jpg
	:alt: infinity band page 2
	:figwidth: 32%

	Edges evoke time passing.

-------

.. figure:: /images/devices/later/infinityBand/Page_3.jpg
	:alt: infinity band page 3
	:figwidth: 32%

	Containers of time energy.

-------

.. figure:: /images/devices/later/infinityBand/Page_4.jpg
	:alt: infinity band page 4
	:figwidth: 32%

	Cogs 1.

-------

.. figure:: /images/devices/later/infinityBand/Page_5.jpg
	:alt: infinity band page 5
	:figwidth: 32%

	Cogs 2.

-------

.. figure:: /images/devices/later/infinityBand/Page_6.jpg
	:alt: infinity band page 6
	:figwidth: 32%

	Exposed electronics in secret compartment.

-------

.. figure:: /images/devices/later/infinityBand/Page_7.jpg
	:alt: infinity band page 7
	:figwidth: 32%

	Relief leather work with metallic finish.

-------

.. figure:: /images/devices/later/infinityBand/Page_8.jpg
	:alt: infinity band page 8
	:figwidth: 32%

	Beautiful texture and light container [could work well for heart rate monitor and low battery indicator].

-------

.. figure:: /images/devices/later/infinityBand/Page_9.jpg
	:alt: infinity band page 9
	:figwidth: 32%

	Detachable components with interesting stud work.
	


Questions
--------------------------------------------------

- Should there be a battery indicator on the device?
- Should there be a warning light if a player reaches a dangerously high heart rate?
- Should app use the same message methods as TT Infinity?
- Do two different scenarios of how core mechanics could work, gold, silver, bronze, treasure only awarded if gold is achieved.
- How should basic information--such as start of day and end of day--be delivered through the interface?




