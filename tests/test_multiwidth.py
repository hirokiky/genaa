#! -*- coding: utf-8 -*-
import unittest


class TestChunks(unittest.TestCase):
    def _getTarget(self):
        from genaa.multiwidth import chunk_strings
        return chunk_strings

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__one_chunk(self):
        actual = self._callFUT(u'0123', 4)
        self.assertEqual([u'0123'], list(actual))

    def test__divided_equally(self):
        actual = self._callFUT(u'01234567', 4)
        self.assertEqual([u'0123', u'4567'], list(actual))

    def test__with_a_rest(self):
        actual = self._callFUT(u'01234', 4)
        self.assertEqual([u'0123', u'4'], list(actual))


class TestStrWidth(unittest.TestCase):
    def _getTarget(self):
        from genaa.multiwidth import str_width
        return str_width

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__ascii(self):
        actual = self._callFUT(u'0123')
        self.assertEqual(4, actual)

    def test__japanese(self):
        actual = self._callFUT(u'あいうえお')
        self.assertEqual(10, actual)

    def test__mix(self):
        actual = self._callFUT(u'0123あいうえお')
        self.assertEqual(14, actual)
