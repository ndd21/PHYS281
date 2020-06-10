# Importing modules

A **module** is ["*... a file containing Python definitions and statements*"](https://docs.python.org/3/tutorial/modules.html#modules).

Python contains a range of [built-in modules](https://docs.python.org/3/py-modindex.html) that contain many useful functions or classes for use in your code.

 * **built-in** modules are files that are automatically bundled with, and accessible by, every
   Python installation (the bundled modules can change for different Python versions)

There are also a huge range of third-party packages  that can be installed and then used within Python. 

 * a **package**, or *library*, is a bundle of files that may contain one or more modules and sub-modules

To use a module within a Python terminal or script you must "import" it, which means loading in the entire module or certain things within it.

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