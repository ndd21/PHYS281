Here is a glossary of commonly used terms within these notes. For a more complete glossary see the
set provided in the Python documentation [here](https://docs.python.org/3/glossary.html) (any
descriptions in quotation marks are lifted directly from that page).

## Argument

An *argument* is a variable or value that is passed to a function, so that it can be used within the
function.

## Attribute

An attribute is ["*A value associated with an object which is referenced by name using dotted
expressions. For example, if an object `o` has an attribute `a` it would be referenced as
`o.a`*"](https://docs.python.org/3/glossary.html#term-attribute). Attributes can be variables within
a class ([data attributes](#data-attribute)) or methods.

## Class

A class is ["*A template for creating user-defined objects. Class definitions normally contain
method definitions which operate on instances of the
class.*"](https://docs.python.org/3/glossary.html#term-class)

## Class instance

A instance of a class is an object created from a class, e.g., in `x = int(1)` the variable `x` is
an instance of the [`int`](#int) class.

## Class method

A class method is [*"A function which is defined inside a class
body."*](https://docs.python.org/3/glossary.html#term-method)

## Class variable

This is a ["*variable defined in a class and intended to be modified only at class level (i.e., not
in an instance of the class).*"](https://docs.python.org/3/glossary.html#term-class-variable)

## Data attribute

This is a class attribute that refers to a data variable within the class.

## Decorator

A decorator is ["*A function returning another
function*"](https://docs.python.org/3/glossary.html#term-decorator). To define a function that is
wrapped in another "decorator" function, the line before the function definition should contain
`@decoratorname`, where `decoratorname` is the name of the decorating function. 

## float

A class for defining a [floating point number](#floating-point-number). Python automatically
recognises variables set with numbers containing decimal places or exponential notation to be
floating point numbers, e.g., in `y = -9.7` the variable `y` will be a `float` type, which is
equivalent to explicity saying `y = float(-9.7)`.

## Floating point number

A [floating point](https://en.wikipedia.org/wiki/Floating-point_arithmetic) number is any real
non-integer number. The "floating point" refers to the decimal point in the number, which can
"float", i.e., be placed anywhere between the other digits in the number.

## Function attribute

This is a class attribute that refers to a function (also known as a class method).

## Indent

Using [whitespace](#whitespace) (a series of spaces or tabs) to place a code block away from the
left hand edge of the screen.

## int

A class for defining integer numbers. Python automatically recognises variables set with integer
number values to be integers, e.g., in `x = 1` the variable `x` will be an `int` type, which is
equivalent to explicitly saying `x = int(1)`.

## Keyword

In Python there are a set of [reserved
words](https://www.w3schools.com/python/python_ref_keywords.asp) that cannot be used for variable,
function or class names as they already have a defined usage.

## Keyword argument

A keyword argument to a function is an [argument](#argument) defined by a keyword identifier and
value pair separated by an equals sign. The value after the equals sign provides a default value
used within the function if the keyword is not used in the function call, e.g., in `def func(x=2):`
the argument `x` is the keyword and `2` is the default value it takes. Keyword arguments can be
passed to the function in any order provided the keyword identifier is used, if not used then the
arguments must be given in the order in the function definition.

## Object

In Python, object's are the building blocks of a code; everything is an object! They can contain
data (variables) and ways of manipulating data (functions). Objects have a type which is defined
using their class. Generally, any [instance of a class](#class-instance) is an object.

## Positional argument

A positional argument to a function is an [argument](#argument) defined by a name without the equals
sign, e.g., in `def func(a, b):` both `a` and `b` are positional arguments. When using the function
the positional arguments must be passed in the order that they are given in the function definition.
They must come before any [keyword arguments](#keyword-argument).

## Variable

A variable in Python is a named object (or named class instance), e.g., in `x = 2.9` a variable
called `x` has been created that pointed to the `float` number object `2.9`. 

## Whitespace

Spaces ++space++, tabs ++tab++ and carriage returns ++return++/new lines within a document or string
and known as [whitespace](https://en.wikipedia.org/wiki/Whitespace_character).