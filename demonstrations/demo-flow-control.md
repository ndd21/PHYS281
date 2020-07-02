# Flow control

When Python runs a script the code is executed from the top to the bottom. However, you might want
to only run certain parts of the code given specific conditions, or you might want to repeat
something multiple times. To do this you can use flow control:

 * `if... elif... else` statements
 * `for` loops
 * `while` loops

# Indenting

In Python the way to specify that you are defining something "inside" a flow control
statement/function/class is by using indenting. Most other languages use parentheses (brackets) of
some sort, but in Python indenting is vital.

Things that are together within the same statement or definition must be indented using whitespace
(regular spaces or tabs) to the same level.

> Tip: Be consistent with your whitespace. It is highly recommended that you use spaces rather than
> tabs. Using four spaces for each level of indentation is considered standard and is recommended.

If you are nesting statements (i.e., flow control within a function definition, or loops within
loops), each statement definition my be further indented.

**Correct examples**

```python
x = True
if x is True:
    # Indented with 4 spaces
    print("x is true!")

def my_function(a):
    # first level of indentation
    x = range(a)
    y = []
    for i in x:
        # second level of indentation
        y.append(i * 2 + 1)

    # back to first level of indenting (i.e., outside the for loop, but still in the function definition)
    return y

# back outside the function definition
b = my_function(10)
print(b)
```

**Incorrect examples**

```python
x = True
if x is True:
# we've forgetten any indentation!
print("x is True")
IndentationError: expected an indented block

if x is True:
  # different indenting levels
  print("x is True")
    print("...or is it!")
IndentationError: unexpected indent
```

If you are writing code in an IPython terminal session, or using VS Code with the Python extension,
it can automatically indent for you. But, be careful!

## `if` statements

## `for` loops

## Iterators

A very useful built-in function that returns an iterator is the
[`range`](https://docs.python.org/3/library/functions.html#func-range) function. `range`

# List comprehension

You can use the `for` statement to create lists using a single line of code. This is called list
comprehension. For example, suppose we had a list of values and we wanted to create a new list with
the square of each of those values:

```python
values = [1, 2, 3, 4, 5]
x = [y ** 2 for y in values]
print(x)
[1, 4, 9, 16, 25]
```

We can also use an `if` statement within list comprehension if we require a specific condition to be
met, e.g.:

```python
import math
values = [-3, -2, -1, 0, 1, 2, 3]
# get a list of square roots, but only for positive numbers
x = [math.sqrt(y) for y in values if y > 0]
print(x)
[1.0, 1.4142135623730951, 1.7320508075688772]
```