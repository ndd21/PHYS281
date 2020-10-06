---
title: Phys281 Lecture 1
author: Matthew Pitkin and Brooke Simmons
date: 5 October, 2020

---

# Course Aims

Programming is an important skill for scientists in the modern world. At the end of this module you
should be able to:

1. Understand the basic concepts involved in writing computer programs;
2. Understand the main features of Python;
3. Design and write simple programs in Python;
4. Devise and use test procedures for your programs;
5. Learn how to debug computer programs;
6. Design and write programs to solve numerical problems.

---

# Staff 

- Academics 
	+ Matthew Pitkin, <m.pitkin@lancaster.ac.uk>
	+ Brooke Simmons, <b.simmons@lancaster.ac.uk>

- Contact 
	+ Chat in Teams ([Matt](https://teams.microsoft.com/l/chat/0/0?users=m.pitkin@lancaster.ac.uk)/[Brooke](https://teams.microsoft.com/l/chat/0/0?users=b.simmons@lancaster.ac.uk)) or via email
   		* **Note**: You can only expect help Monday to Friday from 9 to 5
   		
---

# Lectures

- Programming is a skill
   * It is not suited to book learning
   * It requires practice to learn, i.e., workshops 

- Course notes are available online in html and as video demonstrations
   * Moodle course page <https://modules.lancaster.ac.uk/course/view.php?id=28244>
   * Course notes page <http://ma.ttpitk.in/teaching/PHYS281/>. 
     * videos vary from 15 mins to over an hour
     * consume in short chunks as required
     * run the examples in the notes yourself!

- Look on Moodle for the suggested reading each week (quite top heavy loaded towards the start of the
course).

---

# Workshops

Weekly workshops on Tuesdays from 13:00-17:00 held on [Teams](https://teams.microsoft.com/l/channel/19%3a2fc8b74ecec9415da068a9d1db998c2f%40thread.tacv2/General?groupId=6450347a-2db6-4607-b96d-5b56f586d9b5&tenantId=9c9bcd11-977a-4e9c-a9a0-bc734090164a)
  
  - Read the course notes before the workshops.
  - Attempt exercises before the workshops if possible

* new Teams "channel" for each week's assignments
* we provide help and guidance in completing coursework, or general programming advice
* it's interactive: ask questions, help each other out, but *do not* share completed code with everyone
  * post on channel for general questions
  * if requiring a private chat/screen share ask on the channel and wait for TA to respond
  * do not be afraid of asking basic questions - there is a wide range of coding experience across the class

---

# Recommended Books

The text for this course is
  
**Python and Matplotlib Essentials for Scientists and Engineers**, 

Matt A. Wood, IOP Publishing 2015

<http://iopscience.iop.org/book/978-1-6270-5620-5>.  

The book is freely available from the Institute of Physics as a pdf or ebook.  

<p class="fragment" style="color:orange;">Note the book is based on Python2 and not Python3</p>

---

# Assessment

+ Is by coursework only. There is no exam!
+ The first five weeks of work are worth 6% per week (total of 30%). 
+ The final five weeks is a single project.
	- Gravitational simulation of an *n*-body gravitational system (Solar System)
	- Two intermediate assessments worth 5% each 
	- Final Report worth 30%
	- Final Project Code worth 30%
	
---

# Coursework Submission

+ All work in the first five weeks will be tested using Moodle via a quizzes and exercises. 
	- There is an unmarked [practice](https://modules.lancaster.ac.uk/mod/quiz/view.php?id=1332841) exercise available to try out. Do this before attempting the actual exercise for grades. 
	- Submission time for first five weeks is 13:00 on Mondays of the following week. 
	- Late submission deadline is before the Tuesday workshop. 
	- Late penalty of one grade level.
	- Announcements made via Moodle and Teams.
	- First four weeks are open for submission from today (week five to follow shortly!)
+ If you need an extension/have a problem contact Brooke, myself or Louise Crook <louise.crook@lancaster.ac.uk>. 
	- email or Teams is preferred to Moodle messages (which can get lost)
	- If you have a problem come and talk to Brooke or I. 
	
---

# Why Python?
 
+ Python is now becoming a popular language in High School. You
  are more likely to have experience which we can build on.
+ Python is currently one of the most used languages in industry (see e.g., the
  [IEEE Spectrum report](https://spectrum.ieee.org/static/interactive-the-top-programming-languages-2019)).  
+ Python is currently used by many more academics in the department. 
+ There are a huge number of resources out there (<https://wiki.python.org/moin/NumericAndScientific>). 

---

# Why Python?

In the [TIOBE](https://www.tiobe.com/tiobe-index/) index Python popularity and usage is still
growing:

| Sep 2020 | Sep 2019 | Programming Language | Ratings | Change |
| -------- | -------- | -------------------- | ------- | ------ |
| 1	| 2 | C | 15.95% | +0.74% |
| 2	| 1	| Java | 13.48% | -3.18% |
| 3 | 3	| Python | 10.47% | +0.59% |
| 4 | 4 | C++ | 7.11% | +1.48% |
| 5 | 5	| C# | 4.58% | +1.18% |
| 6 | 6	| Visual Basic | 4.12% | +0.83% |

---

# Why Python?

1. It is portable - Python programs run on most computer systems in use today;
2. It is freely available;
3. It is widely used;
4. A large number of numerical and scientific toolkits are available;
	- it is extensively used in Physics 
	- NumPy, Matplotlib, SciPy
5. Modern data science applications use Python as an interface 
	- driving the growth.
 
---

# Which Python 

+ Installing/using Python 3.6, 3.7, or 3.8 is acceptable (Python2 is not acceptable)
+ Recommend installing Python using [Anaconda](https://www.anaconda.com/distribution/)
   * <http://ma.ttpitk.in/teaching/PHYS281/demo-anaconda/>
+ By default Anaconda has the following modules required for the computing labs
	- **NumPy** <https://pypi.org/project/numpy/>
	- **SciPy** <https://pypi.org/project/scipy/>
	- **Matplotlib** <https://pypi.org/project/matplotlib/>

---

# Which Editor 

-  Recommend using [**Microsoft Visual Studio Code**](https://code.visualstudio.com/)
   * <http://ma.ttpitk.in/teaching/PHYS281/demo-vs-code/>
   * Comes with terminal integration
   * Code Checking
   * Debugger 
   * Auto completion
   * Auto Indentation 
   * Choose Colour Themes and Font sizes that suit you

---

# Backup Your Code

- Use OneDrive or some other backup system or version control software.
	+ No excuses for lost work. 

---

# Week 1

## Quizzes 

- A quiz on Moodle  

## Exercises 

1. Complete the Hello World exercise.
2. Complete Euler's Formula exercise.
3. Complete the trig results exercise.

---

## Week 1 quizzes

* Using Python as a Calculator.
	+ Make sure you do not include the prompt
	+ Copy the exact answer (no rounding or guessing)

* Multiple-choice introductory questions.
	+ Check basic knowledge

---

# Week 1 Exercise 1

Create a Python function called `helloWorld` (**note the case**) that prints 

```python
Hello World! 
How are things.
```
to standard output using the `print` function. 

**Aims**

- Use editor to write a Python program. 
- Create your first function. 

---

# Week 1 Exercise 2

Create a Python function called `eulersFormula` that returns the value of Euler's formula

$\Huge{e^{i\pi} + 1}$

using Pythons `cmath` or `math` module.


**Aims**

- Use the editor to write a Python program. 
- Check that you can import functions from libraries 
- Understand accuracy limitations of computer programs. 

---

# Week 1 Exercise 3

Create a Python function called `trigResults` that takes a floating point number, *x*, as an
argument and returns two values using the `a, b` syntax containing the following quantities (in this
exact order)

\begin{eqnarray} {\sin(x)}\\
{ \csc(x) \mathrm{(~cosecant~)}}
\end{eqnarray}

using Pythons `math` library. 

**Aims**

- return a multiple values as the result of a function. 
- Practice using the `math` library. 
