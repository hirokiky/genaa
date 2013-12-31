import unittest


class TestMapping(unittest.TestCase):
    def _getTarget(self):
        from genaa.mapping import Mapping
        return Mapping

    def _makeOne(self, *args, **kwargs):
        return self._getTarget()(*args, **kwargs)

    def test__iter(self):
        target = self._makeOne(['01',
                                '23'])
        actual = iter(target)
        actual_first = actual.__next__()
        actual_second = actual.__next__()
        actual_third = actual.__next__()
        actual_fourth = actual.__next__()
        self.assertRaises(StopIteration, actual.__next__)

        self.assertEqual('0', actual_first.value)
        self.assertEqual(0, actual_first.coordinate.x)
        self.assertEqual(0, actual_first.coordinate.y)
        self.assertEqual('1', actual_second.value)
        self.assertEqual(1, actual_second.coordinate.x)
        self.assertEqual(0, actual_second.coordinate.y)
        self.assertEqual('2', actual_third.value)
        self.assertEqual(0, actual_third.coordinate.x)
        self.assertEqual(1, actual_third.coordinate.y)
        self.assertEqual(1, actual_fourth.coordinate.x)
        self.assertEqual(1, actual_fourth.coordinate.y)

    def test__cell_upper(self):
        target = self._makeOne(['01',
                                '23'])
        actual = target.Cell(1, 1).upper

        self.assertEqual('1', actual.value)
        self.assertEqual(1, actual.coordinate.x)
        self.assertEqual(0, actual.coordinate.y)

    def test__cell_right(self):
        target = self._makeOne(['01',
                                '23'])
        actual = target.Cell(0, 0).right

        self.assertEqual('1', actual.value)
        self.assertEqual(1, actual.coordinate.x)
        self.assertEqual(0, actual.coordinate.y)

    def test__cell_lower(self):
        target = self._makeOne(['01',
                                '23'])
        actual = target.Cell(0, 0).lower

        self.assertEqual('2', actual.value)
        self.assertEqual(0, actual.coordinate.x)
        self.assertEqual(1, actual.coordinate.y)

    def test__cell_left(self):
        target = self._makeOne(['01',
                                '23'])
        actual = target.Cell(1, 0).left

        self.assertEqual('0', actual.value)
        self.assertEqual(0, actual.coordinate.x)
        self.assertEqual(0, actual.coordinate.y)

    def test__cell_value_with_too_big_x(self):
        target = self._makeOne(['01',
                                '23',
                                '45'])
        self.assertRaises(IndexError, target.Cell, 3, 0)

    def test__cell_value_with_too_big_y(self):
        target = self._makeOne(['01',
                                '23',
                                '45'])
        self.assertRaises(IndexError, target.Cell, 0, 4)
