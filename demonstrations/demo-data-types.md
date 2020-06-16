# Basic data types

In code you can define **variables** and these have a **type**, where the type is the kind of
*thing* that the variable represents. For example, a variable might hold an integer number, or a set
of alphanumeric values (known as a string).

* a **variable** is any object that you create in a code, e.g., in `x = 2` I have defined a
  variable called `x`, which can be reused later in the code.

> Note:  Variable names must start with a letter, but can then contain numbers, hyphens or
> underscores. Variable names are case sensitive, i.e., `a = 2` and `A = 2` are difference
> variables. It is useful to have descriptive variable names.

Some languages have *static typing*, where you must explicitly tell the code what the variable's type
is. In the `C` language you would have define a variable that hold an integer with, e.g.,

```C
int myvariable = 2;
```

Python is a ["duck typing"](https://en.wikipedia.org/wiki/Duck_typing) language - "*If it walks like
a duck and it quacks like a duck, then it must be a duck*". It will work out the type for basic data
types by what they *look* like:

```python
x = 5
type(x)
<class 'int'>
```

It has determined that the variable `x` is of the integer (or `int`) type. In this example `type()`
is a built-in Python function that returns the type of a variable.

> Note: everything in Python is an **object** (hence *object oriented programming*, or OOP). In OOP
> an object is a thing that contain data in the form of variables and/or functions to act on that
> data. All variables are objects and therefore the **type** refers to the "type" of object. "Type"
> is sometimes used interchangeably with "**class**", where a class this the thing that defines a
> type.

The main basic data types (in Python and many languages) are:

* `int`: represents an positive or negative integer number
* `float`: represents a "floating point" number, i.e., a non-integer number.
* `str`: represents some alphanumeric text
* `bool`: represents True or False 

```python
# defining an integer
myInteger = 2

# defining a float (note the decimal point)
myFloat = -59.87534

# define a string
myString = "Hello"

# define a boolean
myBool = True
```

The basic data types are objects, and have **attributes** and **methods**:

* **attributes** are variables that are contained within an object.
* **methods** are functions within an object.

Examples:

```
x = 1
# int and float objects contain real and imag attributes
x.real
1
```

```
y = 1.5
# floats contain an is_integer() method
y.is_integer()
False

# the float can be returned as an integer ratio
y.as_integer_ratio()
(3, 2)
```

## Strings

Strings can be defined in three different, but equivalent, ways:

```
z1 = "Hello"
z2 = 'Hello'
z3 = """Hello"""
```

Strings have a lot of [methods](https://www.w3schools.com/python/python_ref_string.asp), for example:

```
z = "Hello"
# show the string in upper case
z.upper()
'HELLO'
# replace l's with x's
z.replace("l", "x")
'Hexxo'
```