+++++++++++++++++++
python-htmlentities
+++++++++++++++++++

HTML Entities for Python

Installing
==========

For install python-htmlentities, run on terminal: ::

    $ [sudo] pip install htmlentities

Using htmlentities
==================

encoding
--------

You can encode a char to your htmlentitie relative using ``encode`` method: ::

    import htmlentities

    htmlentities.encode('<') # returns "&lt"

decoding
--------

You can decode a htmlentitie to your relative char using ``decode`` method: ::

    import htmlentities

    htmlentities.decode('&lt') # returns "<"


development
===========

* Source hosted at `GitHub <http://github.com/cobrateam/python-htmlentities>`_
* Report issues on `GitHub Issues <http://github.com/cobrateam/python-htmlentities/issues>`_

Pull requests are very welcomed! Make sure your patches are well tested.

running the tests
-----------------

if you are using a virtualenv, all you need is:

::

    $ make test

community
=========

irc channel
-----------

#cobrateam channel on irc.freenode.net
