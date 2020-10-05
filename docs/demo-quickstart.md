# Python: a quick-start guide

First, it's traditional for one's first program in any new language to greet the world. You can do this just by typing at the Python prompt:

```
>>> print("Hello World!")
Hello World!

```


## Program Order

In a more formal program that you would save to a file:

1. Any packages/modules you need to import should be called first.
2. Then any functions (more on this later) we want to declare.
3. Then the code you actually want to run.

```
# This is a comment line; comments can be anywhere
# Import packages first
# You can just say "import numpy" but then you have to use numpy.pi below 
#     and anywhere else, and that gets old fast, so use standard shorthand
import numpy as np

# Now declare functions you'll use below
def print_pi():
    print('The value of pi is ', np.pi)

# Now run whatever code you need to
print_pi()
```

## Python as a calculator

If you just want to use python to do some quick calculations, you can. It's also useful to play with this to get a sense of how Python works with numbers. Usually, it does exactly what you expect.

```
>>> 3 + 6
9

>>> 97 - 12
85

>>> 97.0 - 12
85.0

>>> 10 * 4
40

>>> 10 / 4
2.5
```

Notice that, when Python did the division, it automatically converted to a decimal (floating-point) number even though it was given 2 integers. If, for some reason, you **don't** want that to happen, use the floor operator to force integer division:

```
>>> 10 // 4
2
```

The floor operator truncates the decimal part of the result. It does *not* round.

Two more operators that you will find useful are the power and modulo operators:

```
# note: the power doesn't have to be an integer (try it)
>>> 2**3
8

# modulo: divide the first number by the second, and return the remainder
>>> 10 % 3
1
```

## Complex Numbers
We use *i* in physics, but Python uses *j*:

```
>>> (2 + 3j)*(1 - 2j)
(8 - 1j)
```

Note the following won't work:

```
>>> j**2
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-12-5678b10dee2c> in <module>()
----> 1 j**2

NameError: name 'j' is not defined
```

#### Why?
Python thinks a single *j* on its own is a variable! And we haven't defined that variable yet.

But this works fine:

```
>>> 1j**2
(-1 + 0j)
```

## Variables

- We store values using variables.
- Assign values using the equals, symbol, `=`. 
- A variable can have (almost) any name, but certain characters aren't allowed.
- Variable names must begin with a letter or an underscore, `_`.

### Valid variable names:

- `hello_world`
- `_helloworld`
- `helloworld_`
- `helloworld123`

### Invalid variable names:

- `123helloworld`
- `hello world`
- `hello&world`

## Assigning variables
Fire up Python and try out assigning and working with some variables:

```
>>> x = 3 + 4
>>> y = 3.0 + 5.2

>>> print(x, y, x+y)
7  8  15.2

>>> a = 2 + 3j
>>> b = 1 - 2j
>>> c = a * b
>>> print(c)
(8 - 1j)
```

*Pro tip:* Make your variable names descriptive (but not too long).

That way, when you come back to a code you haven't looked at in weeks, you will still be able to tell what it's doing at a glance.


## Functions

Functions are self-contained units of code that you can call from other parts of your code. 

We create a function using the `def` keyword, followed by the name of the function (see tip about variable names above: same applies). 

After the name, you specify what arguments the function will take, if any, in brackets. After the closing bracket, there's a colon `:`

```
# just print something, no arguments, nothing returned back
def say_hello():
    print("Hello world!")
    return


# take a variable and do something with it, also return the result
def square_it(x):
    return x**2


# swap the values of two variables and return them both
def swap(x, y):
    return y, x
```

Nothing will visibly happen when you run this code, because this just defined the functions. It doesn't call them, but it does load them into memory.

But now that they're loaded, you can use them:

```
>>> say_hello()
Hello world!

>>> t = square_it(4.2)
>>> print(t)
17.64

>>> a = 3
>>> b = 2

>>> result = swap(a, b)
```

The function returns 2 variables but we saved them in 1. What format is the result in?
```
>>> result
(2, 3)
```

The function returns multiple variables as a tuple.

We can access individual values with indices:
```
>>> result[0]
2

>>> result[1]
3
```

Or, we can split the tuple when we call the function:
```
>>> a_swap, b_swap = swap(a, b)
>>> print(a_swap)
2

>>> print(b_swap)
3
```

## See this code in a notebook

You can play with this code [in a Google Colab notebook](https://colab.research.google.com/drive/1uAgmWZ4OJO3SklbuJkGpi16xqah0E1fp?usp=sharing). Copy the notebook to your own version, and play around with changing values, exploring functions, and so on. A Jupyter notebook like this is like a sandbox for you to test code and try out new things.