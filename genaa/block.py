"""
Rendering a free shape block.

input::

    . .
    ...

output::

    +-+ +-+
    | | | |
    | +-+ |
    |     |
    +-----+

To render the final output the input will be separated to many parts.
For more readability, this is new input that each dots have own names.

input::

    a b
    cde

To analyse which character should be put on the output,
First, the input will be separated like this::

  '   a', ' a', '  a ', '  ', '   b', ' b', '  b ',
  ' a', 'a', 'a ', ' ', ' b', 'b', 'b '
  ' a c', 'ac', 'a cd', ' d', ' bde', 'be', 'b e '
  ' c', 'c', 'cd', 'd', 'de', 'e', 'e '
  ' c  ', 'c ', 'cd  ', 'd ', 'de  ', 'e ', 'e   '

These 35 parts are corresponding to each characters of the final output.
For instance, the top left part '   a' will translate to '+' which is
corresponding to the top left '+' on the output.

Each parts can be classified to 4 categories, 'body', 'vertical', 'horizontal and 'cross'.
That '   a' is one of crosses.
Above separated parts is aligned, according to following rule::

  cross, vertical, cross, vertical, cross ... vertical, cross
  horizontal, body, horizontal, body, ... horizontal, body
  cross, vertical, cross, vertical, cross ... vertical, cross
  ...
  cross, vertical, cross, vertical, cross ... vertical, cross

Ways to render each parts can be specified by following patterns.

body
------
body is a part for filling the rendered block and empty space.
On the above example, 'a' on the second line is one of bodies.
bodies are directory corresponding to user inputs.

bodies will be rendered according to the rule::

     body  | style
    -------+----------
     True  | body
     False | space

If the body is not space character (' '), the body of style will be rendered.

horizontal
--------------
horizontal is a part for separating blocks and empty space.
On the above example, ' c' on the fourth line is one of verticals.
' c' means 'a block is in the right side and the left side is empty.' like this::

   left   |x    right

So then, Notice that the part ' c' should be some lines like '|' to separate
block and empty space.

horizontal will be rendered according to the rule::

      left | right | style
    -------+-------+--------
      True |  True | body
      True | False | horizontal
     False |  True | horizontal
     False | False | space

The ' c' means 'left: False, right: True' so the horizontal of style will be rendered finally.

vertical
------------
vertical is a part for separating blocks and empty space as same as horizontal.
On the above example, 'c ' ond the fifth line is one of verticals.
'c ' means 'a block is in the upper and the lower is empty.' like this::

      upper
        x
        -

      lower

So then, Notice that the part 'c ' should be some lines like '-' to separate
block and empty space.

verticals will be rendered according to the rule::

     upper | lower | style
    -------+-------+--------
      True |  True | body
      True | False | vertical
     False |  True | vertical
     False | False | space

The 'c ' means 'upper: True, lower: False' so the vertical of style will be rendered.

cross
-------
cross is the most difficult part, where some lines will across or one line will be folded.
On the above example, '   a' on the first line is one of crosses.
'    a' means 'a block is on the lower left and the others are empty.' like this::

    upper left       upper right
                 |
                -o-
                 |x
     lower left      lower right

So then, Notice that the part '   a' should be an upper left corner
(on this example, all corner is renderd by '+').

crosses will be rendered according to the rule::

      upper left | upper right |  lower left | lower right | style
    -------------+-------------+-------------+-------------+------------
         True    |     True    |     True    |     True    | body
         True    |     True    |     True    |    False    | upper left
         True    |     True    |    False    |     True    | upper right
         True    |     True    |    False    |    False    | vertical
         True    |    False    |     True    |     True    | lower left
         True    |    False    |     True    |    False    | horizontal
         True    |    False    |    False    |     True    | cross
         True    |    False    |    False    |    False    | lower right
        False    |     True    |     True    |     True    | lower right
        False    |     True    |     True    |    False    | cross
        False    |     True    |    False    |     True    | horizontal
        False    |     True    |    False    |    False    | lower left
        False    |    False    |     True    |     True    | vertical
        False    |    False    |     True    |    False    | upper right
        False    |    False    |    False    |     True    | upper left
        False    |    False    |    False    |    False    | space

The '   a' means 'upper left: False, upper right: False, lower left: False, lower right: True'
so the upper left of style will be rendered.
"""
import itertools

from genaa import utils as genaa_utils


def wrap_mapping(mapping, fillwith=' '):
    """

    ['. .',
     '...']

    to

    ['     ',
     ' . . ',
     ' ... ',
     '     ']
    """
    max_width = max(map(len, mapping))
    redundant_row = [fillwith*(max_width+2)]
    mapping = [fillwith + row.ljust(max_width+1, fillwith) for row in mapping]
    return redundant_row + mapping + redundant_row


def slice_wrapper(mapping):
    """
    ['     ',
     ' . . ',
     ' ... ',
     '     ']

    to

    ['. .',
     '...']
    """
    mapping = mapping[1:-1]
    return [row[1:-1] for row in mapping]


def translate_to_bool_mapping(mapping, falsewith=' '):
    """

    ['. .',
     '...']

    to:

    [[True, False, True]
     [True, True, True]]
    """
    ret = []
    for row in mapping:
        ret.append([cell != falsewith for cell in row])
    return ret


def one_x_one(mapping):
    for row in mapping:
        yield (cell for cell in row)


def two_x_one(mapping):
    for row in mapping:
        yield ((row[i], row[i+1]) for i in range(len(row)-1))


def one_x_two(mapping):
    for y in range(len(mapping)-1):
        yield ((mapping[y][x], mapping[y+1][x]) for x in range(len(mapping[y])))


def two_x_two(mapping):
    for y in range(len(mapping)-1):
        yield ((mapping[y][x], mapping[y][x+1], mapping[y+1][x], mapping[y+1][x+1])
               for x in range(len(mapping[y])-1))


def render_block(mapping, style):
    mapping = wrap_mapping(mapping)
    mapping = translate_to_bool_mapping(mapping)
    body_pattern = generate_body_pattern(style)
    horizontal_pattern = generate_horizontal_pattern(style)
    vertical_pattern = generate_vertical_pattern(style)
    cross_pattern = generate_cross_pattern(style)

    body_lines = [''.join(map(lambda x: body_pattern[x], row))
                  for row in one_x_one(mapping)]
    horizontal_lines = [''.join(map(lambda x: horizontal_pattern[x], row)) for
                        row in two_x_one(mapping)]
    vertical_lines = [''.join(map(lambda x: vertical_pattern[x], row)) for
                      row in one_x_two(mapping)]
    cross_lines = [''.join(map(lambda x: cross_pattern[x], row)) for
                   row in two_x_two(mapping)]

    body_lines = [''.join(genaa_utils.zipped_iter(b, h))
                  for b, h in itertools.zip_longest(body_lines, horizontal_lines, fillvalue=[])]
    border_lines = [''.join(genaa_utils.zipped_iter(v, c))
                    for v, c in itertools.zip_longest(vertical_lines, cross_lines, fillvalue=[])]

    mapping = list(genaa_utils.zipped_iter(body_lines, border_lines))
    return '\n'.join(slice_wrapper(mapping))


def generate_body_pattern(style):
    return {
        True: style.body,
        False: style.space,
    }


def generate_horizontal_pattern(style):
    return {
        (True, True): style.body,
        (True, False): style.horizontal,
        (False, True): style.horizontal,
        (False, False): style.space,
    }


def generate_vertical_pattern(style):
    return {
        (True, True): style.body,
        (True, False): style.vertical,
        (False, True): style.vertical,
        (False, False): style.space,
    }


def generate_cross_pattern(style):
    return {
        (True, True, True, True): style.body,
        (True, True, True, False): style.upperleft,
        (True, True, False, True): style.upperright,
        (True, True, False, False): style.vertical,
        (True, False, True, True): style.lowerleft,
        (True, False, True, False): style.horizontal,
        (True, False, False, True): style.cross,
        (True, False, False, False): style.lowerright,
        (False, True, True, True): style.lowerright,
        (False, True, True, False): style.cross,
        (False, True, False, True): style.horizontal,
        (False, True, False, False): style.lowerleft,
        (False, False, True, True): style.vertical,
        (False, False, True, False): style.upperright,
        (False, False, False, True): style.upperleft,
        (False, False, False, False): style.space,
    }


class ASCIIStyle(object):
    space = ' '
    body = ' '
    upperleft = '+'
    upperright = '+'
    lowerleft = '+'
    lowerright = '+'
    vertical = '-'
    horizontal = '|'
    cross = '+'


class SimpleStyle(object):
    space = ' '
    body = ' '
    upperleft = '┌'
    upperright = '┐'
    lowerleft = '└'
    lowerright = '┘'
    vertical = '─'
    horizontal = '│'
    cross = '┼'


style_mapping = {
    'ascii': ASCIIStyle,
    'simple': SimpleStyle,
}
