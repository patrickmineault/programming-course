% Lecture 1 - Python
% Programming for VR I
% Patrick Mineault

# First steps

- Python runs code in interactive mode and in script mode.
- From command line, `python` will start interactive mode
- You get a big old calculator!

```{python}
$ python
Python 3.5.2 (default, Nov 23 2017, 16:37:01)
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 5
6
```

- To exit, Ctrl+D, or type quit()

# Running a script

- Create a file in your favorite editor (Atom, Notepad++, etc.)
- Call it "helloworld.py"
- Write:

```{.python}
print("Hello world!")
```

- Run it in the command line:

```
$ python helloworld.py
Hello world!
```

# Variables

 - Variables hold values
   * Bools (False, True)
   * Integers (- 10, 1, 2, 5, ...)
   * Floats (-1010.1, 0.0, 0.3, 1e81, etc.)
   * String ("Hello", "t", "¯\\_()_/¯")
   * Lists, dicts, object instances, etc.

```{.python}
a = 10
a *= 2
print(a)
b = 15
b = a + b
print(b)
```

# Numbers

  - Calculator: +, -, *, /, %, **
  - Compare: >, <, <=, >=, ==
  - Don't forget the parentheses: ()

```{.python}
gretzky = 99
print((10 ** 2) > gretzky)
```

# Strings

 - `+` concatenates two string pieces

```
h = "Hello"
w = "world!"
print(h + " " + w)
```

# If/else

```{.python}
if 2 + 2 == 4:
  print("Everything is right with the world.")
else:
  print("Mayhem!")
print("The end.")
```

* The indentation is critical!

# Challenge

- I give you a big number, `a = 650`
- Write me a program that prints "gotcha" if `a` is divisible by 7, otherwise
  print "nope"
