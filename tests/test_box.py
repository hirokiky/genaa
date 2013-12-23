#! -*- coding:utf-8 -*-
import unittest


class TestBox(unittest.TestCase):
    def _getTarget(self):
        from genaa.box import Box
        return Box

    def _makeOne(self, width=None, height=None, text=u''):
        class DummyStyle(object):
            space = u' '
            upperleft = u'g'
            upperright = u'r'
            lowerleft = u'm'
            lowerright = u'v'
            vertical = u'c'
            horizontal = u'h'

        return self._getTarget()(DummyStyle(), width=width, height=height, text=text)

    def test_body_content(self):
        actual = self._makeOne(text=u'01\n23456').body_content
        expected = [u'01',
                    u'23456']

        self.assertEqual(expected, actual)

    def test_render__autho_empty(self):
        actual = self._makeOne().render()
        expected = u"""\
gcr
h h
mcv\
"""
        self.assertEqual(expected, actual)

    def test_render__auto(self):
        actual = self._makeOne(text="""\
1
345
67\
""").render()

        expected = u"""\
gcccr
h1  h
h345h
h67 h
mcccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_empty(self):
        actual = self._makeOne(2, 2).render()
        expected = u"""\
gccr
h  h
h  h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_fillup(self):
        actual = self._makeOne(2, 2, u'1234').render()
        expected = u"""\
gccr
h12h
h34h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_overflow(self):
        actual = self._makeOne(2, 2, u'12345').render()
        expected = u"""\
gccr
h12h
h34h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_enough(self):
        actual = self._makeOne(2, 2, u'123').render()
        expected = u"""\
gccr
h12h
h3 h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_with_2_lines_text(self):
        actual = self._makeOne(2, 3, u'1\n23456').render()
        expected = u"""\
gccr
h1 h
h23h
h45h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fixed_only_height(self):
        actual = self._makeOne(height=3, text=u"""\
123
4567890
""").render()
        expected = u"""\
gcccccccr
h123    h
h4567890h
h       h
mcccccccv\
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
gcccr
h1  h
h23 h
h456h
h789h
h0  h
mcccv\
"""
        self.assertEqual(expected, actual)
