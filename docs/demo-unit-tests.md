---
title: Code testing
authors:
    - Matthew Pitkin
date: 2020-09-23
---

# Code testing

<iframe width="560" height="315" src="https://www.youtube.com/embed/YiLVUG0KCB0" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

A code will do what you tell it. So, if you make a mistake in your code it will run with that
mistake. Therefore it will probably not do what you expected it to do, i.e., it will give an
obviously wrong answer or fail. A more serious case is when it does not fail, but returns an answer
that is subtly, but not obviously, wrong.

To avoid this it is worth testing your code to make sure it definitely does as expected.

## Unit testing

Unit testing is the process of testing small components of your code in well defined situations with
known answers. Units test should be used for testing functions or class methods, but not for testing
chunks of a script.

Breaking down the tests is generally better than trying to do a global test of your entire code. It is
trickier to find the source of any problem if you have to run through your whole code each time.

The units test should be performed in a script of their own, importing any functions or classes from
the script/module to be tested. This means that each time you change your script/module you can run
the test script and check that everything still works. This also means you can fix problems as they arise rather than having to wait until you have finished writing your entire code.

Here we will show a basic example of unit testing. The examples will be rather contrived and simplistic, but give a idea of what to do.

Suppose you have a Python file, called `shapes.py`, containing the following function and class
definitions:

```python
def triangle_area(base, height):
    """
    Calculate and return the area of a triangle given its base and height.
    """

    return 0.5 * base * height


def circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    """

    from math import pi

    # spot the "mistake"!
    return pi * (0.7 * radius) ** 2


class shape:
    """
    Class to hold a shape.

    Parameters
    ----------
    name: str
        The name of the shape.
    """
    
    def __init__(self, name, **kwargs):
        self.name = name
        self.parameters = kwargs

    def area(self):
        """
        Calculate the area of the shape.
        """

        if self.name.lower() == "triangle":
            if "base" in self.parameters and "height" in self.parameters:
                return triangle_area(
                    self.parameters["base"], self.parameters["height"]
                )
            else:
                # A triangle must be supplied with a base and height
                return None
        elif self.name.lower() == "circle":
            if "radius" in self.parameters:
                return circle_area(self.parameters["radius"])
            else:
                # A circle must be supplied with a radius
                return None
        else:
            return None
```

We could then write a test script (preferably writing in conjunction with our main code file, i.e.,
just after we have defined each function) that checks these functions/classes with known inputs and
pre-calculated expected results, e.g., areas. We could have a file called `test_shapes.py`
containing the following:

```python
import shapes

# test the triangle area function
base = 2.0
height = 2.0
trianswer = 2.0  # the known answer
area = shapes.triangle_area(base, height)
if area != trianswer:  # check the answer
    print(
        "The triangle_area function is not working!\n"
        "\tReturned result {}\n"
        "\tExpected result{}".format(area, trianswer)
    )

# test the circle area function
radius = 3.0
circanswer = 28.274333882308138  # the known answer pi * radius ** 2
area = shapes.circle_area(radius)
if abs(area - circanswer) > 1e-14:  # check the absolute difference is small
    print(
        "The circle_area function is not working!\n"
        "\tReturned result {}\n"
        "\tExpected result{}".format(area, circanswer)
    )

# test the shape class
square = shapes.shape("square")

# check the name attribute is correctly set
if square.name != "square":
    print("shape class name attribute is incorrect: {}".format(square.name))

# check square (which currently has no area function defined) returns None for area
if square.area() is not None:
    print("Unrecognised shape returning non-None area!")

# check triangle area (within shape class) returns None if base or height aren't set
for bh in [{"base": 2.0}, {"height": 2.0}]:
    triangle = shapes.shape("triangle", **bh)
    if triangle.area() is not None:
        print("Non-None area returned for triangle without {}".format(list(bh.keys())[0]))

# re-check for correct triangle area when used within class
triangle = shapes.shape("triangle", base=2.0, height=2.0)
if triangle.area() != trianswer:  # check the answer
    print(
        "The triangle_area function within shape is not working!\n"
        "\tReturned result {}\n"
        "\tExpected result {}".format(triangle.area(), trianswer)
    )

# check circle area (within shape class) return None is radius is not set
circle = shapes.shape("circle")
if circle.area() is not None:
    print("Non-None area returned for circle without radius")

# re-check for correct circle area when used within class
circle = shapes.shape("circle", radius=3.0)
if (circle.area() - circanswer) > 1e-14:  # check the answer
    print(
        "The circle_area function within shape is not working!\n"
        "\tReturned result {}\n"
        "\tExpected result {}".format(circle.area(), circanswer)
    )
```

You could then run:

```bash
python test_shapes.py
The circle_area function is not working!
	Returned result 13.854423602330982
	Expected result 28.274333882308138
```

Here we can see that our `circle_area` function had a mistake, which we can then fix.

### pytest

There is a third-party Python package called [`pytest`](https://docs.pytest.org/en/stable/), which
is useful for running unit tests. It should be available within the `base` Anaconda environment. It
provides a format for writing the test script and a way of running that test script. At its most
basic, you write each test as a function named `test_sometestname()` (replacing `sometestname` with
what you want) and use the `assert` keyword when doing the comparisons for the tests (in this case
the "assertion" is that the returned values is the same as the expected value). Converting the above
script into this format, and calling it `test_shape_pytest.py`, would give, e.g.,:

```python
import shapes

# test the triangle area function
def test_triangle_area():
    base = 2.0
    height = 2.0
    trianswer = 2.0  # the known answer
    area = shapes.triangle_area(base, height)

    # check the answer
    assert area == trianswer, "The triangle_area function is not working!"


# test the circle area function
def test_circle_area():
    radius = 3.0
    circanswer = 28.274333882308138  # the known answer pi * radius ** 2
    area = shapes.circle_area(radius)
    assert abs(area - circanswer) < 1e-14, "The circle_area function is not working!\n"


# test the shape class
def test_shape():
    square = shapes.shape("square")

    # check the name attribute is correctly set
    assert square.name == "square", "shape class name attribute is incorrect"

    # check square (which currently has no area function defined) returns None for area
    assert square.area() is None, "Unrecognised shape returning non-None area!"


# check triangle area (within shape class) returns None if base or height aren't set
def test_triangle_within_shape():
    for bh in [{"base": 2.0}, {"height": 2.0}]:
        triangle = shapes.shape("triangle", **bh)
        assert triangle.area() is None, "Non-None area returned for triangle"

    # re-check for correct triangle area when used within class
    triangle = shapes.shape("triangle", base=2.0, height=2.0)
    trianswer = 2.0
    assert triangle.area() == trianswer, "The triangle_area function within shape is not working!"


# check circle area (within shape class) return None is radius is not set
def test_circle_within_shape():
    circle = shapes.shape("circle")
    assert circle.area() is None, "Non-None area returned for circle without radius"

    # re-check for correct circle area when used within class
    circle = shapes.shape("circle", radius=3.0)
    circanswer = 28.274333882308138
    assert (circle.area() - circanswer) < 1e-14, "The circle_area function within shape is not working!"
```

This could then be run using `pytest` with:

```bash
pytest test_shape_pytest.py
============================= test session starts ==============================
platform linux -- Python 3.8.5, pytest-6.0.2, py-1.9.0, pluggy-0.13.1
rootdir: /home/matthew/phys281
collected 5 items                                                              

test_shape_pytest.py .F...                                               [100%]

=================================== FAILURES ===================================
_______________________________ test_circle_area _______________________________

    def test_circle_area():
        radius = 3.0
        circanswer = 28.274333882308138  # the known answer pi * radius ** 2
        area = shapes.circle_area(radius)
>       assert abs(area - circanswer) < 1e-14, "The circle_area function is not working!\n"
E       AssertionError: The circle_area function is not working!
E         
E       assert 14.419910279977156 < 1e-14
E        +  where 14.419910279977156 = abs((13.854423602330982 - 28.274333882308138))

test_shape_pytest.py:19: AssertionError
=========================== short test summary info ============================
FAILED test_shape_pytest.py::test_circle_area - AssertionError: The circle_ar...
========================= 1 failed, 4 passed in 0.19s ==========================
```

It looks like we've not fixed that `circle_area` function yet!
