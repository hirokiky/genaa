#! -*- coding: utf-8 -*-
class Box(object):
    space = u' '

    min_width = 2
    min_height = 2

    def __init__(self, width, height, border):
        if self.min_width > width:
            raise ValueError('Applied width is too small %s (required %s)',
                             width, self.min_width)
        if self.min_height > height:
            raise ValueError('Applied height is too small %s (required %s)',
                             height, self.min_height)
        self.width = width
        self.height = height
        self.border = border

    def render(self):
        space_width = self.width - 2
        space_height = self.height - 2
        vertical = self.border.vertical * space_width
        row = self.border.horizontal + self.space * space_width + self.border.horizontal
        return '\n'.join(
            [self.border.upperleft + vertical + self.border.upperright] +
            [row] * space_height +
            [self.border.lowerleft + vertical + self.border.lowerright]
        )


class SimpleBorder(object):
    upperleft = u'┌'
    upperright = u'┐'
    lowerleft = u'└'
    lowerright = u'┘'
    vertical = u'─'
    horizontal = u'│'
