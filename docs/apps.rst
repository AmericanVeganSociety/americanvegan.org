====
Apps
====

A number of Django apps power the American Vegan Society's website.
They are listed in detail below.

``avs``
=======
Contains site settings, static files, global templates, and global blocks.
In general, things that affect the whole site (or multiple parts of it) go here.

``blog``
========
American Vegan Society has a quarterly magazine that they publish (physically) and distribute to members.
Some articles from these magazines might also be published online, at the same time the physical magazine issue is released.
This app contains those articles.

``events``
==========
AVS keeps a calendar of events.
The calendar lists events that AVS hosts, as well as events that they endorse.
This app stores and displays those events.

``home``
========
This is the first thing users will see when they visit americanvegan.org.
This app deals with rendering the homepage.

``info_pages``
==============
AVS has a lot of detailed content relating to veganism and their organization.
This app enables editors to comfortably write long, complex documents which are then displayed on thi site.

``magazine``
============
AVS's quarterly magazine, "American Vegan," is indexed on the site here.
Users can find the whole list of issues in this app.
Many older issues are available to the public for free, while newer issues are restricted to members only.

``members``
===========
People can sign up to become AVS members by offering a recurring donation.
This app contains the necessary forms for people to become members or manage their membership.
Additionally, it stores metadata about members in the database.

``merchandise``
===============
AVS sells some physical items, including t-shirts and books.
Goods can be purchased in person at their headquarters or by placing an order online.
This app deals with selling and managing online merchandise.

``newsletter``
==============
Email campaigns are sent out to members who enroll in a mailing list.
This app deals with subscription to and from the email list.

``portals``
===========
The top level pages for the entire site, directly below the home page.
Few portals should exist; at the time of writing they are: *Discover*, *Act*, and *Support*.
All lower-level content can be broken up into these sections.
Portals allow users to navigate deeper into the site by guiding users into the child pages of the portal.

``recipes``
===========
AVS keeps a digital cookbook of vegan recipes.
This app stores and displays those recipes.

``search``
==========
Full-text search across the entire website.
This app handles the search bar and search results.

``speakers``
============
The AVS Speakers Bureau is a group of vegan speakers.
This app displays profiles for members of the bureau.

``vips``
========
VIPs (*vegan information points*) are people who have volunteered to be contacted to provide resources about veganism.
This international group is displayed with points on a map alongside their contact information.
