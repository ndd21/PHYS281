# Importing modules

A **module** is ["*... a file containing Python definitions and statements*"](https://docs.python.org/3/tutorial/modules.html#modules).

Python contains a range of [built-in modules](https://docs.python.org/3/py-modindex.html) that contain many useful functions or classes you can use.

 * **built-in** modules are files that are automatically bundled with, and accessible by, every
   Python installation (the bundled modules can change for different Python versions).

There are also a huge range of third-party packages  that can be installed and then used within Python. 

 * a **package**, or *library*, is a bundle of files that may contain one or more modules and submodules

To use a module within a Python terminal or script you must **import** it, which means loading in the entire module or certain things within it.

For example, if I wanted to determine the date I could use the built-in module [`datetime`](https://docs.python.org/3/library/datetime.html#module-datetime):

```python
import datetime
print(datatime.date.today())
2020-06-10
```

Once imported, the module functions and classes exist within the module's *namespace*. In the example, to use the `date` class that exists within the `datetime` module I've had to write `datatime.date`.

 * a **namespace** is generally way to try and keep names used within a program unique (i.e., if another module was imported that also had a `date` class it would still be separate from that in `datetime`)

You don't need to keep the namespace, e.g., I could just import the `date` class from `datetime` using the `from` keyword:

```python
from datetime import date
print(date.today())
2020-06-10
```

But, this runs more risk of clashing names.

As the module definition states, you can import from any Python file, where a Python file is one
saved with the "`.py`" file extension, e.g., `myfunctions.py` (it's best have have file names that are representative of the contents). If I had a file called `message.py` with the following content:

```python
def message_in_box(a):
    """
    Print a message in a box.

    Parameters
    ----------
    a: str
        The message to print.
    """

    messagelen = len(a)
    output = "{}\n# {} #\n{}"
    print(output.format((4 + messagelen) * "#", a, (4 + messagelen) * "#"))
```

then I could use this with:

```python
import message

message.message_in_box("Hello world!")
```

When importing you can use alias for commomly used module namespaces or functions/classes. This can
be for convenience or to avoid clashes. There are two common aliases that you might see in codes on
the internet:

```python
import numpy as np
from matplotlib import pyplot as plt
```

In the first instance this means that the `numpy` namespace is aliases to `np` and in the second the `pyplot` submodule of `matplotlib` is aliased to `plt`, e.g.,

```python
import numpy as np
x = np.sin(3.2)

# rather than
import numpy
x = numpy.sin(3.2)
```

## Glossary

`import`: load a module into a Python terminal session or script
`from`: declare a module from which you want to import something, but within the local namespace
`as`: set an alias for the namespace to use for an import