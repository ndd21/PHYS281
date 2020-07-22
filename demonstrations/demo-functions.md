# Functions

If you have a piece of code that does a particular job and you need to reuse it multiple times it is
useful to define it as a function.

To define a function you use the [`def`](https://www.w3schools.com/python/ref_keyword_def.asp)
keyword followed by the name you want to give the function followed by brackets containing any
[arguments][arguement] that the function takes:

```python
def my_function(variable1, variable2):
    # contents of a function must be indented
    print(variable1, variable2)

a = "Hello"
b = "world!"

# use (or "call") the function with the two variable a and b
my_function(a, b)
Hello world!
```

The function name must start with an upper or lowercase letter, but can then contain any letters,
numbers or the underscore `_` character. It cannot contain spaces or. It is useful if the function
name is descriptive of what the function does. Some fairly common ways of defining function names is
to split multiple descriptive words using an underscore, or using [camel
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
def CountToTen():
    # indent the function
    for i in range(1, 11):
        # indent the for loop within the function
        print(i)

# use the function
CountToTen()
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

In the above examples there are some functions that take arguments, i.e., you pass variables to them
that they then use. In the definition each variable with the brackets is separated by a comma. The
name of the variable used in the definition is what that variable will be known as _within_ the
function even if the variable had a different name outside the function. As with function names, it
is useful for variable names to be descriptive. You can have as many arguments to a function as you
want, including no arguments at all!

```python
# a function with no arguments
def PiratePete():
    print("Aarrrrrrrr! Where's me treasure.")

# use the function (remember the brackets)
PiratePete()
Aarrrrrrrr! Where's me treasure.
```

Notice that when using the function, even when they take no arguments, you need to include the
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

These type of arguments are known as "positional" arguments. This means that when you pass values to
the function their order (or position) matters. Positional arguments are always *all* required when
you use the function, i.e., you cannot leave any out when calling the function.

It's best not to have too many arguments or you can lose track of them. If you do require lots of
arguments it can be useful to group them and instead define the function to take single variable
that has a type such as a list or dictionary.

### Keyword arguments

As well as positional arguments, you can define a function to be passed *keyword* arguments. With
these you pass a variable to a function using a specific "key" word that is then used as that
variable's name within the function. Keyword arguments and defined in the function definition using
a `keyword=value` pair.

Unlike positional keyword arguments, you do not have to call the function using all of (or even any
of) the keywords. However, this means that when defining a function with keyword arguments you must
give them default values that will be used if they are not explicitly set.

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

# use both minumum and maximum keywords
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

## Returning values

Many of the above example using the `print` built-in function to print a message to the screen.
However, you cannot use the output of the function if it just prints it, e.g., if you had a function
that calculated the sine of an angle and it just prints it to the screen it would be fine if that is
all you ever used it for, but if you wanted to use that output as part of a larger equation it
wouldn't be much use.

Most functions should return something to the user and that they can assign to a variable that can
then be used later in the code. To do this the
[`return`](https://www.w3schools.com/python/ref_keyword_return.asp) keyword is used within the
function definition. As well as returning a variable from the function it also tells to function to
exit, i.e., there shouldn't be code after the return (unless you're using it in a conditional
statement) as it won't get run.

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

## Functions as variables

Like everything within Python function are themselves objects. So, you can create a variable out of
a function by omitting the bracket during the function call:

```python
def sing_a_rainbow(forwards=True):
    colours = ["red", "yellow", "pink", "green", "purple", "orange", "blue"]
    if forwards:
        print(" and ".join(colours))
    else:
        print(" and ".join(colours[::-1]))

# create a variable from the function (note the lack of brackets)
song = sing_a_rainbow
print(song)
<function sing_a_rainbow at 0x7f9254c7f840>

# call the function using the new variable
song()
red and yellow and pink and green and purple and orange and blue

# or
song(forwards=False)
blue and orange and purple and green and pink and yellow and red
```

This means you can easily pass functions as arguments to other functions:

```python
def CanISing(aSong, forwards=True):
    # call the function aSong
    aSong(forwards=forwards)
    print("I can sing a rainbow too!")

song = sing_a_rainbow
CanISing(song)
red and yellow and pink and green and purple and orange and blue
I can sing a rainbow too!
```

## Variable scope

A variable's scope relates to where in a code a particular variable is recognised

## Documenting functions

The above examples are lacking one key feature. Documentation! It is very good practice to document
your code. This helps you and others know what your code is supposed to do. The documentation of a
function should briefly describe what it does, list its arguments, and state what it returns. Using
a couple of the above examples we could have:

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

As well as the _docstring_ you should liberally comment your code using comment lines starting with
`#`. Using descriptive variable names and leaving blank space lines between less closely related
code blocks will help with code readability.

[argument]: an *argument* is a variable that is passed to a function, so that it can be used within
the function.