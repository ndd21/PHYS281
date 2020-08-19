# NumPy

[NumPy](https://numpy.org/) is a Python library containing many useful features for numerical and
scientific computation. It is not a built-in module, but is available in the default Anaconda
environment.

NumPy can be imported using:

```python
import numpy
```

You will often find that the NumPy namespace is aliased as:

```python
import numpy as np
```

In this tutorial we will use this `np` namespace.

This tutorial will not go into detail of the vast majority of functionality in NumPy, but much more
information can be found through the [official documentation](https://numpy.org/doc/stable/). We
will mainly focus on NumPy's array class, which is useful for holding multi-dimensional numerical
arrays of numbers.

## NumPy arrays

The basic class for NumPy arrays is the
[`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html) class. They can
hold arrays of any Python object, but are most generally used to hold arrays of numbers.

### Creating an array

Rather than using this `ndarray` class for creating new instances of NumPy arrays, the standard way
is to use the `array` function. To create a numerical array you can pass `array` a list of values:

```python
x = np.array([1, 2, 3])
print(type(x))
print(x)
print(x.dtype)
<class 'numpy.ndarray'>
[1 2 3]
int64
```

We passed a list of values and created a NumPy `ndarray` holding those values. The `array` function
will automatically try and identify the number's type and as we passed a list of integers it has set
the array's `dtype` attribute to `int64` (which stands for a 64 bit integer). If any of the numbers
were a `float` the type for all numbers would be a float:

```python
x = np.array([1.0, 2, 3])
print(x.dtype)
float64
```

It is often useful to be explicit about the type of number that you want to store, and generally
make sure they are floats if you are going to perform further mathematical operations on the array:

```python
x = np.array([1, 2, 3], dtype=float)  # explicitly type the values to be floats
print(x.dtype)
```

!!! warning
    If you have an integer array and use the `+=` operator to add another non-integer array to it
    it will raise an error:

    ```python
    x = np.array([1, 2, 3])
    y = np.array([3.5, 4.5, 6.5])
    x += y
    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-23-3fa90755daf3> in <module>
    ----> 1 x += y

    TypeError: Cannot cast ufunc add output from dtype('float64') to dtype('int64') with casting rule 'same_kind'
    ```

`ndarray`s have a shape attribute that returns a tuple containing the dimensions of the array and
the size of each dimension:

```
x = np.array([1, 2, 3])
print(x.shape)
print("Number of dimension: {}".format(len(x.shape)))
print("Length of array: {}".format(x.shape[0]))
(3,)
Number of dimension: 1
Length of array: 3
```

Like a regular a [`list`](../demo-compound-data-types/index.html#lists), values within an array can
be accessed using indexing, where the index starts as zero:

```python
print(x[0])  # first value in the array
1
print(x[1])  # second value in the array
2
```

You can also change the contents of an array by setting the values using their index, e.g.,

```python
x[2] = 100
print(x)
[  1   2 100]
```

Like with a [`list`](../demo-compound-data-types/index.html#lists) multiple values can be returned,
or assigned, using a [slice](../demo-compound-data-types/index.html#slices) (the `:`):

```python
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print(x[2:4])  # get values from indexes 2 and 3
[20 30]
print(x[4::2])  # get values from index 4 to end in steps of 2
[ 40  60  80 100]
x[0:3] = [20, 19, 18]  # re-assign the first three values
print(x)
[ 20,  19,  18,  30,  40,  50,  60,  70,  80,  90, 100]
```

You can assign returned parts of an array to a new variable:

```python
y = x[4::2]
print(y)
[ 40  60  80 100]
```

Again, similarly to a [`list`](../demo-compound-data-types/index.html#copying-lists), if you assign
a new variable name to an existing lists it just "points" to the existing list rather than making a
copy, e.g.,:

```
x = np.array([1, 2, 3])
y = x  # assign a variable y to point to x
y[0] = 100  # change something in y
print(x)  # see the change in x
[100   2   3]
```

The same is true of returned slices of parts of a list. If you assigned the return slice from a list
as a new variable it just "points" back to the memory in the original array, so if you alter the new
array the original one will be altered too:

```python
x = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
y = x[4::2]
print(y)
[ 40  60  80 100]
y[0] = 1000  # change the first index of y
print(y)
[1000   60   80  100]
print(x)  # see the change effects x
[   0   10   20   30 1000   50   60   70   80   90  100]
```

If you want a new array that contains the same contents as another one, but is not just a pointer,
you must copy the array. The simplest way to do this is to create a new array from the old one:

```python
x = np.array([1, 2, 3])
y = np.array(x)  # make a new array that contains a copy of x
print(y)
[1 2 3]
y[0] = 100  # change y
print(y)
[100   2   3]
print(x)  # show x in unaffected by the change to y
[1 2 3]
```

You can create arrays initialised with all elements contain zero, using the
[`zeros`](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html#numpy.zeros) function:

```python
x = np.zeros(10)  # an array of 10 zeros
print(x)
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
```

Or, containing all ones (using the
[`ones`](https://numpy.org/doc/stable/reference/generated/numpy.ones.html#numpy.ones) function):

```python
x = np.ones(10)  # an array of 10 ones
print(x)
[1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

x = 2.3964 * np.ones(3)  # an array of 3 values of 2.3964
print(x)                                                                                                               
[2.3964 2.3964 2.3964]

# or equivalently
x = np.full(3, 2.3964)
```

### Multidimensional arrays

Arrays can have any number of dimensions. You can create multi-dimensional arrays from
multi-dimensional lists (in the examples here we will stick to 2D objects), e.g.:

```python
x = np.array([[1, 2, 3], [4, 5, 6]])  # a 2x3 2D array
print(x.shape)
(2, 3)
print(x)
(2, 3)
[[1 2 3]
 [4 5 6]]
```

Values can be access either in a list-like indexing manner:

```python
print(x[0][2])  # get the value from the 1st row and 3rd column
3
```

or using a comma to separate the rows and columns:

```python
print(x[0, 2])  # get the value from the 1st row and 3rd column
3
```

Slices can also be used:

```
print(x[1, :])  # get all values from the 2nd row
[4 5 6]
```

### Joining arrays

Unlike a `list`, a NumPy `ndarray` does not have an `append` method to add new values to it. There
are instead a variety of ways to add new values.

You can insert values into an indexed position in an array using the
[`insert`](https://numpy.org/doc/stable/reference/generated/numpy.insert.html#numpy.insert) function.

```python
x = np.array([0, 1, 2, 3])
y = np.insert(x, 0, -1)  # insert the value -1 into the 0th index of the array
print(y)
[-1  0  1  2  3]
```

This does not alter the original array, but instead returns a new copy containing the inserted
value.

You can concatenate two arrays (of the same shape) using the
[`concatenate`](https://numpy.org/doc/stable/reference/generated/numpy.concatenate.html#numpy.concatenate)
function:

```python

```

There are also the
[`hstack`](https://numpy.org/doc/stable/reference/generated/numpy.hstack.html#numpy.hstack) and
[`vstack`](https://numpy.org/doc/stable/reference/generated/numpy.vstack.html#numpy.vstack)
functions that are similar to `concatenate`.

### Mathematical operations on an array

Arrays are overloaded so that the standard mathematical operators can be applied to them.

```python
# adding two arrays
x = np.array([5.5, 9.6, 12.2])
y = np.array([4.5, 0.4, -2.2])
z = x + y
print(z)
[10. 10. 10.]

# add a number to all values in an array
z = x + 2
print(z)
[ 7.5 11.6 14.2]

# add y to x in-place (i.e., x gets changed)
x += y
print(x)
[10. 10. 10.]

# subtract two arrays
z = x - y
[ 5.5  9.6 12.2]

# multiply two arrays (multiplication of each component individually)
z = x * y
print(z)

# multiply all numbers in an array by a value
z = x * 2
print(z)
[20. 20. 20.]

# divide two arrays
z = x / y
print(z)
[ 2.22222222 25.         -4.54545455]

# raise an array to a power
z = x ** 2
print(z)
[100. 100. 100.]
```

1D arrays can be thought of as vectors, and NumPy can be used to compute vector
[dot](https://en.wikipedia.org/wiki/Dot_product) and [cross
products](https://en.wikipedia.org/wiki/Cross_product):

```python
x = np.array([1, 0, 0])
y = np.array([0, 1, 0])
print(np.dot(x, y))  # vectors are orthogonal
0
z = np.cross(x, y)
print(z)
[0, 0, 1]
```

!!! note
    The [`dot`](https://numpy.org/doc/stable/reference/generated/numpy.dot.html#numpy.dot) function
    can be used for arrays of any number of dimensions, but if you have 1D arrays (e.g., vectors)
    then the [`vdot`](https://numpy.org/doc/stable/reference/generated/numpy.vdot.html#numpy.vdot)
    function can be used instead (if you supply higher dimensional array to `vdot` they will get
    "flattened" into 1D arrays). `vdot` is a little bit faster than `dot` when used on vectors:

    ```python
    %timeit np.dot(x, y)
    818 ns ± 39 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    %timeit np.vdot(x, y)
    613 ns ± 6.89 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)
    ```

    If the first vector supplied to `vdot` is complex valued then it's complex conjugate is
    automatically used when calculating the dot product. This is not the case for `dot`
    (see also, yet another similar function
    [`inner`](https://numpy.org/doc/stable/reference/generated/numpy.inner.html#numpy.inner)!):

    ```python
    x = np.array([3 + 4j, 8 - 1j, 9 + 2j])
    y = np.array([10.0, 9.0, 8.0])
    print(np.dot(x, y))
    (174+47j)
    print(np.vdot(x, y))
    (174-47j)
    print(np.dot(np.conj(x), y))  # explicitly perform complex conjugation to replicate vdot
    (174-47j)
    ```

The norm or magnitude of a vector can be calculated using the
[`norm`]()https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html function in the
NumPy linear algebra submodule
[`linalg`](https://numpy.org/doc/stable/reference/routines.linalg.html):

```python
print(np.linalg.norm(z))
1.0
```



The transpose of an array can be returned by using the `.T` attribute.

### Range-like arrays

The built-in Python `range` function can return a list of integers, but it is often useful to have a
1D array of non-integer spaced values. There are a couple of different ways to do this using NumPy:
the [`linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html) and
[`arange`](https://numpy.org/doc/stable/reference/generated/numpy.arange.html#numpy.arange)
functions.

`linspace` takes in an initial value and a final value, and the number of points within that range
(inclusive of the start and end values) at which to generate evenly spaced values:

```python
start = 0.1
stop = 1.2
num = 12
values = np.linspace(start, stop, num)
print(len(values))
12
print(values)
[0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2]
```

With `arange`, instead of supplying the number of steps you supply the step size, so equivalently we
could have done:

```python
start = 0.1
stop = 1.2
step = 0.1
values = np.arange(start, stop, step)
print(values)
[0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1]
```

!!! note
    `arange` is not inclusive of the final value, so if you want to include a value at your
    intended final values you could instead use:

    ```python
    values = np.arange(start, stop + step, step)
    print(values)
    [0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1.  1.1 1.2]
    ```

If you just give `arange` an integer start value, and optionally a stop value, it will work just
like `range` (i.e., using a default step size of 1), but will return a NumPy array rather than a
list.

## NumPy maths

NumPy has its own functions for many mathematical functions. Ones that are commonly used are the
trigonometric functions, exponentiation and logarithm. Many of these are equivalent to, and can be
used in place of, the functions in the built-in `math` library. The main differences is that these
functions work on arrays, so all values in the array can have the function applied to them.

## NumPy random number generation

## Saving and loading data

savetxt, loadtxt, save, load