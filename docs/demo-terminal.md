# Using a terminal

As described in the [_VS Code_](../demo-vs-code/index.html) introduction, any Python code that you
write can be run within [_VS Code_](../demo-vs-code/index.html#running-code).

However, it use also useful to know how run code and navigate a file system using a @(terminal)
(sometimes referred to as a Command Prompt window, console or @(shell)). Indeed, a Python code
interpreter can be run interactively via a terminal as will be described in [another
tutorial](../demo-python-terminal/index.html).

A terminal is a text-based window that allows you to type and run commands. There are different
terminal programmes for different operating systems, the most common being:

=== "Windows 10"
    [**PowerShell Prompt**](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/powershell)

    !!! note
        If you have installed [Anaconda](../demo-anaconda/index.html) you should access the
        PowerShell using the "Anaconda PowerShell Prompt", which automatically starts the terminal
        with the ability to run conda commands and within @(virtual environments), instead of the
        standard Windows PowerShell.

    Open this by either:

    * click in the Windows start :fontawesome-brands-windows: button and scroll to find:
        * "Anaconda Powershell Prompt (anaconda3)" within the "Anaconda3 (64-bit)" menu;
        * or "Windows Powershell" within the "Windows Powershell" menu;
    * or, search for "PowerShell" in the search bar and select "Anaconda Powershell prompt" or
      "Windows PowerShell" as required.

    ![Anaconda Powershell](img/anaconda-powershell.png)

    The PowerShell command prompt will generally end in a `>` character and contain the path to the
    current directory.

    The "Anaconda Powershell Prompt" can also be launched from within the
    [_Anaconda Navigator_](../demo-anaconda/index.html#anaconda-navigator).

=== "Mac OS"
    [**Terminal App**](https://support.apple.com/en-gb/guide/terminal/apd5265185d-f365-44cb-8b09-71a064a42125/mac)

    Open this using, either:

    * click on the Launchpad icon, type "Terminal" in the search bar and then click on Terminal;
    * or, in Finder, open the "Applications/Utilities" folder and double click on Terminal.

=== "Linux"
    There are a wide variety of terminal applications that come with different Linux distributions
    and desktop environments.

    In most distributions a terminal can be opened using the key combination ++ctrl+alt+t++,
    although there may also be an icon in a launcher panel, or it can be found through a search functionality.

    ![Linux terminal](img/linuxterminal.png)

    In a Linux terminal there are a variety of different shells that you can use with slightly
    different syntax and abilities (shell's are a coding language within themselves), but on most
    Linux distribution the default shell is called
    [bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)).

    The command prompt will often end with a `$` or `#` character.

Within a terminal the line you input commands onto is called the @(command line) and it starts with
some characters called the @(command prompt) as mentioned above. If you have installed Anaconda, the
command prompt should start with the name of the Anaconda environment in brackets, e.g., `(base)`
for the default environment.

A terminal might sometimes be referred to as a "@(shell)"; the shell is a programme that runs within
the terminal and is what you actually interact with when running commands. Another common term used
to describe a terminal is a "console". Despite subtly different meanings terminal, console and shell
are often used interchangeably.

## Terminal "cheat sheet"

Below we will go through a few of the basic commands, with examples, to help navigate using a
terminal. If there is different syntax between Windows, Mac OS, or Linux these will be given. For
Windows these commands assume you are using the PowerShell (Anaconda or Windows) and not a different
terminal programme.

Two useful features (among others) of a terminal are:

1. command history: the ability to toggle back (and then forward) through previous commands you have
   typed using arrow keys ++up++ and ++down++;
2. tab completions: the ability to autocomplete known command and filename using the tab ++tab++ key.

The examples shown below start with a command prompt character, in these cases either `>` or `$`,
which does not need to be typed.

### Show the current directory path

`pwd`

When you open a terminal there will be a default directory that the command prompt will be based in. To find out what this directory is, if not known, you can run, e.g.:

=== "Windows 10"
    ```bash
    > pwd

    Path
    ----
    C:\Users\username
    ```

=== "Mac OS/Linux"
    ```bash
    $ pwd
    /home/username
    ```

### Change between directories

=== "Windows 10"
    `chdir` or `cd`

=== "Mac OS/Linux"
    `cd`

You can change to a new directory using either its path relative to the current directory you are
in, or using the absolute path, i.e., the full path from the drive or base directory name, e.g.,

```
# move to a directory called level1 within the current directory using its relative path
$ cd level1

# move to a directory called level2 specifying its full path
$ cd C:\Users\username\level2
```

To move down one directory level use two dots, e.g.,:

```bash
$ cd ..
```

### List the contents of a directory

=== "Windows 10"
    `dir` or `ls`

    To list the contents of the current directory (in alphabetical order) use:

    ```
    > dir

        Directory: C:\Users\username

    Mode               LastWriteTime           Length Name
    ----               -------------           ------ ----
    d-----      04/09/2020     16:03                  .conda
    d-----      04/09/2020     19:33                  anaconda3
    -a----      09/09/2020     12:34               10 test.txt
    ```

    The "Mode" shows "`d-----`" for a directory and "`-a----`" for "archive", i.e., a file.

    To list the contents of a particular directory supply either the relative or absolute path, e.g.,:

    ```bash
    > dir C:\Users\username
    ```

=== "Mac OS/Linux"
    `ls`

    To list the contents of the current directory (in alphabetical order) use:

    ```bash
    $ ls
    alphabet.txt
    Bookmarks
    notes.pdf
    ```

    To also list the attributes (e.g., accessibility, creator, file size, date of last change) of
    files and directories use the `-l` flag, e.g.,:

    ```
    $ ls -l
    -rw-r--r--  1 username username    4096 Aug 10 22:06  alphabet.txt
    drwxr-xr-x  2 username username    4096 Jan 12  2018  Bookmarks
    -rw-r--r--  1 username username
    ```
    
    A `d` at the start of the attributes indicates a directory, while a `-` is a file`. The other
    letters (`r`, `w`, and `x`) represent whether, and by whom, the files are readable, writeable
    and executable, respectively.

    To colourise the output, i.e., give files and directories different colors depending on their
    types the `--color=auto` flag can be used.

    To list the contents of a particular directory supply either the relative or absolute path, e.g.,:

    ```bash
    $ ls /home/username
    ```

### Make a new directory

`mkdir`

E.g., make a directory called `Project` in the current directory:

```bash
$ mkdir Project
```

Or, make new directory based on an absolute of relative path, e.g.,:

=== "Windows"
    ```
    > mkdir C:\Users\username\Project
    ```

=== "Mac OS/Linux"
    ```bash
    $ mkdir /home/username/Project
    ```

### Show the content of a text file

=== "Windows 10"
    `more` or `type`

=== "Mac OS/Linux"
    `more`, `less`, or `cat`

    For short files, that can be displayed fully within the terminal window the `more` and `cat`
    essentially commands are equivalent (note that `cat` can actually be used to concatenate the
    content of many files). For longer files `cat` will output the whole content in one go while
    `more` will output just what fits on the screen and the content can be scrolled through with
    the ++enter++ key.

E.g., to show the content of a text file called `numbers.txt` in the current directory, which
contains a column of numbers:

```bash
$ more numbers.txt
1
2
3
4
```

Relative or absolute file paths can be used for files not in the current directory.

### Run a Python script

`python myscript.py` - where `myscript.py` is replace by the name of your Python file (which could
be the relative or full file path including directory location)

### Open an Python terminal session

`python` (see the [Python terminal tutorial](../demo-python-terminal/index.html))

### Open an interactive Python terminal session

`ipython` (see the [IPython tutorial](../demo-python-terminal/index.html#ipython-terminal))