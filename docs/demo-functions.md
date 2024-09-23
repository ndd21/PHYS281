---
title: Python functions
authors:
    - Matthew Pitkin
date: 2020-09-24
---

# Functions

<iframe width="560" height="315" src="https://www.youtube.com/embed/PG7MgQnWWIc" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

If you have a piece of code that does a particular job and you need to reuse it multiple times it is
useful to define it as a [function](glossary.md#function).

To define a function you use the [`def`](https://www.w3schools.com/python/ref_keyword_def.asp)
[keyword](glossary.md#keyword) followed by the name you want to give the function, followed by brackets containing any
[arguments](glossary.md#argument) that the function takes. The definition line should be finished with a colon `:`. The
function contents then follow, with indents at the start of the line defining code that is within
the function. E.g.,

```python
# define a function
def my_function(variable1, variable2):
    # contents of a function must be indented
    print(variable1, variable2)

# define variables (back "outside" of the function)
a = "Hello"
b = "world!"

# use (or "call") the function with the two variables a and b
my_function(a, b)
Hello world!
```

The function name must start with an upper or lowercase letter, but can then contain any letters,
numbers or the underscore `_` character. It cannot contain spaces or other characters. It is useful
if the function name is descriptive of what the function does. Some fairly common ways of defining
function names are to split multiple descriptive words using an underscore, or use [camel
case](https://en.wikipedia.org/wiki/Camel_case) (having words together, but starting each with a
capital letter), e.g.,

```python
def add_two_numbers(a, b):
    c = a + b
    return c

# use the function
num = add_two_numbers(1, 2)
print(num)
3
```

```python
def countToTen():
    # indent the function
    for i in range(1, 11):
        # indent the for loop within the function
        print(i)

# use the function
countToTen()
1
2
3
4
5
6
7
8
9
10
```

## Function arguments

In the above examples there are some functions that take [arguments](glossary.md#argument), i.e., variables that are
passed to them that they then use. In the function definition each variable within the brackets is
separated by a comma.

!!! note
    The name of the variable used in the function definition is what that variable will be known as
    *within* the function even if the variable passed to the function has a different name.

As with function names, it is useful for variable names to be descriptive. You can have as many
arguments to a function as you want, including no arguments at all!

```python
# a function with no arguments
def PiratePete():
    print("Aarrrrrrrr! Where's me treasure.")

# use the function (remember the brackets)
PiratePete()
Aarrrrrrrr! Where's me treasure.
```

!!! note
    Notice that when using the function, even if it takes no arguments, you need to include the
    brackets.

```python
# a function with two arguments
def full_name(firstname, surname):
    name = firstname + " " + surname
    return name

myname = full_name("Joe", "Bloggs")
print(myname)
Joe Bloggs
```

```python
# a function with lots of arguments
def sum_many_numbers(a, b, c, d, e, f, g, h, i, j, k):
    total = sum([a, b, c, d, e, f, g, h, i, j, k])
    return total

total = sum_many_numbers(2, 3, 1, 5, 6, 1, 3, 4, 9, 7)
TypeError: sum_many_numbers() missing 1 required positional argument: 'k'

total = sum_many_numbers(2, 3, 1, 5, 6, 1, 3, 4, 9, 7, 1)
print(total)
42
```

This style of argument is known as a "positional" argument. This means that when you pass values to
the function their order (or position) matters. Positional arguments are always *all* required when
you use the function, i.e., you cannot leave any out when calling the function.

It is best not to have too many arguments or you can lose track of them. If you do require lots of
inputs to a function it can be useful to group them and instead define the function to take a single
variable that has a type such as a list or dictionary.

!!! note
    You can use the names of positional arguments (see [keyword arguments
    below](#keyword-arguments)) when parsing values to a function if you want, and they can then
    be passed in any order:

    ```python
    def hey_there(firstname, lastname):
        print(f"Hello {firstname} {lastname}")
    
    hey_there(lastname="Pitkin", firstname="Matt")
    Hello Matt Pitkin
    ```

### Keyword arguments

As well as positional arguments, you can define a function to be passed *keyword* arguments. With
these you pass a variable to a function using a specific "key" word that is then used as that
variable's name within the function. Keyword arguments and defined in the function definition using
a `keyword=value` pair.

Unlike positional arguments, you do not have to call the function using all of (or even any of) the
keywords. However, this means that when defining a function with keyword arguments you must give
them default values that will be used if they are not explicitly set.

```python
# a function with one positional argument and two keyword arguments
def in_range(value, minimum=-100, maximum=100):
    # return True if value is within minimum and maximum
    return minimum < value < maximum

# use function without keywords (i.e., using defaults)
print(in_range(20))
True

# set minimum value using the "minimum" keyword
print(in_range(12, minimum=15))
False

# use both minimum and maximum keywords
lower = 34
upper = 90
print(in_range(56, minimum=lower, maximum=upper))
True
```

You do not have to pass keyword arguments in the same order that they come in the function
definition:

```python
print(in_range(99, maximum=lower, minimum=upper))
False
```

!!! note
    Sometimes you might see code where the user has given the variable being passed to a
    keyword argument the same name as the keyword argument itself, e.g.:

    ```python
    minimum = 12
    maximum = 100
    is_in_range = in_range(34, minimum=minimum, maximum=maximum)
    ```

    While this may look a bit confusing it is perfectly valid.

## Returning values

Many of the above example use the [`print`](demo-built-in-functions.md#print) [built-in](glossary.md#built-in)
function to print a message to the screen. However, you cannot then *use* the output of the function
if it just prints it, e.g., if you had a function that calculated the sine of an angle and it just
prints it to the screen it would be fine if that is all you ever used it for, but if you wanted to
use that output as part of a larger equation it would not be much use.

Most functions should return something to the user. This returned value can be assigned to a
variable that can then be used later in the code. To do this the
[`return`](https://www.w3schools.com/python/ref_keyword_return.asp) keyword is used within the
function definition. As well as returning a variable from the function it also tells the function to
exit, i.e., there should not be code after the return (unless you're using it in a conditional
statement) as it will not get run.

```python
def add_two_numbers(a, b):
    # add the two input arguments
    c = a + b
    
    # return the result
    return c

# use the function and assign the output to a variable called result
result = add_two_numbers(3, 5)

# use the "result" variable
print(result + 10)
18
```

### Multiple outputs

The returned item can be any Python object, but you can explicitly return multiple variables by
separating them with commas in the `return` statement:

```python
def sum_and_product(a, b):
    totalsum = a + b
    totalproduct = a * b

    # return both values
    return totalsum, totalproduct

# call the function and assign the answers to two variables
sumres, prodres = sum_and_product(5, 10)
print(sumres, prodres)
15 50

# return them as a tuple
result = sum_and_product(12, 8)
print(result)
(20, 96)
```

The results are returned with a Python tuple object.

## Functions as variables

Like everything within Python function are themselves objects. So, you can create a variable out of
a function by omitting the bracket during the function call:

```python
def sing_a_rainbow(forwards=True):
    colours = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
    if forwards:
        print(" and ".join(colours[:4]) + ", " + " and ".join(colours[4:]))
    else:
        print(" and ".join(colours[::-1][:4]) + ", " + " and ".join(colours[::-1][4:]))

# create a variable from the function (note the lack of brackets)
song = sing_a_rainbow
print(song)
<function sing_a_rainbow at 0x7f9254c7f840>

# call the function using the new variable
song()
red and yellow and pink and green, purple and orange and blue

# or
song(forwards=False)
blue and orange and purple and green, pink and yellow and red
```

This means you can easily pass functions as arguments to other functions:

```python
def CanISing(aSong, forwards=True):
    # call the function aSong
    aSong(forwards=forwards)
    print("I can sing a rainbow too!")

song = sing_a_rainbow
CanISing(song)
red and yellow and pink and green, purple and orange and blue
I can sing a rainbow too!
```

## Variable scope

A variable's scope, or [nested scope](https://docs.python.org/3/glossary.html#term-nested-scope),
relates to where in a code a particular variable is recognised. It is easiest to demonstrate this
with an example:

```python
# a variable that can be recognised/used anywhere within the script
variable1 = 1

def testfunc1(arg1):
    # a variable that can be used anywhere within testfunc1, but not at lower levels
    variable2 = arg1 * variable1  # using variable1

    def testfunc2(arg2):
        # a variable that can be used anywhere within testfunc2, but not at lower levels
        variable3 = variable2 + arg2  # using variable2
```

Here, we see that a variable (`variable1`) defined at the lowest level, i.e., not indented, can be
recognised and used anywhere within a code.

A variable defined within a function (or class), e.g., `variable2`, can be used anywhere within that
function, but not at lower levels. I.e., its "scope" is limited to its indented level and higher.

It is worth noting that you can use the same variable name, without clashing, within different
scopes, e.g.:

```python
x = 2

def myfunc(y):
    # re-use variable name x, but within this scope
    x = 2 * y
    return x

z = myfunc(3)
print(z)
6

# x in the outer scope shouldn't change
print(x)
2
```

If you do this, then you cannot use the variable `x` from the outer most scope within the inner
scope.

!!! tip
    If you want to use a value within a function it is best practice to pass it as an argument
    rather than rely on it having an appropriate scope.

## Unknown numbers of keyword arguments

!!! question
    What if your function calls another function that takes in multiple keyword arguments. Does your
    function then have to be defined with all those keyword arguments too?

    ```python
    def somefunc(firstname="Default", lastname="Name"):
        # do something with args...
        return f"{firstname} {lastname}"

    # another function that uses somefunc
    def anotherfunc(message="Hello", firstname="Default", lastname="Name"):
        # we've had to define this function to take firstname and last name as well,
        # and redo their default values too

        # use somefunc
        output = somefunc(firstname=firstname, lastname=lastname)

        return f"{message} {output}"
    ```

There are a couple of ways to make this slightly simpler, both of which use the ability to "unpack"
a dictionary.

A function can be defined to take an argument named `**kwargs`. This is special syntax that means
that when you use the function you can pass it any number of keyword arguments. `**kwargs` must be
the final argument in your function definition, but you can have other positional and explicit
keyword arguments before it.

Within the function `kwargs` (without the preceding two asterisks) is just a Python dictionary
containing the keywords and their values as key-value pairs.

If you know that you are only ever going to pass the additional keywords `"firstname"` and `"lastname"`
to `anotherfunc` then you could do:

```python
def anotherfunc(message="Hello", **kwargs):
    print(kwargs)  # print statement is just for show here

    # use somefunc
    output = somefunc(**kwargs)

    return f"{message} {output}"

print(anotherfunc(firstname="Matt", lastname="Pitkin"))
{'lastname': 'Pitkin', 'firstname': 'Matt'}
Hello Matt Pitkin
```

By passing `**kwargs` to `somefunc` it "unpacks" the dictionary, so that essentially `{'lastname':
'Pitkin', 'firstname': 'Matt'}` becomes `lastname="Pitkin", firstname="Matt"` when input into
function.  If you did not supply either `firstname` or `lastname` to `anotherfunc` then the default
values defined in `somefunc` would be used.

If there are other keyword arguments that you could pass to `anotherfunc` then trying to pass them
to `somefunc` will not work:

```python
print(anotherfunc(firstname="Matt", lastname="Pitkin", random="blah"))
{'random': 'blah', 'lastname': 'Pitkin', 'firstname': 'Matt'}
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-8-cf7c1c75bd94> in <module>()
----> 1 print(anotherfunc(firstname="Matt", lastname="Pitkin", random="blah"))

<ipython-input-6-b382a5e46b0e> in anotherfunc(message, **kwargs)
      3 
      4     # use somefunc
----> 5     output = somefunc(**kwargs)
      6 
      7     return f"{message} {output}"

TypeError: somefunc() got an unexpected keyword argument 'random'
```

So, alternatively you could have:

```python
def anotherfunc(message="Hello", **kwargs):
    print(kwargs)  # print statement is just for show here

    # only get keyword args required for somefunc
    somefunckwargs = {}
    if "firstname" in kwargs:
        somefunckwargs["firstname"] = kwargs.pop("firstname")
    if "lastname" in kwargs:
        somefunckwargs["lastname"] = kwargs.pop("lastname")

    # use somefunc, but unpacking somefunckwargs
    output = somefunc(**somefunckwargs)

    return f"{message} {output}"
```

There is similar unpacking for positional arguments using the `*args` syntax in the function
definition, but it is generally safer to use keyword arguments.

## Documenting functions

The above examples are lacking one key feature: Documentation! It is very good practice to document
your code. This helps you and others know what your code is supposed to do. The documentation of a
function should briefly describe what it does, list its arguments, and state what it returns. We
will demonstrate this using a couple of the above examples.

### Example 1

```python
def sum_and_product(a, b):
    """
    Calculate the sum and product of two numbers.

    Parameters
    ----------
    a: float
        A floating point number
    b: float
        A floating point number

    Returns
    -------
    sum, product: tuple
        The resulting sum and product
    """

    totalsum = a + b
    totalproduct = a * b

    # return both values
    return totalsum, totalproduct
```

The text between the `"""`'s is known as a "docstring". In IPython you can access a function's
docstring using `?`, e.g.,

```python
sum_and_product?

Signature: sum_and_product(a, b)
Docstring:
Calculate the sum and product of two numbers.

Parameters
----------
a: float
    A floating point number
b: float
    A floating point number

Returns
-------
sum, product: tuple
    The resulting sum and product
File:      ~/repositories/<ipython-input-27-b49e20c31d46>
Type:      function

```

!!! note
    There are various styles of docstrings. The above example, and others in these notes, use the
    [numpydoc](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) style. But
    others are available. The best advice is to pick one and be consistent when using it.

    As well as the *docstring* you should liberally comment your code using comment lines starting
    with `#`. Using descriptive variable names and leaving blank space lines between less closely
    related code blocks will also help with code readability.

### Example 2

```python
def in_range(value, minimum=-100, maximum=100):
    """
    Check whether a given value is within a given range, excluding the limits
    of the range.

    Parameters
    ----------
    value: (int, float, required)
        The value for checking
    minimum: (int, float)
        The lower limit of the range (defaults to -100).
    maximum: (int, float)
        The upper limit of the range (defaults to 100).
    """

    # return True if value is within minimum and maximum
    return minimum < value < maximum
```

### Type hinting

When defining a function you do not need to specify the [type](glossary.md#type) of each argument. When writing a
docstring you should however let the user know what type of object each argument should be. Another
way of doing this is to use ["type-hints"](https://docs.python.org/3/library/typing.html). This is
way of "hinting" at what type each argument should be in the function definition. If we take the
examples above, we could have:

```python
# use Tuple to show that the returned value is a tuple
from typing import Tuple

def sum_and_product(a: float, b: float) -> Tuple(float, float):
    """
    Calculate the sum and product of two numbers.

    Parameters
    ----------
    a: float
        A floating point number
    b: float
        A floating point number

    Returns
    -------
    sum, product: tuple
        The resulting sum and product
    """

    totalsum = a + b
    totalproduct = a * b

    # return both values
    return totalsum, totalproduct
```

or

```python
# use Union to define multiple allowed types
from typing import Union

def in_range(value: Union[float, int], minimum: Union[float, int] = -100, maximum: Union[float, int] = 100) -> bool:
    """
    Check whether a given value is within a given range, excluding the limits
    of the range.

    Parameters
    ----------
    value: (int, float, required)
        The value for checking
    minimum: (int, float)
        The lower limit of the range (defaults to -100).
    maximum: (int, float)
        The upper limit of the range (defaults to 100).
    """

    # return True if value is within minimum and maximum
    return minimum < value < maximum
```

!!! note
    Type hints are purely for documentation purposes. Python will not check that input arguments
    are actually of the "correct" type unless you explicitly do it within the function (see
    [here](demo-error-checking.md#adding-exception-handling-to-code) for an example).