genaa, a AA generator
======================

.. image:: https://travis-ci.org/hirokiky/genaa.png?branch=master
   :target: https://travis-ci.org/hirokiky/genaa

genaa is a command line tool for generating ASCII art.

Install
---------
Install genaa by using pip.

::

    pip install git+https://github.com/hirokiky/genaa

Basic Usage
---------------
Now genaa can only generate a box::

    echo -e 'Hello world!\nThis is genaa' | genaa box
    ┌─────────────┐
    │Hello world! │
    │This is genaa│
    └─────────────┘

You can also specify width and height of the box::

    echo -e 'Hello world!\nThis is genaa' | genaa box --width=20 --height=3
    ┌────────────────────┐
    │Hello world!        │
    │This is genaa       │
    │                    │
    └────────────────────┘

And changing the style of the box.
This example is using `hash` style which is used as comment block in Python::

    $ echo -e 'Hello world!\nThis is genaa' | genaa box --style=hash
    ###############
    #Hello world! #
    #This is genaa#
    ###############

