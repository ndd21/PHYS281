# PHYS281: Scientific Programming and Modelling Project

This website provides a series of notes introducing the Python
programming language as part of the PHYS281 course. These notes are
available in both text and video formats. They can be accessed in any
order, but it is recommended to cover them in the order presented in
the table of contents sidebar. Concepts and terms will be covered in
that order.

To get the most out of the notes it is recommended that you try
writing and running the examples that are presented. A series of
exercises are provided to test yourself on the practicalities of
creating some code for a specific problem. These exercises are **not**
part of the course assessment.

This website was originally created by Matthew Pitkin, based on
earlier lecture notes by Iain Bertram, Robin Long and Brooke Simmons.
Feedback to improve this website is very welcome, so if you have any
questions or comments please contact the current module lecturer and
website maintainer:

* Neil Drummond, [n.drummond@lancaster.ac.uk](mailto:n.drummond@lancaster.ac.uk)

In this course we will use many jargon terms and unfortunately this is
inevitable. In some cases certain terms will be used interchangeably
as synonyms. We have created a [glossary](glossary.md) of many terms
to try and help with this, but it will be incomplete.  Please do ask
us if there are any concepts or terms that you do not understand and
remember that it may be helpful to search for the terms on the
Internet! It is worth noting that the aim of this course is to allow
you to write and use Python code. However, this is not a computer
science course and we do not expect you to understand the detailed
reasons behind why something is done in a certain way. In the majority
of cases you can treat what we show you as a recipe to follow without
needing to know why a particular syntax or formatting is required.

## Course aims

Programming is an important skill for scientists in the modern
world. At the end of this module you should be able to:

* understand the basic concepts involved in writing computer programs;
* understand the main features of Python;
* design and write simple programs in Python;
* devise and use test procedures for your programs;
* learn how to debug computer programs;
* design and write programs to solve numerical problems.

Programming is a skill. While there is a syntax that you have to learn, the skill is mainly
acquired through practice, i.e., actually writing and running code.

## What is Python?

[Python](https://www.python.org/) is a [programming
language](https://en.wikipedia.org/wiki/Programming_language), i.e.,
it is used to write instructions with a specific syntax that are
interpreted and run by a computer. Python is an interpreted language
rather than a compiled language. This means that you write a code that
is then interpreted and run line-by-line. In a compiled language, such
as [Fortran](https://en.wikipedia.org/wiki/Fortran) or
[C](https://en.wikipedia.org/wiki/C_(programming_language)), the code
you write has to be compiled by a different program to produce an
executable file (basically one written in a more primitive machine
language), that you then run.

Interpreted languages are often slower at certain tasks than compiled
languages, but have the advantage that they are easier for doing code
development, and can even be run interactively, due to not having the
extra compilation step.  Furthermore, many computationally intensive
tasks can be performed efficiently in Python using libraries such as
[NumPy](https://numpy.org/) and [SciPy](https://scipy.org/) that
contain routines that are themselves written in optimised C,
[C++](https://en.wikipedia.org/wiki/C%2B%2B) and Fortran code.

Python is what is known as an [Object Oriented
Programming](https://en.wikipedia.org/wiki/Object-oriented_programming)
(OOP) language (other major languages that support the object oriented
paradigm include [C++](https://en.wikipedia.org/wiki/C%2B%2B) and
[Java](https://en.wikipedia.org/wiki/Java_(programming_language))). This
means that the fundamental things that you use within a code are
objects; these are things that can contain both data and functions
that can perform specific tasks on that data.

There have been several versions of Python as the language gets
updated and new features added. The latest major version is Python 3,
with Python 3.13 being a recent stable release. While most Python code
is fairly backwards compatible, i.e., can run with previous versions
of the language, there are some specific features that are
not. Broadly speaking, code written based on Python 3.6 or above
should be compatible and in this course we will not use any syntax
that does not work across these versions.

Python can be run in both an interactive mode, i.e., you can start an
interactive Python terminal into which you can type and run commands
immediately, or it can be used to run pre-written scripts.  In this
course we will describe both these modes of use.

### Why Python?

There are many reasons why Python is a good choice as a programming
language to learn:

* Python is a popular language in school, so you are more likely to have
  experience that we can build on.
* Python is currently one of the most used languages in industry (see, e.g., the [IEEE Spectrum
  report](https://spectrum.ieee.org/top-programming-languages-2024)).
* There are a huge number of widely used and tested resources and packages out there for scientific
  computing (see, e.g.,
  [https://wiki.python.org/moin/NumericAndScientific](https://wiki.python.org/moin/NumericAndScientific)),
  such as [NumPy](https://numpy.org/), [SciPy](https://scipy.org/) and
  [Matploltib](https://matplotlib.org/).
* Python is portable - Python programs are cross platform and run on most computer systems in use
  today.
* Many modern data science and machine learning applications use Python as an interface, which is
  driving its growth.
* Python is currently used by many physicists in Lancaster University and elsewhere.

In the [TIOBE](https://www.tiobe.com/tiobe-index/) index, Python popularity and usage are high and still growing:

| Jun 2025 | Jun 2024 | Change | Programming Language | Ratings | Change |
| -------- | -------- | ------ | -------------------- | ------- | ------ |
| 1 | 1 | | Python | 25.87% | +10.48% |
| 2 | 2 | | C++ | 10.68% | +0.65% |
| 3 | 3 | | C | 9.47% | +0.24% |
| 4 | 4 | | Java | 8.84% | +0.44% |
| 5 | 5 | | C# | 4.69% | -1.96% |
| 6 | 6 | | JavaScript | 3.21% | -0.11% |
| 7 | 7 | | Go | 2.28% | +0.35% |
| 8 | 9 |:fontawesome-solid-sort-up: | Visual Basic | 2.20% | +0.54% |
| 9 | 11 | :fontawesome-solid-sort-up: | Delphi/Object Pascal | 2.15% | +0.62% |
| 10 | 10 | | Fortran | 1.86% | +0.33% |

## Course overview

This course is assessed through coursework only. There is no exam.

The course assessment consists of two main components:
 
* Programming exercises and quizzes over Weeks 1-5 of Michaelmas Term
* A project over Weeks 6-10 of Michaelmas Term

The programming exercises and quizzes in Weeks 1-5 count for 30% of the
overall grade (6% each week), with the project counting for 70%.

Help and guidance for the exercises and project will be provided in
weekly (Weeks 1-10) computer labs.

The programming exercises and quizzes must be submitted via MOODLE,
where information about deadlines can be found.  Submitted code will
be tested and marked automatically using a MOODLE plugin. To avoid
losing marks it is highly recommended that you test your code on your
own machine before submitting it on MOODLE. Read the questions and
expected inputs/outputs carefully, including making sure
functions/classes are named *exactly* as specified (including letter
case).

The project grade is split between several components:

* Two exercises to be submitted prior to the final project (5% each)
* The written project report (30%)
* The project code (30%)

The [project](gravity.md) aim is to create and test an $n$-body
gravitationally interacting system (e.g., the Solar System). The two
exercises provide a basis on which to build up to the full $n$-body
simulation.

## Prerequisites

Before getting started with the course please make sure you are
familiar with some of the basics of the exploring the directory/folder
structure of the computer operating system that you are using.  You
should know how to browse the directory structure (e.g., with "[File
Explorer](https://en.wikipedia.org/wiki/File_Explorer)" in Windows, or
"[Finder](https://support.apple.com/en-gb/guide/mac-help/mchlp2605/mac)"
on a Mac OS), be able to create new folders, and understand how file
path structure is formatted, including drive if necessary (e.g.,
`C:\User\username\Project\myfile.py`).

Please also see the material in the "Course notes" -> "Getting
started" menu for information on installing the software required for
this course ([Anaconda](demo-anaconda.md) and [Visual Studio
Code](demo-vs-code.md)) on your own machine or using AppsAnywhere on a
machine on campus. The ["Online Python
environments"](#online-python-environments) section below has some
options for running Python, which can be used as a back-up alternative
if you have initial installation problems.

## Unassessed exercises

A selection of [exercises](exercises.md) has been created for you to
try out and test your Python knowledge. These exercises are not marked
and are voluntary. They may also be used for demonstration purposes
during the course lecture slots.

## Other material

There are a variety of useful Python tutorials freely available online:

* The official Python documentation comes with a [tutorial](https://docs.python.org/3/tutorial/index.html)
  on getting started with Python, covering the majority of concepts required to become a proficient user.
* The `w3schools.com` site also offers a Python [tutorial](https://www.w3schools.com/python/default.asp)
  which provides interactive demonstrations embedded in the browser, and includes an introduction to
  [NumPy](https://numpy.org/).
* There is a very nice, and freely available, Software Carpentry course
  "[Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/index.html)".

### Recommended reading

* **Think Python**, 3rd ed., Allen B. Downey, O'Reilly (2024), [https://greenteapress.com/wp/think-python-3rd-edition/](https://greenteapress.com/wp/think-python-3rd-edition/): this book is freely available from the website.
* **Python Data Science Handbook**, Jake VanderPlas, O'Reilly (2016),
  [https://jakevdp.github.io/PythonDataScienceHandbook/](https://jakevdp.github.io/PythonDataScienceHandbook/):
  this book is freely available from the website.
* **Fluent Python**, 2nd ed., Luciano Ramalho, O'Reilly (2022): this book is a bit more advanced, and might be useful for extending what you have learned in PHYS281.

Please let me know if you have found any other Python textbooks
particularly useful.

### Asking for help

If you send code by email or Teams (or if you ever post code to an
external forum such as StackOverflow), it is always better to copy and
paste your code as **text** than to attach a screenshot or a picture
of your code; sending your code as text ensures that the recipient can
easily copy and run it rather than just look at it.

### Ethical programming

Programming is done by people and the outputs of code can affect peoples'
lives. In some cases the code you produce may be part of publicly
funded work. In others, it may be done within a private institution
and bound by national laws or industry-specific regulations and
guidelines. So programming cannot exist independently of ethics and
scrutiny by others.

In general, it is good to think of the following practices when programming:

* Do not use code for illegal or malicious activities.
* Make sure you properly attribute any part of your code that uses code/algorithms from other
  sources. Many codes have open source licenses that allow you to use them or edit them provided
  proper credit is given. Consider giving an open source license to your own code (see, e.g.,
  [here](https://choosealicense.com/)), such as an [MIT
  license](https://choosealicense.com/licenses/mit/) or [GPL
  license](https://choosealicense.com/licenses/gpl-3.0/).
* Programming is often done as part of a community. In such cases be kind and be inclusive. Take a look
  at, e.g., the [NumFOCUS Code of Conduct](https://numfocus.org/code-of-conduct).
* If your code directly affects people or uses personal data, think about whether its design could
  contain or promote biases and if so whether it is possible to mitigate against them.
* Try to document, curate and distribute your code, so that it is useful and usable to others.
  Results should be reproducible into the future. For example, consider hosting your code on a open
  repository such as [Github](https://github.com) (other repositories exist!) and providing online
  documentation, including practical examples of running the code, on sites such as [_Read the
  Docs_](https://readthedocs.org/).
* Make sure any data that your code uses or produces is curated and handled in accordance with data
  protection and governance laws. This is particularly relevant to personal data, for which security
  of the data and compliance with laws and user agreed conditions of use are vital.

While these may not seem relevant to this particular course they are
good things to keep in mind for the future.

### Online Python environments

There are a variety of online Python environments that can be used as
a back up. These generally require your to create an account, but
there are generally free account options that provide a limited but
usable range of functionality. For the first half of the course these
should suffice for any programming needs, but may be more limited when
attempting the project. The options suggested below seem to have
NumPy, SciPy and Matplotlib available.

* Python Anywhere [https://www.pythonanywhere.com](https://www.pythonanywhere.com)
* repl.it [https://repl.it](https://repl.it)
* Google Colaboratory notebook
  [https://colab.research.google.com](https://colab.research.google.com) - this requires a Google
  account and provides a Jupyter Notebook like Python environment. You can produce plots and install
  a wide variety of packages using pip.

Please let us know of any others.

### Generative artificial intelligence (ChatGPT, Gemini, etc.)

Using large language models to generate code or text for you should be
viewed in a similar way to asking another human for help, or
downloading pieces of code from the Internet.  These are all fine, and
indeed to be encouraged if they assist your learning, but you should
never try to pass somebody else's work off as your own.  Above all,
the whole point of the module is to enable you to learn how to
program; if you undermine this by getting somebody or something else
to carry out the exercises for you then it will not help you when you
come to tackle the PHYS281 project (or indeed other projects in later
years).
