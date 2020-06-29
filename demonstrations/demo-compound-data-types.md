# Compound data types

In addition to the basic data types for integers (`int`), floating point numbers (`float`) and
strings of text (`str`), there are some other standard Python data types that can hold multiple
pieces of data.

## Lists

Lists can hold an array of **any** other Python object. Lists are defined using square brackets `[]`
or the `list` keyword.

```python
# a list containing some integers
x = [1, 2, 3]

print(type(x))
<class 'list'>
```

You can access values in a list using their index. The index is an integer giving an items location
within the list. In Python indexes start at zero, e.g.:

```python
print(x[0])
1
```

You can access the last element of a list using:

```python
print(x[-1])
3
```

You can create an empty list using:

```python
x = []
x = list()
```

To find out the length of a list you can use the `len` keyword:

```python
x = [1, 2, 3]
print(len(x))
3
```

You can initialise a list containing multiple instances of a particular value, e.g., initialising it
to contain 10 zeros, with:

```python
x = [0] * 10
print(x)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```

### Slices

You can return certain values from a list using a slice: `startidx:endidx` or `startidx:endidx:step`.

With `startidx:endidx` the `startidx` value is the index for the first list value you want to return
and `endidx` is **one more** than the last list value that you want to return, e.g.:

```python
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(x[0:5])
[1, 2, 3, 4, 5]

# equivalently
print(x[:5])
[1, 2, 3, 4, 5]

print(x[2:7])
[3, 4, 5, 6, 7]

# print up to the last value
print(x[5:])
[6, 7, 8, 9, 10]

# copy those values into a new list variable
y = x[3:5]
print(y)
[4, 5]
```

With `startidx:endidx:step` you can also just return every `step`th value, e.g.:

```python
# return every other value
print(x[::2])
[1, 3, 5, 7, 9]

# return every other value from index 2 onwards
print(x[2::2])
[3, 5, 7, 9]

# return every third value from the start to one before index 8
print(x[:8:3])
[1, 4, 7]
```

You can return a reversed version of the list with:

```python
print(x[::-1])
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### Copying lists

If you set a new variable to be equal to another list variable then the new variable is **not** a
copy of the original list, it is just another name assigned to the same bit of memory as the
original variable name (in `C` jargon it's a pointer). So, if you change the new variable then
original one will also be changed. E.g.

```python
x = [1, 2, 3]
y = x  # new variable "pointing" to the same list as x

y.append(4)
print(x)
[1, 2, 3, 4]
```

To create a new variable that is a copy of another list you must use the copy method:

```python
x = [1, 2, 3]
y = x.copy()  # a copy of the list x

y.append(4)
print(x)
[1, 2, 3]
print(y)
[1, 2, 3, 4]
```

You can also make a copy by using `list`, e.g.,

```python
y = list(x)
```

or explicitly using the built-in [`copy`](https://docs.python.org/3/library/copy.html) module:

```
import copy
y = copy.deepcopy(x)
```

### List methods

Like everything in Python lists are objects and have a variety of useful methods. I'll show a few
here, but they can all be seen by typing `help(list)` in a terminal.

#### Append

Add a new item onto the end of the list:

```python
x = [1, "Hello", 3.4]

# append a new item onto the end of the list
x.append(2)
print(x)
[1, 'Hello', 3.4, 2]
```

#### Insert

Insert an item at a given index:

```python
# insert something into the index 2 (i.e., the third item in the list)
x.insert(2, "World")
print(x)
[1, 'Hello', 'World', 3.4, 2]
```

#### Index

Find the index of a particular value in the list:

```python
x = ["a", "b", "c", "d"]
idx = x.index("b")
print(idx)
1
print(x[idx])
b
```

#### Sort

Sort the values in numerical or alphabetical order.

```python
x = ["b", "d", "a", "c"] 
x.sort()
print(x)
['a', 'b', 'c', 'd']

# sort in reverse order
x = ["b", "d", "a", "c"] 
x.sort(reverse=True)
print(x)
['d', 'c', 'b', 'a']
```

> Note: `sort` works "in place", i.e., it actually changes the list. To return a sorted version of a
> list, but keep the original list as it is you can use the built-in `sorted()` function, e.g.

```python
x = ["b", "d", "a", "c"]
y = sorted(x)
print(x)
['b', 'd', 'a', 'c']
print(y)
['a', 'b', 'c', 'd']
```

## Tuples and sets

## Dictionaries

Dictionaries are a very useful data type as rather than referencing a value by its index in the
array you can reference it with a key. This key can be a word, so you don't have to know the
position you just have to know the key.