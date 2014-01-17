#! -*- coding:utf-8 -*-
import unittest


class TestBox(unittest.TestCase):
    def _getTarget(self):
        from genaa.box import Box
        return Box

    def _makeOne(self, width=None, height=None, align='left', text=u''):
        class DummyStyle(object):
            space = u' '
            upperleft = u'g'
            upperright = u'r'
            lowerleft = u'm'
            lowerright = u'v'
            vertical = u'c'
            horizontal = u'h'

        return self._getTarget()(DummyStyle(), width=width, height=height, align=align, text=text)

    def test_body_content(self):
        actual = self._makeOne(text=u'01\n23456').body_content
        expected = [u'01',
                    u'23456']

        self.assertEqual(expected, actual)

    def test_render__autho_empty(self):
        actual = self._makeOne().render()
        expected = u"""\
gcccr
h   h
mcccv\
"""
        self.assertEqual(expected, actual)

    def test_render__auto(self):
        actual = self._makeOne(text=u"""\
1
345
67\
""").render()

        expected = u"""\
gcccccr
h 1   h
h 345 h
h 67  h
mcccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_empty(self):
        actual = self._makeOne(width=2, height=2).render()
        expected = u"""\
gccccr
h    h
h    h
mccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_fillup(self):
        actual = self._makeOne(width=2, height=2, text=u'1234').render()
        expected = u"""\
gccccr
h 12 h
h 34 h
mccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_overflow(self):
        actual = self._makeOne(width=2, height=2, text=u'12345').render()
        expected = u"""\
gccccr
h 12 h
h 34 h
mccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_enough(self):
        actual = self._makeOne(width=2, height=2, text=u'123').render()
        expected = u"""\
gccccr
h 12 h
h 3  h
mccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_with_2_lines_text(self):
        actual = self._makeOne(width=2, height=3, text=u'1\n23456').render()
        expected = u"""\
gccccr
h 1  h
h 23 h
h 45 h
mccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_only_height(self):
        actual = self._makeOne(height=3, text=u"""\
123
4567890\n
""").render()
        expected = u"""\
gcccccccccr
h 123     h
h 4567890 h
h         h
mcccccccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_only_width(self):
        actual = self._makeOne(width=3, text=u"""\
1
23
456
7890
""").render()
        expected = u"""\
gcccccr
h 1   h
h 23  h
h 456 h
h 789 h
h 0   h
mcccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__align_center(self):
        actual = self._makeOne(align='center', text=u"""\
1234
5\
""").render()
        expected = u"""\
gccccccr
h 1234 h
h  5   h
mccccccv\
"""
        self.assertEqual(expected, actual)

    def test_render__align_right(self):
        actual = self._makeOne(align='right', text=u"""\
1234
5\
""").render()
        expected = u"""\
gccccccr
h 1234 h
h    5 h
mccccccv\
"""
        self.assertEqual(expected, actual)
