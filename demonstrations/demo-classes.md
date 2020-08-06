# Classes

Almost everything in Python is an object. All objects (e.g., named variables, functions) have a
type. An object's type is also known as it's
[**class**](https://docs.python.org/3/tutorial/classes.html). A class can also be thought of as a
template for creating an object of that type.

Objects can combine holding data with functionality. Anything that you can access in an object is
known as an **attribute**. Attributes can either be **data attributes** (sometime also known as
class properties or members) or function attributes (alss known as **class methods**).

A new object class can be defined using the [`class`] keyword.

## A simple class

A simple class containing just data attributes can be created using:

```python
class Particle:
    # indents are required to define thing within a class
    name = "electron"
    charge = -1.6e-19  # electric charge in coulombs
    mass = 9.1e-31  # mass in kg
```

An instance of this class can then be created with:

```python
electron = Particle()  # note the brackets are required
```

The data attributes of the object can be accessed using a `.`, e.g.:

```python
print(electron.mass)
9.1e-31
```

## A class with initialisation

The above class has been created with a fixed set values of the data attributes. Every time an
instance of the class is created the attributes will be the same.

It is often useful to be able to create an instance of a class with a set of user defined values
rather than fixed values. Python classes can have a special method called `__init__` that defines
how the class is initialised and can take in user supplied arguments.

```python
class Particle:
    def __init__(self, name, charge, mass)
        # the initialisation function
        self.name = name
        self.charge = charge
        self.mass = mass
```

Now, this method can be used to create different particles by supplying their values, e.g.:

```python
electron = Particle("electron", -1.6e-19, 9.1e-31)
proton = Particle("proton", 1.6e-19, 1.7e-27)

for part in [electon, proton]:
    print("{} mass = {}".format(part.name, part.mass))
electron mass = 9.1e-31
proton mass = 1.7e-27
```

There are a set of special method names (sometimes called "dunder" methods as they start and end
with a double underscore) that can be defined in a class.

### Adding methods

Methods are defined just like standard functions, but within the class definition. The first
argument that they take must be `self`, so that all other class attributes are available using it.

```python
class Particle:
    def __init__(self, name, charge, mass, spin=None)
        # the initialisation function
        self.name = name
        self.charge = charge
        self.mass = mass
        self.spin = spin

    def fermion_or_boson(self):
        """
        Determine if the particle is a fermion or a boson.
        """

        if self.spin is not None:
            if self.spin % 0.5 == 0.0:
                return "fermion"
            elif self.spin % 1.0 == 0.0:
                return "boson"
            else:
                print("Particle is neither a fermion or a boson")
                return None
        else:
            return None
```

Like the data attributes this can then be accessed using a `.`, e.g.:

```python
electron = Particle("electron", -1.6e-19, 9.1e-31, spin=1/2)
print(electron.fermion_or_boson())  # note the brackets when accessing the method
fermion
```

## Static methods

Static methods are functions within a class that can be used without creating a new instance of that
class. As they do not use an instance of the class they do not have access to any of the other class
attributes, i.e., they are standalone and must be supplied with all the variables they required.

Unlike normal methods they do not get passes the `self` argument. The make a method static you use
the [`@staticmethod`](https://docs.python.org/3/library/functions.html#staticmethod)
[decorator](https://docs.python.org/3/glossary.html#term-decorator) on the line above the method
definition, e.g.:

## `classmethod`

A `classmethod`

## Class inheritance