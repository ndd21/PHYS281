# Exercises

Here are a selection of exercises covering various aspects of the course material. Their aim is to
make you think about how to solve a problem using code. These are not assessed, but you are
encouraged to try these out as the best way to learn to code is to do!

In several cases there are already exist functions, e.g., in NumPy, for performing some of these
exercise problems. While generally you should use existing functions from well maintained libraries
(they will be very well tested and robust), here the aim is for you to think about how you would
code up the function yourself.

!!! note "Exercise 1"

   !!! question "Part 1"

      Write a function that takes in a list of numbers as an argument and returns their mean.

   ??? info "Answer"

      An example of how to do this is:

      ```python
      def mean(values):
          s = 0.0  # variable to hold sum of values
          for value in values:
              s += value

          # return the mean
          return s / len(values)
      ```

      You could add some checking that values is indeed a list. You could also use the built-in
      Python [`sum()`]((https://docs.python.org/3/library/functions.html#sum) ) function rather
      than using the for loop.

   !!! question "Part 2"

      Write a function that takes in a list of numbers as an argument and returns their standard
      deviation. Can the function from Part 1 be re-used?

   !!! question "Part 3"

       Write a function that that takes in list of numbers as an argument and returns the median.

## Exercise 2

Write a function that:
* takes in a list of strings as an argument,
* finds the unique strings,
* counts the number of occurances of each of those unique strings in the list
* returns those number counts in a dictionary keyed by the unique string values.

E.g.,

```python
>>> animals = ['cat', 'dog', 'dog', 'dog', 'cat', 'horse']
>>> counts = count_occurances(animals)
>>> print(counts)
{'cat': 2, 'dog': 3, 'horse': 1}
```

## Exercise 3

### Ex. 3 Part 1

Write a function that takes in a list as an argument and returns a new list containing the square of
every $n$th index (starting at the 0 index), where $n$ is another argument to the function with a
default value of 2.

E.g.,

```python
>>> values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> sq = square_index(index)
>>> print(sq)
[4, 16, 36, 64, 100]
```

### Ex. 3 Part 2

Alter the function so that it takes in another argument, `reverse`, which defaults to `False`, but
if `True` makes the function return the list in reverse order.

## Exercise 4

### Ex. 4 Part 1

Write a function that returns a [boxcar function](https://en.wikipedia.org/wiki/Boxcar_function) of the form:

$$
f(x) = \left\{\begin{array}{rl}
 0, & \text{if } |t| < a \\
 C, & \text{if } a \leq |t| \leq b  \\
 0, & \text{if } |t| > b.
\end{array}\right.
$$

where the arguments should be a list containing $x$ values at which to evaluate the function, the
limits $a$ and $b$ and the amplitude $C$. The following defaults (to give a standard [rectangular
function](https://en.wikipedia.org/wiki/Rectangular_function)) should be set: $a = -1/2$, $b=1/2$,
and $C = 1$.

### Ex. 4 Part 2

Write a function to that returns a triangular function of the form:

$
f(x) = 
$