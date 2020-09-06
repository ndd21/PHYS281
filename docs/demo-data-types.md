# Basic data types

In a code you can define @(variables) and these have a @(type), where the type is the kind of
*thing* that the variable represents. For example, a variable might hold an integer number, or a set
of alphanumeric values (known as a string).

* a variable is the _name_ you give any object that you create in a code, e.g., in `x = 2` I
  have defined a variable called `x`, which can be reused later in the code.

!!! note
    Variable names must start with a letter, but can then contain numbers, hyphens or
    underscores. Variable names are case sensitive, i.e., `a = 2` and `A = 2` are different
    variables. It is useful to have descriptive variable names.

Some languages have *static typing*, where you must explicitly tell the code what the variable's type
is. In the `C` language you would have define a variable that holds an integer with, e.g.,

```C
int myvariable = 2;
```

Python is a ["duck typing"](https://en.wikipedia.org/wiki/Duck_typing) language - "*If it walks like
a duck and it quacks like a duck, then it must be a duck*". It will work out the type for basic data
types by what they "look" like:

```python
x = 5
type(x)
<class 'int'>
```

It has determined that the variable `x` is of the integer (or `int`) type. In this example `type()`
is a built-in Python function that returns the type of a variable.

!!! note
    Everything in Python is an @(object) (hence *object oriented programming*, or OOP). In OOP
    an object is a thing that contain data in the form of variables and/or functions to act on that
    data. All variables are objects and therefore the @(type) refers to the "type" of object.
    "Type" is sometimes used interchangeably with "@(class)", where a class defines a type.

The main basic data types (in Python and many languages) are:

* `int`: represents an positive or negative integer number;
* `float`: represents a "@(floating point number)", i.e., a non-integer number;
* `str`: represents some alphanumeric text, know as a "@(string);
* `bool`: represents a @(boolean) value, i.e., "True" or "False".

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

The basic data types are @(objects), and as such have @(data attributes) and @(methods):

* @(data attributes) are variables that are contained within an object;
* @(methods) are functions within an object.

Examples:

```python
x = 1
# int and float objects contain real and imag attributes
x.real
1
```

```python
y = 1.5
# floats contain an is_integer() method
y.is_integer()
False

# the float can be returned as an integer ratio
y.as_integer_ratio()
(3, 2)
```

!!! note
    Due to being held in a finite amount of computer memory, floating point numbers are not
    exact. They can show loss of precision when including many significant figures, e.g.,:

    ```python
    x = 4.1 - 1.2
    print(x)
    2.8999999999999995
    ```

    The above calculation has produced a number that is very close to, but not quite, `2.9`.
    This can mean that you have to be careful if doing comparisons with float, as:

    ```python
    print(x == 2.9)
    False
    ```

    You might instead do:

    ```python
    print(abs((x - 2.9)/x) < 1e-15)  # difference has very small relative error
    ```

## Strings

@(Strings) can be defined in three different, but equivalent, ways:

```python
z1 = "Hello"
z2 = 'Hello'
z3 = """Hello"""  # you could also use three consecutive apostrophes
```

Strings have a lot of [methods](https://www.w3schools.com/python/python_ref_string.asp), for example:

```python
z = "Hello"
# show the string in upper case
z.upper()
'HELLO'
# replace l's with x's
z.replace("l", "x")
'Hexxo'
```

To join strings together you can just use the addition operator `+`, e.g.,

```python
x = "Hello"
y = " "  # a space
z = "World!"
phrase = x + y + z
print(phrase)
Hello World!
```

### String formatting

The basic Python types have a representation of themselves in a string format. So, for example, if
you define an integer and print it you will see:

```python
x = 34
print(x)
34
```

You can place an object's string representation into another strings using the
[`format()`](https://www.w3schools.com/python/ref_string_format.asp) method. For example:

```python
x = 12
y = 14
z = x + y
print("The sum of {} + {} = {}".format(x, y, z))
The sum of 12 + 14 = 26
```

The `format()` method replaces the curly brackets with the string representations for `x`, `y` and
`z`.

You can have even more control about how numbers are displayed, for example:

```python
x = 12.9627459845
y = 13.9875284843
z = x + y
print("The sum of {0:.2f} + {1:.2f} = {2:.2f}".format(x, y, z))
The sum of 12.96 + 13.99 = 26.95
```

In this case the `0` represents the first argument to `format`, which is followed by the formatting
type `:.2f` that means show a floating point number (`f`) to two decimal places (`.2`).

In Python versions greater than 3.5 there is another way to use string formatting. If you define a
string with an `f` (known as an [f-string](https://www.python.org/dev/peps/pep-0498/)) before the
opening quotes you can use variable names within curly brackets to show their values, e.g.:

```python
firstname = "Matthew"
age = 21

mystring = f"My name is {firstname} and my age is {age}."
print(mystring)
My name is Matthew and my age is 21.
```