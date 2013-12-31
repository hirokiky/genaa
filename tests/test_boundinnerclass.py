"""
http://code.activestate.com/recipes/577070-bound-inner-classes/

Copyright (C) 2010-2011 by Alex Martelli and Larry Hastings

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""
import unittest


class TestBoundInnerClass(unittest.TestCase):
    def test(self):
        from genaa.boundinnerclass import BoundInnerClass, UnboundInnerClass

        class Outer(object):
            @BoundInnerClass
            class Inner(object):
                def __init__(self, outer):
                    self.outer = outer

            @BoundInnerClass
            class SubclassOfInner(Inner.cls):
                def __init__(self, outer):
                    super(Outer.SubclassOfInner, self).__init__()
                    assert self.outer == outer

            @BoundInnerClass
            class SubsubclassOfInner(SubclassOfInner.cls):
                def __init__(self, outer):
                    super(Outer.SubsubclassOfInner, self).__init__()
                    assert self.outer == outer

            @BoundInnerClass
            class Subclass2OfInner(Inner.cls):
                def __init__(self, outer):
                    super(Outer.Subclass2OfInner, self).__init__()
                    assert self.outer == outer

            class RandomUnboundInner(object):
                def __init__(self):
                    super(Outer.RandomUnboundInner, self).__init__()
                    pass

            @BoundInnerClass
            class MultipleInheritanceTest(SubclassOfInner.cls,
                                          RandomUnboundInner,
                                          Subclass2OfInner.cls):
                def __init__(self, outer):
                    super(Outer.MultipleInheritanceTest, self).__init__()
                    assert self.outer == outer

            @UnboundInnerClass
            class UnboundSubclassOfInner(Inner.cls):
                pass

        def tests():
            assert outer.Inner == outer.Inner
            assert isinstance(inner, outer.Inner)
            assert isinstance(inner, Outer.Inner)

            assert isinstance(subclass, Outer.SubclassOfInner)
            assert isinstance(subclass, outer.SubclassOfInner)
            assert isinstance(subclass, Outer.Inner)
            assert isinstance(subclass, outer.Inner)

            assert isinstance(subsubclass, Outer.SubsubclassOfInner)
            assert isinstance(subsubclass, outer.SubsubclassOfInner)
            assert isinstance(subsubclass, Outer.SubclassOfInner)
            assert isinstance(subsubclass, outer.SubclassOfInner)
            assert isinstance(subsubclass, Outer.Inner)
            assert isinstance(subsubclass, outer.Inner)

        import itertools

        for order in itertools.permutations([1, 2, 3]):
            outer = Outer()
            # This strange "for" statement lets us test every possible order of
            # initialization for the "inner" / "subclass" / "subsubclass" objects.
            for which in order:
                if which == 1:
                    inner = outer.Inner()
                elif which == 2:
                    subclass = outer.SubclassOfInner()
                elif which == 3:
                    subsubclass = outer.SubsubclassOfInner()
            tests()

        outer.MultipleInheritanceTest()
        assert outer.MultipleInheritanceTest.mro() == [
            # bound inner class, notice lowercase-o "outer"
            outer.MultipleInheritanceTest,
            # unbound inner class, notice uppercase-o "Outer"
            Outer.MultipleInheritanceTest,
            outer.SubclassOfInner,  # bound
            Outer.SubclassOfInner,  # unbound
            Outer.RandomUnboundInner,  # etc.
            outer.Subclass2OfInner,
            Outer.Subclass2OfInner,
            outer.Inner,
            Outer.Inner,
            object
        ]

        outer.UnboundSubclassOfInner()
        assert outer.UnboundSubclassOfInner.mro() == [
            outer.UnboundSubclassOfInner,
            Outer.UnboundSubclassOfInner,
            outer.Inner,
            Outer.Inner,
            object
        ]

        class InnerChild(outer.Inner):
            pass

        inner_child = InnerChild()

        assert isinstance(inner_child, Outer.Inner)
        assert isinstance(inner_child, InnerChild)
        assert isinstance(inner_child, outer.Inner)
