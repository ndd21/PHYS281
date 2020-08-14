---
title: Python classes
authors:
    - Matthew Pitkin
date: 2020-08-12
---

# Classes

Almost everything in Python is an object. All objects (e.g., named variables, functions) have a
type. An object's type is also known as its
[**class**](https://docs.python.org/3/tutorial/classes.html). A class can also be thought of as a
template for creating an object of that type.

Objects can combine holding data with functionality. Anything that you can access in an object is
known as an **attribute**. Attributes can either be **data attributes** (sometime also known as
class properties or members) or **function attributes** (also known as **class methods**).

A new object class can be defined using the
[`class`](https://www.w3schools.com/python/ref_keyword_class.asp) keyword.

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

For an instance of the class these data attributes can be altered:

```python
electron.mass = 2
print(electron.mass)
2
```

## A class with initialisation

The above class has been created with a fixed set values of the data attributes. Every time an
instance of the class is created the attributes will be the same.

It is often useful to be able to create an instance of a class with a set of user defined values
rather than fixed values. Python classes can have a special method called `__init__` that defines
how the class is initialised and can take in user supplied arguments. In OOP languages like `C++`
the `__init__` method is equivalent to what is called a constructor.

```python
class Particle:
    def __init__(self, name, charge, mass)
        # the initialisation function
        self.name = name
        self.charge = charge
        self.mass = mass
```

Now, creating an instance of a `Particle` class different particles can be created by supplying
their values, e.g.:

```python
electron = Particle("electron", -1.6e-19, 9.1e-31)
proton = Particle("proton", 1.6e-19, 1.7e-27)

for part in [electon, proton]:
    print("{} mass = {}".format(part.name, part.mass))
electron mass = 9.1e-31
proton mass = 1.7e-27
```

The `__init__` method of a class can can have positional and/or keyword arguments, just like any
other function. Using keyword arguments allows the setting of default initialisation values if no
user supplied values are given, e.g.,

```python
class Particle:
    def __init__(self, name="electron", charge=-1.6e-19, mass=9.1e-31):
        # if no values are supplied the default values will be used
        self.name = name
        self.charge = charge
        self.mass = mass

myparticle = Particle()
print(myparticle.name)
electron
```

### `self`

The `__init__` method, and any other regular method defined in a class, takes `self` as its first
argument. But when creating the new object above nothing was passed for `self` (i.e., the brackets
were empty)! When **defining** a class method the method has to have the class instance explicitly
passed to it. This allows that method to access all the class attributes of the current class
instance via `self`. But, when using a method `self` is passed implicitly, i.e., the user does not
have to supply it as it is supplied automatically.

### Special methods

There are a set of [special method names](https://rszalski.github.io/magicmethods/) (sometimes
called "dunder", or magic, methods as they start and end with a double underscore) like `__init__`
that can be defined in a class. These can be used

 * to allow comparisons of objects of specific class
 * define how mathematical operators work on a class
 * access attributes within a class
 * provide representations of class

One particular special method is
[`__str__`](https://thomas-cokelaer.info/blog/2017/12/difference-between-__repr__-and-__str__-in-python/).
This defines how to displayed a class instance as a string, for example if trying to print the
object, e.g.:

```python
class Particle:
    def __init__(self, name="electron", charge=-1.6e-19, mass=9.1e-31):
        # if no values are supplied the default values will be used
        self.name = name
        self.charge = charge
        self.mass = mass

    def __str__(self):
        # a string representing the object
        vowel = self.name[0].lower() in ["a", "e", "i", "o", "u"]
        firstword = "An" if vowel else "A"

        return "{} {} with mass of {} kg and charge of {} C".format(
            firstword, self.name, self.mass, self.charge
        )

myparticle = Particle(name="positron", charge=1.6e-19)
print(myparticle)
A positron with mass of 9.1e-31 kg and charge of 1.6e-19 C
```

A similar method that can be used instead is `__repr__`.

### Adding methods

Methods are defined just like standard functions, but within the class definition. The first
argument that they take must be `self`, so that all other class attributes are available using it.

```python
class Particle:
    def __init__(self, name, charge, mass, spin=None):
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

The `fermion_or_boson` method does not take in any arguments (other than the impicit `self`). A
method that could be added to the particle is one that calculates the [Lorentz
force](https://en.wikipedia.org/wiki/Lorentz_force) on the particle in an electric and magnetic
field:

```python
class Particle:
    def __init__(self, name, charge, mass, spin=None):
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

    def lorentz_force(self, E, B=[0.0, 0.0, 0.0], v=[0.0, 0.0, 0.0]):
        """
        Calculate the Lorentz force on the particle.

        Parameters
        ----------
        E: array
            A vector giving the x, y and z components of the electric field
            (required).
        B: array
            A vector giving the x, y and z components of the magnetic field
            (defaults to zero).
        v: array
            A vector giving the x, y and z components of the particle's
            velocity (defaults to zero)
        """

        if len(E) != 3:
            # check E is the right length
            raise ValueError("E is not the right length")

        F = 3 * [0.0]  # initialise F as zeros
        
        # calculate F = q * (E + v x B)
        F[0] = self.charge * (E[0] + v[1] * B[2] - v[2] * B[1])
        F[1] = self.charge * (E[1] + v[2] * B[0] - v[0] * B[2])
        F[2] = self.charge * (E[2] + v[0] * B[1] - v[1] * B[0])

        return F


electron = Particle("electron", -1.6e-19, 9.1e-31)

# calculate the Lorentz force (forgetting the required positional argument!)
F = electron.lorentz_force()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-23-14143ee08c6d> in <module>
----> 1 F = electron.lorentz_force()

TypeError: lorentz_force() missing 1 required positional argument: 'E'

# try again (with E being the wrong length!)
F = electron.lorentz_force([0.1, 0.2])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-24-966d81233b8b> in <module>
----> 1 F = electron.lorentz_force([0.1, 0.2])

<ipython-input-20-98635895214d> in lorentz_force(self, E, B, v)
     42         if len(E) != 3:
     43             # check E is the right length
---> 44             raise ValueError("E is not the right length")
     45
     46         F = 3 * [0.0]  # initialise F as zeros

ValueError: E is not the right length

# try again!
F = electron.lorentz_force([0.1, 0.2, 0.3])
print(F)
[-1.6e-20, -3.2e-20, -4.8e-20]
```

The `lorentz_force` method above takes one positional argument and two keyword arguments (that give
default values). Any number of positional or keyword arguments could be used.

The `lorentz_force` method could be simplified using Numpy (see [#demo-numpy]).

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

You may want to define a new class that is very similar to an already existing class, but adds new
attributes. Rather than redefining all of the aspects of the existing class in the new class you can
[inherit](https://www.w3schools.com/python/python_inheritance.asp) them from the existing class.

Suppose we have a `Galaxy` class:

```python
class Galaxy:
    """
    A class defining a galaxy.

    Parameters
    ----------
    mass: float
        The galaxy mass (in solar masses)
    distance: float
        The distance (in Mpc)
    type: str
        The type of galaxy, e.g., "spiral"
    name: str
        The galaxy's name. Defaults to None.
    """

    def __init__(self, mass, distance, type, name=None):
        self.mass = mass
        self.distance = distance
        self.type = type
        self.name = name

    def redshift(self, H0=70.0):
        """
        Calculate the redshift using Hubble's law.

        Parameters
        ----------
        H0: float
            Hubble's constant (defaults to 70 km/s/Mpc)
        """

        # recession velocity
        v = H0 * self.distance

        return v / 3e5  # velocity / speed of light (km/s)
```

Now, suppose we want a class specifically for a spiral galaxy, but keeping the attributes of a
`Galaxy`, i.e. `Galaxy` is the **parent** class and `SpiralGalaxy` will be its **child**. We can
create a new class with:

```python
class SpiralGalaxy(Galaxy):  # this is where the Galaxy gets inherited
    """
    A class defining a spiral galaxy.
    """

    def __init__(self, bulge_mass, disc_mass, halo_mass, distance, name=None, barred=False):
        # the special "super" function allows initialisation of the common
        # Galaxy attributes
        super().__init__(bulge_mass + halo_mass + disc_mass, distance, "spiral", name=name)

        # add spiral specific properties
        self.bulge_mass = bulge_mass
        self.disc_mass = disc_mass
        self.halo_mass = halo_mass
        self.barred = barred  # has it got a bar

    def disc_circular_velocity(self, Rd, r):
        """"
        Calculate the contribute to the circular velocity contribution of the
        disc (see Eqn. 1 of astro-ph/9909252).

        Parameters
        ----------
        Rd: float
            The disc scale-length (kpc)
        r: array_like
            A set of positive radial values at which to calculate the velocity (kpc)

        Returns
        -------
        velocity: array_like
            A set of circular velocity values (km/s).
        """

        # import modified Bessel functions from scipy
        from scipy.special import iv, kn
        from math import sqrt 

        disc_mass_si = self.disc_mass * 1.99e30  # disc mass in kg

        velocities = []  # list to hold velocities

        for rval in r:
            x = rval / Rd
            B = iv(0, x / 2) * kn(0, x / 2) - iv(1, x / 2) * kn(1, x / 2)
            G = 6.67e-11  # Newton's gravitational constant
            v = sqrt(0.5 * G * (disc_mass_si / (Rd * 3.086e19)) * x ** 2 * B)
            velocities.append(v / 1e3)  # convert to km/s

        return velocities
```

It we create a `SpiralGalaxy`:

```python
bulge_mass = 3.0e8  # solar masses
disc_mass = 6.0e9
halo_mass = 5.0e10
distance = 0.84  # Mpc
m33 = SpiralGalaxy(bulge_mass, disc_mass, halo_mass, distance, name="M33")
```

we can then use attributes from the `Galaxy` class like:

```python
z = m33.redshift()
print("{}'s redshift is {}".format(m33.name, z))
M33's redshift is 0.000196
```

or use the new attributes:

```python
rs = list(range(1, 16))  # range of distances
Rd = 1.2  # disk scale in kpc
vs = m33.disc_circular_velocity(Rd, rs)

from matplotlib import pyplot as plt
plt.plot(rs, vs)
plt.xlabel("Distance from Galactic centre (kpc)")
plt.ylabel("Circular velocity (km/s)")
plt.show()
```