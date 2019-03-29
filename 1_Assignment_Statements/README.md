# Getting started
Up to this point we've only been typing `python` to get an interactive prompt. Now we want to write some programs into a file and run them. We'll use our editor and the shell to do this. I'll walk you through the first one line-by-line, then you'll try your hand at a couple of problems yourself.

Open your shell and type the following commands.
```
cd c:\
mkdir practice_python
cd practice_python
code .
```
This will create a directory on your hardrive, step inside and then start the Visual Studio Code editor in that directory. The next time you open the editor just click in the Taskbar and it will remember where you were.

If you look in the pane on the left and hover over the `PRACTICE_PYTHON` name you'll see some icons appear. These let you create folders and files in this directory. We want to create a directory first, click this one.

![Add directory](add-directory.PNG)

Name the directory, `1_Assignment_Statements`, create it, then click on it. Now click the icon next to the create folder icon to create a file. Call the file `Problem_0.py`. This will be your first program. Your window should look like this.

![Editor window](problem_0_window.PNG)

You can now type your code in that window (you can close the `Welcome` window).

## Problem 0

To start with we want to take input from the user, append a silly string to it, then print the new string out. Even though we haven't covered functions yet, there are a few built-in functions that will be useful for us now. The first is to get input from the user. Type this into your file:

```python
user_text = input("Enter some text: ")
```
This is an assignment statement where the expression is a function that returns a string. You don't really need to know the details at this point, just recognize that the string you pass to `input` will print on the screen for the user. Once the user types something, then presses enter (very important), your `user_text` variable will hold the string they typed.

Now add a print function call. Your program should now look like this:

```python
user_text = input("Enter some text: ")
print(user_text + " silly string")
```
The `print` function takes whatever string you pass and prints it to the screen. In this case we're taking the string from the user and concatenating `" silly string"` to the end. 

Save your program, and then run it.

To run it, we can open a shell directly in VSCode. Press the `Ctrl` key at the same time as the `` ` `` key to open a shell. You may need to move down into the folder where your program is by typing `cd 1_Assignment_Statements` (`cd` stands for `change directory`).

To run your program, just type `python Problem_0.py`. Here's what your screen should look like:

![VSCode Shell](vs_shell.PNG)

For each problem below, create a new file and follow the same steps to write and run your program.

# Problem 1

In this problem we want to let the user enter a temperature in Fahrenheit and convert it to Celsius.

Here are a couple of hints.
1. When you get the input from the user, remember that it's a string. You can not perform arithmetic on strings, so you will need to convert it to an integer. There is a nice function in Python to do this, like so:
```python
integer_value = int(string_value)
```
There is a simliar function for turning a number into a string. This could come in handy:
```python
string_value = str(number_value)
```

2. You'll need to look up the formula for converting temperature.

Here are some questions to think about:
1. How are you going to test that your solution is correct?
2. What happens if the user types something other than a number in?
3. How could you round the answer to the nearest degree?

# Problem 2

This problem is intended to help you think of variables. 

Imagine a gym floor with squares numbered 1, 2, 3, 4, 5 etc down the middle. There are three people, Bob, Lisa, and Marcy standing on these squares. The numbers go from left to right. Here's what we know:

1. Bob is always 2 squares to the left of Lisa.
2. Marcy is always 5 squares to the right of Bob.

If I tell you which square Lisa is on, tell me which square Bob and Marcy must be on.


