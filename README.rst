genaa, a AA generator
======================

genaa is a command line tool for generating ASCII art.

Install
---------
Install genaa by using pip.

::

    pip install git+https://github.com/hirokiky/genaa

Basic Usage
---------------
Now genaa can only generate a box, by specifying --width and --height::

    echo -e 'Hello world!\nThis is genaa' | genaa box --width=13 --height=2
    ┌─────────────┐
    │Hello world! │
    │This is genaa│
    └─────────────┘

