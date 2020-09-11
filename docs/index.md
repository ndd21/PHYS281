# PHYS281: Scientific Programming and Modelling Project

This website provides a series of tutorials introducing the Python programming language as part of the
PHYS281 course. The tutorials are available in both text and video formats. They can be accessed in
any order, but it is recommended to cover them in the order presented in the table of contents
sidebar. Concepts and terms will be covered in that order.

To get the most out of the tutorials it is recommended that you try writing and running the examples
that are presented yourself.

Feedback to improve these notes is very welcome, so if you have any questions or comments please contact:

* Dr Matthew Pitkin, m.pitkin@lancaster.ac.uk
* Dr Brooke Simmons, b.simmons@lancaster.ac.uk

## What is Python?

[Python](https://www.python.org/) is a [programming
language](https://en.wikipedia.org/wiki/Programming_language), i.e., it is used to write
instructions with a specific syntax that are interpreted and run by a computer. Python is an
interpreted language rather than a compiled language. This means that you write a code that is then
interpreted and line-by-line and the commands run. In a compiled language, such as
[C](https://en.wikipedia.org/wiki/C_(programming_language)), the code you write has to be compiled
by a different programme to produce an executable file (basically one written in a more primitive
machine language), that you then run.

Interpreted languages are often slightly slower at certain tasks than compiled languages, but have
the advantage that they are easier for doing code development, and can even be run interactively,
due to not having the extra compilation step.

Python is what is known as an [Object Oriented
Programming](https://en.wikipedia.org/wiki/Object-oriented_programming) (OOP) language (other major
languages that support the object oriented paradigm include
[C++](https://en.wikipedia.org/wiki/C%2B%2B) and
[Java](https://en.wikipedia.org/wiki/Java_(programming_language))). This means that the fundamental
things that you use within a code are objects; these are things that can contain both data and
functions that can perform specific tasks on that data.

There have been several versions of Python as the language gets updated and new features added. The
latest major version in Python 3, in particular with Python 3.8 being a recent stable release. While
most Python code is fairly backwards compatible, i.e., can run with versions of the language, there
are some specific features that are not. Broadly speaking, code written based on Python 3.5 of above
should be compatible and in this course we will not use any syntax that does not work across these
versions.

### Why Python?

There are many reasons why Python is a good choice as a programming language to learn:

* Python is now becoming a popular language in High School. You are more likely to have experience
  which we can build on.
* Python is currently one of the most used languages in industry (see, e.g., the [IEEE Spectrum
  report](https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2019)).
* Python is currently used by many more academics in the department.
* There are a huge number of widely used and tested resources and packages out there for scientific
  computing (see, e.g.,
  [https://wiki.python.org/moin/NumericAndScientific](https://wiki.python.org/moin/NumericAndScientific)),
  such as [NumPy](http://www.numpy.org/), [SciPy](https://www.scipy.org/) and
  [Matploltib](https://matplotlib.org/).
* Python is portable - Python programs are cross platform and run on most computer systems in use today.
* Many modern data science and machine learning applications use Python as an interface, this
  driving its growth.

In the [TIOBE](https://www.tiobe.com/tiobe-index/) index Python popularity and usage is still
growing:

| Sep 2020 | Sep 2019 | Change | Programming Language | Ratings | Change |
| -------- | -------- | ------ | -------------------- | ------- | ------ |
| 1	| 2 | :fontawesome-solid-sort-up: | C | 15.95% | +0.74% |
| 2	| 1	| :fontawesome-solid-sort-down: | Java | 13.48% | -3.18% |
| 3 | 3	| | Python | 10.47% | +0.59% |
| 4 | 4 | | C++ | 7.11% | +1.48% |
| 5 | 5	| | C# | 4.58% | +1.18% |
| 6 | 6	| | Visual Basic | 4.12% | +0.83% |

## Course overview

## Prerequisites

Before getting started with the course please make sure you are familiar with some of the basics of
the exploring the directory/folder structure of the computer operating system that you are using.
You should know how to browse the directory structure (e.g., with "[File
Explorer](https://en.wikipedia.org/wiki/File_Explorer)" in Windows, or
"[Finder](https://support.apple.com/en-gb/HT201732)" on a Mac OS), be able to create new folders,
and understand how file path structure is formatted, including drive if necessary (e.g.,
`C:\User\username\Project\myfile.py`).

## Other material

There are a variety of useful Python tutorial freely avaiable online. The official Python
documentation comes with a [tutorial](https://docs.python.org/3/tutorial/index.html) on getting
started with Python covering the majority of concepts required to become a proficient user. The
`w3schools.com` site also offers a Python [tutorial](https://www.w3schools.com/python/default.asp)
which provides interactive demonstrations embedded in the browser, and includes an introduction to
Numpy.

### Recommended reading

* **Python and Matplotlib Essentials for Scientists and Engineers**, Matt Wood, IoP Publishing, 2015
  [http://iopscience.iop.org/book/978-1-6270-5620-5](http://iopscience.iop.org/book/978-1-6270-5620-5):
  this book is freely available as a pdf from the IoP website. Note that this book is written based
  on Python 2 rather than Python 3, so minor differences will be present.
* **Python Data Science Handbook**, Jake VanderPlas, O'Reilly,
  [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/):
  this book is freely available from the website.