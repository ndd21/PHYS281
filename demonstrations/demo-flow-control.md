# Flow control

When Python runs a script the code is executed from the top to the bottom. However, you might want
to only run certain parts of the code given specific conditions, or you might want to repeat
something multiple times. To do this you can use flow control:

 * `if... elif... else` statements (sometime called clauses)
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

## Conditional expressions

Before discussing `if` statements we need to describe conditional expressions. These can be
mathematical equalities and inequalities (useful for comparing numbers):

 * `x == y`: "the value of `x` is equal to the value of `y`"
 * `x != y`: "the value of `x` is not equal to the value of `y`"
 * `x > y`: "the value of `x` is greater than the value of `y`"
 * `x >= y`:  "the value of `x` is greater than, or equal to, the value of `y`"
 * `x < y`: "the value of `x` is greater than the value of `y`"
 * `x <= y`:  "the value of `x` is greater than, or equal to, the value of `y`"

These return a boolean value of `True` or `False`:

```python
x = 2
y = 3

x == y
False

x != y
True

x > y
False

x >= y
False

# save the output to a variable
expression = (x < y)
print(expression)
True
```

These expressions can be combined with the logical statements `and`, `or`, `not`:

 * `x and y`: "`x` is `True` and `y` is `True`"
 * `x or y`: "`x` is `True` or `y` is `True`"
 * `not x`: "`x` is not `True`" (i.e., "`x` is `False`")

where `x` and `y` can be variables, or other conditional expression like above. These also return
boolean values:

```python
a = 1
b = 5
c = 1

(a == c) and (a < b)
True

(a != c) and (a < b)
True

not (a == c)
False
```

> Note: if you have an `int` or `float` variable that is set to zero it will evaluate as `False` in
> a logical expression while any non-zero value will evaluate as `True`. For array-like variables
> such as lists, dictionaries or tuples, or strings, an empty array will evaluate as `False` while
> an array containing any number of values will evaluate as `True`.

The `is` keyword can be used to test is two variables have the same value and are also of the same
type:

```python
x = 2     # integer value
y = 2.0   # float value

# test that they have the same value
x == y
True

# test that the are the same
x is y
False
```

## `if` statements

You may want to execute a part of your code only if a certain condition is fullfilled. You can place
that code inside an `if` clause:

```python
x = 4

if x < 10:
    # indent the code within the if statement
    y = x * 2

# exit the if statement by removing the indent
print(y)
8
```

The condition being evaluated can be any combination of conditional expressions and logical
statements (it is neater to have them each within brackets):

```
x = 5.5
y = "Hello"
z = 13

if ((x != 3.0) and (y[0] == "H")) or (x % 2):
    print("I'm in the if statement")
I'm in the if statement
```

### `else`

If statements allow you to execute code under a certain condition, but what if you also want to
execute some different code if the condition is not fullfilled? You can combine an `if` with and
`else`:

```python
x = 4

if x < 2:
    # indent inside the initial if statement
    print("My number is less than 2")
else:
    # indent again for the else statement
    print("My number is greater than or equal to 2")
"My number is greater than or equal to 2"
```

### `elif`

There may be multiple exclusive conditions that you want to test for. To do this you can use `elif`
(or "else if") statements after an initial `if` statement:

```python
x = 3

if x < 2:
    # indent inside the initial if statement
    print("My number is less than 2")
elif x < 4:
    # indent again for the elif statement
    print("My number if greater than or equal to 2, but less than 4")
else:
    # indent again
    print("My number is greater than or equal to 4")
My number if greater than or equal to 2, but less than 4
```

You can have as many `elif` statements as required.

> Note: you do not have to end with an `else` if you've covered all the condition that are required.

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

There is a very similar way of 