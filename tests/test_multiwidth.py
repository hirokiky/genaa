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

    def test__with_multi_width_characters(self):
        actual = self._callFUT(u'林原めぐみ', 4)
        self.assertEqual([u'林原', u'めぐ', u'み'], list(actual))

    def test__with_multi_width_characters_and_ascii(self):
        actual = self._callFUT(u'藤子Fふじお', 3)
        self.assertEqual([u'藤', u'子F', u'ふ', u'じ', u'お'], list(actual))


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

    def test__hald_width_japanese(self):
        actual = self._callFUT(u'ｱｲｳｴｵ')
        self.assertEqual(5, actual)

    def test__mix(self):
        actual = self._callFUT(u'0123あいうえお')
        self.assertEqual(14, actual)


class TestRJust(unittest.TestCase):
    def _getTarget(self):
        from genaa.multiwidth import rjust
        return rjust

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__ascii(self):
        actual = self._callFUT(u'a', 3)
        self.assertEqual(u'  a', actual)

    def test__multi_width_characters(self):
        actual = self._callFUT(u'あ', 3)
        self.assertEqual(u' あ', actual)

    def test__multi_width_fullchar(self):
        actual = self._callFUT(u'申', 4, fillchar=u'ネ')
        self.assertEqual(u'ネ申', actual)

    def test__multi_width_fullchar_with_rest(self):
        actual = self._callFUT(u'申', 5, fillchar=u'ネ')
        self.assertEqual(u'ネ申', actual)


class TestLJust(unittest.TestCase):
    def _getTarget(self):
        from genaa.multiwidth import ljust
        return ljust

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__ascii(self):
        actual = self._callFUT(u'a', 3)
        self.assertEqual(u'a  ', actual)

    def test__multi_width_characters(self):
        actual = self._callFUT(u'あ', 3)
        self.assertEqual(u'あ ', actual)

    def test__multi_width_fullchar(self):
        actual = self._callFUT(u'ネ', 4, fillchar=u'申')
        self.assertEqual(u'ネ申', actual)

    def test__multi_width_fullchar_with_rest(self):
        actual = self._callFUT(u'ネ', 5, fillchar=u'申')
        self.assertEqual(u'ネ申', actual)


class TestCenter(unittest.TestCase):
    def _getTarget(self):
        from genaa.multiwidth import center
        return center

    def _callFUT(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__ascii_by_odd_width(self):
        actual = self._callFUT(u'a', 3)
        self.assertEqual(u' a ', actual)

    def test__ascii_by_even_width(self):
        actual = self._callFUT(u'a', 4)
        self.assertEqual(u' a  ', actual)

    def test__multi_width_character_by_odd_width(self):
        actual = self._callFUT(u'中', 3)
        self.assertEqual(u'中 ', actual)

    def test__multi_width_character_by_even_width(self):
        actual = self._callFUT(u'中', 4)
        self.assertEqual(u' 中 ', actual)
