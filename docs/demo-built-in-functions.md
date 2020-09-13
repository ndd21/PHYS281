# Built-in functions

The are a set of [built-in
functions](https://docs.python.org/3/library/functions.html#built-in-functions) that are a part of
any Python installation, i.e., they can be used and recognised in any Python code. The built-in
function do not have to be imported.

We will describe a few common functions here.

## `float`

The [`float`](https://docs.python.org/3/library/functions.html#float) function creates a @(floating
point number) object from a number or a string, e.g.:

```python
num = float("4.5")  # convert a string containing 4.5 into a float representing 4.5
```

## `int`

The [`int`](https://docs.python.org/3/library/functions.html#int) function creates an integer object
from a number or a string, e.g.:

```python
num = int("3")  # convert a string containing 3 into an int representing 3
```

## `input`

The [`input`](https://docs.python.org/3.8/library/functions.html#input) function allows you to get
user input from the keyboard, e.g.:

```python
name = input("What is your name?")
```

## `len`

The [`len`](https://docs.python.org/3/library/functions.html#len) function returns the length of an
object, such as a list, if this is meaningful for that object, e.g.,:

```python
x = [4, 9, 2, 6]
len(x)
4
```

## `print`

The [`print`](https://docs.python.org/3/library/functions.html#print) function allows you
to print text to the screen, e.g.:

```python
print("Hello")
Hello
```

!!! note
    `print` just prints text to the screen (or to a [file if
    specified](../demo-io/index.html#writing)). It does not return that text to a variable.

## `type`

The [`type`](https://docs.python.org/3/library/functions.html#type) function return the @(type) of a
variable.

```python
type("Hello")
str
```

# Keywords

Along with the built-in functions, there are a set of [reserved
keywords](https://www.w3schools.com/python/python_ref_keywords.asp) in Python that have a specific
meaning and cannot be used for variable or function names.