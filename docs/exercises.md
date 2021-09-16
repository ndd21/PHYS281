# Exercises

Here are a selection of exercises covering various aspects of the course material. Their aim is to
make you think about how to solve a problem using code. These are not assessed, but you are
encouraged to try these out as the best way to learn to code is to do!

In several cases there are already exist functions, e.g., in NumPy, for performing some of these
exercise problems. While generally you should use existing functions from well maintained libraries
(they will be very well tested and robust), here the aim is for you to think about how you would
code up the function yourself.

## Exercise 1

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

??? info "Answer"
    An example of how to do this is:

    ```python
    def std(values):
        # get the mean of the values (re-use the previous function)
        mu = mean(values)
        
        # get the variance (re-use mean function again)
        var = mean([(x - mu)**2 for x in values])

        # return the standard deviation
        return var ** 0.5
    ```

!!! question "Part 3"
    Write a function that that takes in list of numbers as an argument and returns the median.

??? info "Answer"
    An example of how to do this is:

    ```python
    def median(values):
        # use the built-in sorted function to sort the values in ascending order
        sortvals = sorted(values)

        # get the halfway index
        half = int(len(values) / 2)
        
        # check if values contains an odd or even number of values
        if len(values) % 2 == 0:
            # an even number, so return average of middle two numbers
            return (values[half - 1] + values[half]) / 2
        else:
            # an odd number, so return middle number
            return values[half]
    ```

## Exercise 2

!!! question
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

??? info "Answer"
    A way of doing this is:

    ```python
    def count_occurances(values):
        # get unique strings by converting to a set
        unique = set(values)

        # create empty dictionary for counts
        counts = {}

        # loop over unique strings and count occurances
        for word in unique:
            count = 0
            for w in values:
                if w == word:
                    count += 1

            # short method (use count method of a list)
            #counts[word] = values.count(word)

        return counts
    ```

## Exercise 3

!!! question "Part 1"
    Write a function that takes in a list as an argument and returns a new list containing the square of
    every $n$th index (starting at the 0 index), where $n$ is another argument to the function with a
    default value of 2.

    E.g.,

    ```python
    >>> values = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> sq = square_index(values)
    >>> print(sq)
    [4, 16, 36, 64, 100]
    ```

??? info "Answer"
    A way of doing this is:

    ```python
    def square_index(values, step=2):
        squ = []

        # loop over list in steps of "step"
        for i in range(0, len(values), step):
            squ.append(values[i] ** 2)

        return squ

        # short method (using slice notation instead)
        #return [x ** 2 for x in values[::step]]
    ```

    You may want to include checks that `values` is a list and that `step` is an integer.


!!! question "Part 1"
    Alter the function so that it takes in another argument, `reverse`, which defaults to `False`, but
    if `True` makes the function return the list in reverse order.

??? info "Answer"
    A way of doing this is:

    ```python
    def square_index(values, step=2, reverse=False):
        squ = []

        # get indices to return
        if reverse:
            idxs = range(len(values), 0, -step)
        else:
            idxs = range(0, len(values), step)

        # loop over list in steps of "step"
        for i in idxs:
            squ.append(values[i] ** 2)

        return squ
    ```

## Exercise 4

!!! question "Part 1"
    Write a function that returns a [boxcar function](https://en.wikipedia.org/wiki/Boxcar_function) of the form:

    $$
    f(x) = \left\{\begin{array}{rl}
     C, & \text{if } a \leq x \leq b  \\
     0, & \text{otherwise},
     \end{array}\right.
    $$

    where the arguments should be a list containing $x$ values at which to evaluate the function,
    the limits $a$ and $b$ at which the boxcar starts and stops, and the amplitude $C$. The
    following defaults (to give a standard
    [rectangular function](https://en.wikipedia.org/wiki/Rectangular_function)) should be set:
    $a = -1/2$, $b=1/2$, and $C = 1$.

!!! question "Part 2"
    Write a function to that returns a
    [triangular function](https://en.wikipedia.org/wiki/Triangular_function) of the form:

    $$
    f(x) = \left\{\begin{array}{rl}
    C - \left|\frac{{\rm d}y}{{\rm d}x}(x - x_0)\right|, & \text{if } a \leq x \leq b \\
    0, & \text{otherwise},
    \end{array}\right.
    $$

    where $x_0$ is the midpoint of the triangle. The arguments should be a list containing $x$
    values at which to evaluate the function, the limits $a$ and $b$ at which the triangle starts
    and stops, and the peak triangle amplitude $C$. The following defaults (to give a standard
    normalised [triangular function](https://en.wikipedia.org/wiki/Triangular_function)) should be
    set: $a = -1$, $b=1$, and $C = 1$.

??? info "Answer"
    A potential way to do this is:

    ```python
    def tri(x, a=-1, b=1, C=1):
        vals = []
        
        # get half-width of the triangle's base
        halfwidth = (b - a) / 2

        # mid-point of triangle
        mid = a + halfwidth

        # gradient of triangle sides dy/dx
        grad = C / halfwidth

        # loop over x-values
        for xs in x:
            if a < xs < b:
                vals.append(C - abs(grad * (xs - mid)))
            else:
                vals.append(0.0)

        return vals
    ```

    You may want to include checks that `x` is a list, that `a` is less than `b`, and that `C` is positive.