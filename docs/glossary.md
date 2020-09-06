Here is a glossary of commonly used terms within these notes. For a more complete glossary see the
set provided in the Python documentation [here](https://docs.python.org/3/glossary.html) (any
descriptions in quotation marks are lifted directly from that page).

## `%`

The percent sign is used for [modular arithmetic](https://en.wikipedia.org/wiki/Modular_arithmetic),
i.e., it returns the integer remainder after division of one number by another. E.g., `10 % 3` gives
`1`.

## `*`

The multiplication [operator](#operator), i.e., used for getting the product of two values/objects.
An asterisk is used rather than the standard cross.

## `**`

The exponentation [operator](#operator), i.e., used for raising a value to the power of an exponent.
E.g., in `x = 2 ** 5` the value of 2 is raised to the power of 5. Integer or floating point numbers
can be used for both the base and exponent.

## `+`

The addition [operator](#operator), i.e., used for getting the sum of two values/objects.

## `-`

The subtraction [operator](#operator), i.e., used for getting the different beteween two
values/objects.

## `/`

The division [operator](#operator), i.e., used for getting the quotient of two values/objects.

## `@`

The "at" symbol has two uses. It can be used as an operator to perform [matrix
multiplication](https://en.wikipedia.org/wiki/Matrix_multiplication). Alternatively, it is used when
defining a [decorator](#decorator) function wrapping another function.

## Argument

An argument is a variable or value that is passed to a function, so that it can be used within the
function.

## Attribute

An attribute is ["*A value associated with an object which is referenced by name using dotted
expressions. For example, if an object `o` has an attribute `a` it would be referenced as
`o.a`*"](https://docs.python.org/3/glossary.html#term-attribute). Attributes can be variables within
a class ([data attributes](#data-attribute)) or methods.

## Boolean

A data type that can take one of two possible values, "True" or "False", which can be used when
performing [Boolean algebra](https://en.wikipedia.org/wiki/Boolean_algebra), i.e., evaluating
logical expressions. In Python, Boolean variables have the [type](#type) "`bool`".

## Built-in

Something, for example a function or module, that is defined within any Python installation and
is therefore available to use in any Python code.

## Child

A class that inherits attributes from a [parent](#parent) class, sometimes known as a subclass.

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

## Command prompt

The line in a [terminal](#terminal) into which you type a command. In a Python session, the command
prompt line will start with `>>>` and contain a flashing cursor.

## Data attribute

This is a class [attribute](#attribute) that refers to a data variable within the class.

## Decorator

A decorator is ["*A function returning another
function*"](https://docs.python.org/3/glossary.html#term-decorator). To define a function that is
wrapped in another "decorator" function, the line before the function definition should contain
`@decoratorname`, where `decoratorname` is the name of the decorating function. 

## File extension

This is the end part of a file's name, after the full stop, that defines type of file that it is.
For example, in `myscript.py` the file extension is `py` and shows this is a Python file, or in
`mydocument.docx` the file extension `docx` shows this is a Microsoft Word document.

## float

A class for defining a [floating point number](#floating-point-number). Python automatically
recognises variables set with numbers containing decimal places or exponential notation to be
floating point numbers, e.g., in `y = -9.7` the variable `y` will be a `float` type, which is
equivalent to explicity saying `y = float(-9.7)`.

## Floating point number

A [floating point](https://en.wikipedia.org/wiki/Floating-point_arithmetic) number is any real
non-integer number. The "floating point" refers to the decimal point in the number, which can
"float", i.e., be placed anywhere between the other digits in the number.

## Function

A function is a piece of code that can take in variable [arguments](#argument), perform some
operations, and return an output. In Python, functions are defined using the `def`
[keyword](#keyword).

## Function attribute

This is a class attribute that refers to a function (also known as a [class method](#class-method)).

## Immutable

An object that cannot be changed after it is created. The opposite is something that is
[mutable](#mutable).

## Indent

Using [whitespace](#whitespace) (a series of spaces or tabs) to place a code block away from the
left hand edge of the screen.

## Index

The location of a value within an array-like object, e.g., a list. Indices start at 0 for the
location of the first value, and end at one less than the length of the object.

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

## Method

In Python, a method is how a [function](#function) within a class is referred to.

## Mutable

An object that is changeable after created. The opposite is something that is
[immutable](#immutable).

## Object

In Python, object's are the building blocks of a code; everything is an object! They can contain
data (variables) and ways of manipulating data (functions). Objects have a type which is defined
using their class. Generally, any [instance of a class](#class-instance) is an object.

## Operator

An operator generally refers to one of the mathematical [binary
operators](https://en.wikipedia.org/wiki/Binary_operation) of addition `+`, subtraction `-`,
multiplication `*`, and division `/`, used in [elementary
arithmetic](https://en.wikipedia.org/wiki/Elementary_arithmetic).

## Parent

A class who's attributes will be inherited by a new [child](#child) class. This is sometimes known as a
superclass.

## Positional argument

A positional argument to a function is an [argument](#argument) defined by a name without the equals
sign, e.g., in `def func(a, b):` both `a` and `b` are positional arguments. When using the function
the positional arguments must be passed in the order that they are given in the function definition.
They must come before any [keyword arguments](#keyword-argument).

## Script

A script is a file containing code that is generally used to perform just one job and is standalone
(i.e., it can be run on its own without having to be run by a different code). A Python script file
has the [file extension](#file-extension) `py`.

## String

In programming a string generally refers to a [variable](#variable) type that holds some text, i.e.,
a series of alphanumerical characters. In Python, strings are defined by text enclosed within
apostrophes, quotation marks, or a series of three apostrophes/quotation marks, e.g., `x = 'Hello'`,
`x = "Hello"` and `x = """Hello"""` are all equivalent ways of defining a string.

## subclass

A synonym for a [child](#child) class.

## superclass

A synonym for a [parent](#parent) class.

## Terminal

A text-based window for running commands via a command-line prompt. In Windows, a common terminal
programme is
[PowerShell](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/powershell).

## Type

In Python, [variables](#variable) have a type, which is the *kind* of thing (e.g., an integer or a
[string](#string)) that the variable represents as defined by its [class](#class). Often "type" and
"class" will be used interchangeably.

## Variable

A variable in Python is a named object (or named class instance), e.g., in `x = 2.9` a variable
called `x` has been created that pointed to the `float` number object `2.9`. 

## Whitespace

Spaces ++space++, tabs ++tab++ and carriage returns ++return++/new lines within a document or string
and known as [whitespace](https://en.wikipedia.org/wiki/Whitespace_character).