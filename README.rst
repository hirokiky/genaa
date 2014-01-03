genaa, a ASCII Art generator
============================

.. image:: https://travis-ci.org/hirokiky/genaa.png?branch=master
   :target: https://travis-ci.org/hirokiky/genaa

genaa is a command line tool for generating ASCII Art::

      +-----+   +---+   +-----+     +-----+   +-----+
      |     |   |   |   |     |     |     |   |     |
    +-+---+ | +-+   +-+ | +---+-+ +-+---+ | +-+---+ |
    | |   | | |       | | |   | | | |   | | | |   | |
    | |   | | | +-----+ | |   | | | |   | | | |   | |
    | |   | | | |       | |   | | | |   | | | |   | |
    +-+---+ | +-+-----+ | |   | | +-+---+ | +-+---+ |
      |     |   |     | | |   | |   |     |   |     |
      +---+ |   +-----+ +-+   +-+   +-----+   +-----+
          | |
      +---+-+
      |   |
      +---+

Install
---------
Install genaa by using pip.

::

    pip install genaa

Now genaa is supporting only Python 3.3.


Basic Usage
---------------

genaa has some sub-commands to render various ASCII Arts:

* box
* block

`genaa box` is the most basic and simple feature.
It can render a block containing text input by user::

    $ genaa box --text Hello!
    +--------+
    | Hello! |
    +--------+

`genaa block` is a command to render some free shape blocks.
It takes some 'dots' and translate it to ASCII Art blocks.
This example show you how to create a well-known TETRIS block from command line::

    $ genaa block --text '
    > ***
    >  * '

    +-----+
    |     |
    +-+ +-+
      | |
      +-+

As filter
-----------

Above examples are used as one of simple command line tools, using --text argument.
But, genaa usually behaves as a filter command, like this::

    $ echo -en 'Hello world!\nThis is genaa' | genaa box
    +---------------+
    | Hello world!  |
    | This is genaa |
    +---------------+

Generally, it is recommended to use from some editors.
Most editors has a feature to pass the selected text to some shell command
and input returned value. On Emacs, you can use 'shell-command-on-region'.

genaa box
-------------------
You can specify these arguments to `genaa box`::

      -h, --help            show this help message and exit
      -t TEXT, --text TEXT  Passing text by argument into box
      -W WIDTH, --width WIDTH
      -H HEIGHT, --height HEIGHT
      -s {ccomment,ascii,hash,simple}, --style {ccomment,ascii,hash,simple}
      -l, --list            Displaying examples for each styles

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
^^^^^^^^
This example is using `hash` style which is used as comment block in Python::

    $ echo -en 'Hello world!\nThis is genaa' | genaa box --style=hash
    #################
    # Hello world!  #
    # This is genaa #
    #################

--list
^^^^^^^
The list of styles are on `genaa box --list` command::

    $ genaa box --list
    ascii:
    +-----------------------+
    | Hello.                |
    | How about this style? |
    +-----------------------+

    ccomment:
    /************************
    * Hello.                *
    * How about this style? *
    ************************/

    hash:
    #########################

--align
^^^^^^^^
`genaa box` command put the text at the left side of the box.
It also supports putting the text on center and right::

    genaa box --align=center --text=Hello --width=20
    +----------------------+
    |        Hello         |
    +----------------------+

genaa block
------------
You can specify these arguments to `genaa block`::

  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  Passing text by argument into block
  -s {ascii,simple}, --style {ascii,simple}
  -l, --list            Displaying examples for each styles

--style
^^^^^^^^
This example is using `simple` style.
You can see this clearly by some mono-space fonts::

    $ genaa block --style=simple
    **
    * *
     *
    ┌───┐
    │   │
    │ ┌─┼─┐
    │ │ │ │
    └─┼─┼─┘
      │ │
      └─┘

--list
^^^^^^^^

The list of styles are on `genaa block --list` command::

    $ genaa block --list
    ascii:
      +-+
      | |
      +-+-+   +-+ +-+       +-+   +-+       +-+
        | |   | | | |       | |   | |       | |
    +---+ |   +-+-+ |   +-+ | |   +-+---+   +-+-+
    |     |     |   |   | | | |     |   |     | |
    +-----+     | +-+   +-+-+ |   +-+ +-+ +---+ |
                | |       |   |   |   |   |     |
                +-+       +---+   +---+   +-----+

    simple:
      ┌─┐
      │ │
      └─┼─┐   ┌─┐ ┌─┐       ┌─┐   ┌─┐       ┌─┐
        │ │   │ │ │ │       │ │   │ │       │ │
    ┌───┘ │   └─┼─┘ │   ┌─┐ │ │   └─┼───┐   └─┼─┐

