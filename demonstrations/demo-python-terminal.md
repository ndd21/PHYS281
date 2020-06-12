# The Python terminal

A **terminal** is a text-based window into which you can type commands and view outputs. 

You can run Python as an interactive environment within a terminal. Within this you can type and run
any Python commands. The terminal is useful for very quick

There are two types of Python terminal sessions: a *regular* session and an enhanced interactive
session. With a terminal window (a Powershell terminal on Windows, or a terminal session in VS Code)
enter a regular Python terminal session by typing `python` and hitting return. You should see something like:

```python
Python 3.7.2 (default, Dec 29 2018, 06:19:36) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

where the `>>>` starts a command prompt line, i.e., the line that you input commands onto. You can type commands in, e.g.

```
>>> x = 1 + 4
>>> print(x)
5
````

To quit the Python session and return to the regular terminal type `quit()` and hit return.

It is recommended to instead use the enhanced interactive version, IPython, which offers more
features for ease of use. IPython is started by typing `ipython` and hitting return. Now you should see something like:

```ipython
Python 3.7.2 (default, Dec 29 2018, 06:19:36) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.2.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

where the command prompt (`In [1]:`) looks slightly different.

In IPython you can do all the things of a standard Python terminal session:

```ipython
In [1]: x = 1 + 4

In [2]: print(x)
5
```

## Resources

See, for example, [Chapter 1 of the Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/01.00-ipython-beyond-normal-python.html) for lots of useful tips in using an IPython terminal.
