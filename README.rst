genaa, a ASCII Art generator
============================

.. image:: https://travis-ci.org/hirokiky/genaa.png?branch=master
   :target: https://travis-ci.org/hirokiky/genaa

genaa is a command line tool for generating ASCII Art.

Install
---------
Install genaa by using pip.

::

    pip install git+https://github.com/hirokiky/genaa

Basic Usage
---------------
Now genaa can only generate a box::

    $ genaa box --text Hello!
    +--------+
    | Hello! |
    +--------+

Above example is as one of simple command line tools.
But, genaa usually behave as a filter command, like this::

    $ echo -en 'Hello world!\nThis is genaa' | genaa box
    +---------------+
    | Hello world!  |
    | This is genaa |
    +---------------+

genaa box
-------------------
You can specify these arguments to `genaa box`::

    genaa box --help
    usage: genaa box [-h] [-t TEXT] [-W WIDTH] [-H HEIGHT]
                     [-s {ccomment,ascii,hash,simple}] [-a {left,center,right}]

    optional arguments:
      -h, --help            show this help message and exit
      -t TEXT, --text TEXT  Passing text by argument into box
      -W WIDTH, --width WIDTH
      -H HEIGHT, --height HEIGHT
      -s {ccomment,ascii,hash,simple}, --style {ccomment,ascii,hash,simple}

--width and --height
^^^^^^^^^^^^^^^^^^^^^^^^^^
By default, `genaa box`  command render the box with automatically specified width/height.
But, you can specify these width and height of the box manually, like this::

    $ echo -en 'Hello world!\nThis is genaa' | genaa box --width=20 --height=3
    +----------------------+
    | Hello world!         |
    | This is genaa        |
    |                      |
    +----------------------+

--style
----------
This example is using `hash` style which is used as comment block in Python::

    $ echo -en 'Hello world!\nThis is genaa' | genaa box --style=hash
    #################
    # Hello world!  #
    # This is genaa #
    #################

--align
------------
`genaa box` command put the text at the left side of the box.
It also supports putting the text on center and right::

    genaa box --align=center --text=Hello --width=20
    +----------------------+
    |        Hello         |
    +----------------------+
