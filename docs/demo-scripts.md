# Python scripts

A Python script is a file that generally contains a short self-contained bit of code that performs a
specific task. In reality scripts can be any length and do multiple things, but it is not
recommended that 

A Python script file must have the `.py` suffix file extension. File names can be anything that your
operating system allows, but it is recommended that they be short and descriptive of what they
contain. It is also good practice to not have blank spaces in file names.

An example script might be a file called `tell_time.py` that contains:

```python
"""
A script to show the user the current time.

Author: Matthew Pitkin
Email: m.pitkin@lancaster.ac.uk
Date: 22/06/2020
"""

# import the required modules
import datetime


def gettime():
    """
    A function to return the current time.

    Returns
    -------
    tuple:
        A tuple containing the hour, minutes and seconds.
    """

    now = datetime.datetime.now()

    return now.hour, now.minute, now.second + 1e-6 * now.microsecond

# get the time
hour, minute, seconds = gettime()

print("The current time is {}:{}:{}".format(hour, minute, seconds))
```

This script can then be run in a terminal using:

```bash
python tell_time.py
```

If you write a script in VS Code you don't need to open a terminal to run it. You can hit the green
triangular play button in the top right corner and it will automatically open a terminal and run the
script for you.

> Note: if you are using Linux of Mac you can start your scripts with the line `#!/usr/bin/env
> python`. This is known as a ["shebang"](https://en.wikipedia.org/wiki/Shebang_(Unix)) and if you
> make you script executable, e.g., with `chmod u+x tell_time.py` you can then just run it in the
> terminal with `./tell_time.py`

As described in the [Importing Modules] demonstration any file with the `.py` extension is also a
Python module. This means that you can import variables, functions or classes defined in one script
into another.

For small projects with multiple script it is useful to keep them in the same directory so that you can import 
(The more advanced topic of "packaging" you project is beyond the scope of this course, although is
a very useful thing to learn)

For example, I could create a new script in the same directory as `tell_time.py` called
`sydney_time.py` that contains:

```python
"""
A script to tell me the current time in Sydney, Australia.

Author: Matthew Pitkin
Email: m.pitkin@lancaster.ac.uk
Date: 22/06/2020
"""

# import time from gettime
from tell_time import gettime

# use gettime function from tell_time
hour, minute, seconds = gettime()

# get the time in Sydney
sydneyhour = (hour + 9) % 24

print("The current time in Sydney is {}:{}:{}".format(sydneyhour, minute, seconds))
```

## Command line arguments