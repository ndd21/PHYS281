# Built-in functions

The are a set of [built-in
functions](https://docs.python.org/3/library/functions.html#built-in-functions) that are a part of
any Python installation, i.e., they can be used and recognised in any Python code. The built-in
function do not have to be imported.

We will describe a few common functions here, but there are many more, that are described at
[https://docs.python.org/3/library/functions.html](https://docs.python.org/3/library/functions.html).

## `abs`

The [`abs()`](https://docs.python.org/3/library/functions.html#abs) function will return the
absolute value of a real or complex number, e.g.:

```python
print(abs(-2.3))
2.3
print(abs(4.5 + 1.2j))
4.65725240888
```

## `dict`

The [`dict()`](https://docs.python.org/3/library/functions.html#dict) function is used to create a
new dictionary, e.g.:

```python
d = dict(value1=1, value2=2)
print(d)
{'value1': 1, 'value2': 2}
```

## `float`

The [`float()`](https://docs.python.org/3/library/functions.html#float) function creates a @(floating
point number) object from a number or a string, e.g.:

```python
num = float("4.5")  # convert a string containing 4.5 into a float representing 4.5
```

## `int`

The [`int()`](https://docs.python.org/3/library/functions.html#int) function creates an integer object
from a number or a string, e.g.:

```python
num = int("3")  # convert a string containing 3 into an int representing 3
```

## `input`

The [`input()`](https://docs.python.org/3.8/library/functions.html#input) function allows you to get
user input from the keyboard, e.g.:

```python
name = input("What is your name?")
```

## `len`

The [`len()`](https://docs.python.org/3/library/functions.html#len) function returns the length of an
object, such as a list, if this is meaningful for that object, e.g.,:

```python
x = [4, 9, 2, 6]
len(x)
4
```

## `list`

The [`list()`](https://docs.python.org/3/library/functions.html#list) function (actually a "[mutable
sequence](https://docs.python.org/3/library/stdtypes.html#typesseq)" rather than a function) is used
to create a new list, e.g.,:

```python
l = list((1, 2, 3))
print(l)
[1, 2, 3]
```

## `max`

The [`max()`](https://docs.python.org/3/library/functions.html#max) function returns the largest
value in a list of values, or the largest value from a set of @(arguments), e.g.:

```python
print(max([5, 7, 2, 1, 7]))
7
print(max(5, 7, 2, 1, 7))
7
```

## `min`

The [`min()`](https://docs.python.org/3/library/functions.html#min) function returns the smallest
value in a list of values, or the smallest value from a set of @(arguments), e.g.:

```python
print(min([5, 7, 2, 1, 7]))
1
print(min(5, 7, 2, 1, 7))
1
```

## `print`

The [`print()`](https://docs.python.org/3/library/functions.html#print) function allows you
to print text to the screen, e.g.:

```python
print("Hello")
Hello
```

!!! note
    `print` just prints text to the screen (or to a [file if
    specified](../demo-io/index.html#writing)). It does not return that text to a variable.

## `str`

The [`str()`](https://docs.python.org/3/library/functions.html#func-str) function returns a string
representation of an object, e.g.:

```python
numstr = str(3)  # get a string version of the integer number object 3
```

## `sum`

The [`sum()`](https://docs.python.org/3/library/functions.html#sum) function will sum the items
within a list (or other @(iterable)), e.g.:

```python
sum([2, 3, 4, 5, 6])
20
```

## `type`

The [`type()`](https://docs.python.org/3/library/functions.html#type) function return the @(type) of a
variable.

```python
type("Hello")
str
```

# Keywords

Along with the built-in functions, there are a set of [reserved
keywords](https://www.w3schools.com/python/python_ref_keywords.asp) in Python that have a specific
meaning and cannot be used for variable or function names.

A list of the current keywords can be found by importing the [`keyword`] module and printing the
`kwlist` value, e.g.:

```python
import keyword
for i in range(len(keyword.kwlist) // 5): 
    print("\t".join(keyword.kwlist[(i * 5):(i * 5 + 5)]))
False	None	True	and	as
assert	async	await	break	class
continue	def	del	elif	else
except	finally	for	from	global
if	import	in	is	lambda
nonlocal	not	or	pass	raise
return	try	while	with	yield
```

Many of these keywords will be defined in other the tutorials other tutorials, but a good resource
defining them all can be found [here](https://www.programiz.com/python-programming/keyword-list).