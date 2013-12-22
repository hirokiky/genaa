#! -*- coding:utf-8 -*-
import unittest


class TestBox(unittest.TestCase):
    def _getTarget(self):
        from genaa.box import Box
        return Box

    def _makeOne(self, width, height, text=u''):
        class DummyBorder(object):
            space = u' '
            upperleft = u'g'
            upperright = u'r'
            lowerleft = u'm'
            lowerright = u'v'
            vertical = u'c'
            horizontal = u'h'

        return self._getTarget()(width, height, DummyBorder(), text=text)

    def test_body_content(self):
        actual = self._makeOne(5, 9999, u'01\n23456').body_content
        expected = [u'01',
                    u'234',
                    u'56']

        self.assertEqual(expected, actual)

    def test_fillup(self):
        actual = self._makeOne(6, 5).fillup([u'01',
                                             u'2345'])
        expected = [u'01  ',
                    u'2345',
                    u'    ']

        self.assertEqual(expected, actual)

    def test_render__empty(self):
        actual = self._makeOne(4, 4).render()
        expected = u"""\
gccr
h  h
h  h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__fillup(self):
        actual = self._makeOne(4, 4, u'1234').render()
        expected = u"""\
gccr
h12h
h34h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__overflow(self):
        actual = self._makeOne(4, 4, u'12345').render()
        expected = u"""\
gccr
h12h
h34h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__enough(self):
        actual = self._makeOne(4, 4, u'123').render()
        expected = u"""\
gccr
h12h
h3 h
mccv\
"""
        self.assertEqual(expected, actual)

    def test_render__with_2_lines_text(self):
        actual = self._makeOne(4, 5, u'1\n23456').render()
        expected = u"""\
gccr
h1 h
h23h
h45h
mccv\
"""
        self.assertEqual(expected, actual)
