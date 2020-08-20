# Reading and writing data

A code might require input data and it might also create data for outputting. Therefore it is useful
to be able to read and write data from and to a file.

Files can either contain plain [ascii text](https://en.wikipedia.org/wiki/ASCII), i.e., text that is
readable if the file is opened with a standard text editor, or information that is in a binary
format (generally this is not readable by standard editor unless the format is known).

Plain text files are useful, in that they are human readable, although for the same amount of
information they will generally be larger in size (i.e., memory taken up on disc) than an equivalent
binary file.

## Basic reading and writing to file (ascii text only)

The built-in Python function [`open`](https://docs.python.org/3/library/functions.html#open)
provides a way to open files and make them ready for reading their content or writing to them.

When using `open` it requires the name of the file to open and the "mode", i.e., whether to open the
file for reading (mode `"r"`), writing (mode `"w"`), or appending (mode `"a"`). It returns a [file
object](https://docs.python.org/3/glossary.html#term-file-object).

### Reading

Suppose you have a plain text file called `mydata.txt` in your current directory containing some
numerical data (this will be used in further examples):

```
--8<-- "docs/mydata.txt"
```

The first line starts with a `#` and is comment line a giving the "names" of the columns. The two
columns can be read into two lists with using the following code:

```python
fp = open("mydata.txt", "r")  # open mydata.txt for "r"eading
x = []  # empty list to contain x data
y = []  # empty list to contain y data
for line in fp.readlines():  # loop through each line in the data
    if line[0] == "#":
       # skip lines that start with a "#"
       continue
    data = line.split()  # split the line on any whitespace
    x.append(float(data[0]))  # convert string into float
    y.append(float(data[1]))

fp.close()  # close the file

print(x)
print(y)
[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
[9.8, 10.3, 12.4, 13.2, 14.7, 16.1, 17.2, 18.7, 20.1, 21.3]
```

In this [`readlines`](https://www.w3schools.com/python/ref_file_readlines.asp) is a method of the
file object. It goes through the file and returns a list, where each entry is a string containing a
line from the file.

When reading data in this way you must know what the data file looks like.

## pickling

Allows classes to be saved.

## JSON

Writing to a JSON format file

## NumPy