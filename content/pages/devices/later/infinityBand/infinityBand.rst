Infinity Band
==================================================

:slug: infinityBand
:url: pages/devices/later/infinityBand
:save_as: pages/devices/later/infinityBand.html

.. contents::

------

Sample UML: Sequence diagram

.. uml::
  	participant User

  	User -> A: DoWork
  	activate A #FFBBBB

  	A -> A: Internal call
  	activate A #DarkSalmon

  	A -> B: << createRequest >>
  	activate B

  	B --> A: RequestCreated
  	deactivate B
  	deactivate A
  	A -> User: Done
  	deactivate A



Introduction
--------------------------------------------------

Sample UML: Activity Diagram

.. uml::
	start
	:Hello world;
	:This is on defined on
	several **lines**;
	stop

Sample UML: Class diagram

.. uml::
	class Car
	Driver - Car : drives >
	Car *- Wheel : have 4 >
	Car -- Person : < owns


The Infinity Band is a sci-fi wearable toy designed to entertain children while encouraging them to stay active and fit. 

Sample UML: Class diagram

.. uml::
	scale 200 width
	Class01 <|-- Class02
	Class <|-- Subclass

Sample UML: Activity diagram

.. uml::
	start
	repeat
  	:read data;
  	:generate diagrams;
	repeat while (more data?)
	stop

Sample UML: Class diagram

.. uml::
	scale 200 width
	Class01 <|-- Class02
	Class <|-- Subclass

Sample UML: Object diagram

.. uml::
	object firstObject
	object "My Second Object" as o2

Sample UML: Object diagram

.. uml::
	object Object01
	object Object02
	object Object03
	object Object04
	object Object05
	object Object06
	object Object07
	object Object08

	Object01 <|-- Object02
	Object03 *-- Object04
	Object05 o-- "4" Object06
	Object07 .. Object08 : some labels


Sample UML: Object diagram

.. uml::
	object Node
	object Idea
	object Question
	object Evidence
	object Source
	object Knowledge
	
	Node <|-- Evidence
	Node <|-- Question
	Node <|-- Idea
	Node o- Source

	Evidence -> Question : raises
	Question -> Idea : inspires

	Evidence ..> Knowledge : suggests\nexistence of
	Question ..> Knowledge : defines\nlack of
	Idea ..> Knowledge : suggests path\ntowards new
	

Sample UML: Swimlanes

.. uml::
	scale 200 width
	|Swimlane1|
	start
	:foo1;
	|#AntiqueWhite|Swimlane2|
	:foo2;
	:foo3;
	|Swimlane1|
	:foo4;
	|Swimlane2|
	:foo5;
	stop



Worn on the wrist, the band enables children to play a magical collection game that encourages them to engage in a variety of active movements from low to high intensity. [both types of exercise are recommended for optimum health benefits - provide research]. 

Players are able to compete with other players, trade their finds and explore an exciting story-world opened up by their collection via an accompanying smart phone app.


The Story
--------------------------------------------------

The Infinity Band is a 'future artifact' created by the Time Keepers to locate and collect past and future Time Treasures. These objects have been, or will be, instrumental in shaping the path of history. The Infinity Band was stolen from the Time Vault of the Time Agents in 3015, and smuggled back to the present day once it became apparent that an evil force known as Bugly, was intent on the complete destruction to the very fabric of time and space.


Use Cases + Functions
--------------------------------------------------

The Infinity Band works by translating kinetic energy into Time Energy when activated in the correct way. It enables the wearer to reach through time and grab a Time Treasure from the future or past.


Generating Time Energy and Discovery
..................................................

The Infinity Band generates Time Energy through persistent motion. This Time Energy is stored in a circular band that surrounds the centerpiece of the device. The more walking, running or other exercise a child does the quicker their time energy will fill up. It will take approximately 90 minutes of activity to fill up the Time Energy from empty.

The centerpiece of the device will light up depending on the players progress. This could be split into three colours, bronze, sliver and gold. This indicates milestones in progress, or levels of achievement. Time wise this could be split into 40, 60 and 90 minutes of moderate movement. When each level is reached, the device will vibrate. Once for 40 minutes, twice for 60 minutes, and three times for 90 minutes.

Activity detection uses a combination of a heart rate monitor and pedometer to ensure that the player has is being active enough and is not just shaking the device with their wrist. The level of achievement will dictate the variety of the the treasure to be collected.

or

The player must reach gold to unlock a Time Treasure. If they have accomplished bronze or silver, then they will be awarded with power ups to use in the Time Tremors Infinity Game.


Retrieving a Treasure
..................................................

Treasures are awarded at the beginning of each day following the day of activity. This way, kids will look forward to opening the app with anticipation to discover what they have won. Once the treasure has been awarded, they receive encouragement for the activity for the day ahead. By connecting the device to the Infinity Band App, the player is able to view all of their collection including the Time Treasures they have just discovered, which will animate into the player’s collection board. By touching any of these treasures they are able to view a 3D explorable version of the Time Treasure, read about its back-story or trade the Time Treasure, and check leaders boards.


Leader Boards
..................................................

Leaders Boards exist for the player’s global collection as well as for each Mission they have undertaken. They are crucial for getting keeping a sense of competition across. Would also consider placing some fictional characters in the leader boards, so competing again Time Mutants or Bugly her very self to retrieve treasures quicker than she does.


Heart Rate
..................................................

There is a small hear shape light on the wrist band. When lit up, the player will receive an increased rate of time energy accumulation that goes above 60% to 70% of of their maximum heart rate, the cardio zone (A formula that appropriately estimates maximum heart rate is subtracting a persons age from 220. Although not exact, this formula works for most people in most conditions, player’s age will need to be acquired via app).

It is at this point and beyond that the player will achieve more health benefits such as fat burning. Trading and Treasure Fusing


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




