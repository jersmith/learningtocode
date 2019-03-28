A brief introduction to coding, for Abi.

1. [Setup](#setup)
    1. [Editor](#editor)
    2. [Language](#language)
    3. [Shell](#shell)
    4. [Source Control](#sourcecontrol)
2. [Expressions](#expressions)
    1. [Numbers](#numbers)
    2. [Booleans](#booleans)
    3. [Other Expressions](#otherexpressions)
3. [Statements](#statements)
    1. [Assignments](#assignments)
    2. [Conditionals](#conditional)
    3. [Loops](#loops)
4. Strings
5. Lists
6. Maps
7. Functions
8. Classes
9. Excercise Index
    1. Guessing Game

# Setup<a name="setup"></a>
An introduction to coding should be based on concepts, not language details, so in many ways the choice of language is secondary. But in order to understand concepts, you need to implement them in *some* language, and for many reasons I won't express here, I've chosen Python. We'll focus on concepts, but use Python to express those concepts. You can then apply these concepts to additional languages at your leisure.

## Editor<a name="editor"></a>
For any coding, you'll need an editor. I recommend [Visual Studio Code](https://code.visualstudio.com/download), note that this is not the same as Visual Studio. It runs on Windows, Mac or Linux, has excellent documentation, and a rich ecosystem of addons/plugins so you can tailor it for most languages. This is your primary weapon, and you will spend a lot of time in it. So it pays to take time to learn how it works, create some files, delete some files, play with the themes/search, etc. You'll use this a lot, so pin it to the taskbar.

## Language<a name="language"></a>
Of course you'll need [Python](https://www.python.org/downloads/). Make sure when you install on Windows you allow it to overwrite your path so you can run it from anywhere. While you're downloading it from the python.org site, take a look around. There is a lot of documentation there that will be useful later.

## Shell<a name="shell"></a>
We run Python programs by using the `python` command in a shell. Every OS has one; on Windows you have a few choices. There is the old DOS shell called *cmd* and a much better, more recent shell, called *PowerShell*. A good reason for using PowerShell is that many of the commands that work in other shells (say for Mac, Linux or even DOS) work in PowerShell. You can find PowerShell in the Start menu, under *Windows PowerShell*. Pin this to the taskbar.

## Source Control<a name="sourcecontrol"></a>
You are reading this on GitHub, which is a good way to learn about source control. As part of the first excercise we'll get you're own repository set up, but for now just sign up for a Github account.

And that's enough preamble for now, let's get started!

# Expressions<a name="expressions"></a>
Languages are composed of expressions and statements. An expression is like a phrase, or fragment. It doesn't usually do much on its own but is used heavily in statements. A statement is like a complete sentance. Sentances are composed of phrases, and there are different kinds of statements just like there are grammatically different kinds of sentances.

Expressions are *evaluated*, which means that after the evaluation you have a value that can be used in a statement.

Statements are *executed*, which means they do something with those values.

We'll look at statements more later, but it's good to have an understanding of expressions first. Let's start with expressions you already know.

## Numbers<a name="numbers"></a>
Believe it or not, this is an expression:
```
5 + 3 * 2 - 4
```
If you saw that on a piece of paper, you could *evaluate* it and obtain the number 7. This expression is composed of numbers and symbols for arithmetic. We call those symbols *operators*, and you already know them for arithmetic:

|Operator  |Meaning       |
|:--------:|--------------|
|+         |Addition      |
|-         |Subtraction   |
|*         |Multiplication|
|/         |Division      |

There are actually a few more that we'll ignore for now. And just like in math class, if you can't remember the order to apply the operators, you can always use parenthesis to force them to evaluate in a particular order:

```
(5 + 3) * (2 - 4)   is not 7, but -16
```
Expressions that use arithmetic operators and numbers are call *numeric* or *arithmetic* expressions. They work in Python just like in math class. Go ahead and open your shell and type `Python`.

This will start the interactive Python interpreter. While not great for running large programs, it's perfect for testing little snippets. Once you start it, it should print out the version and how to get help, then present you with a prompt, something like this:

```
Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
You can type expressions directly at the prompt. Go ahead and try a few with and without parenthesis, pressing enter to evaluate the expression. When you're finished you can type `quit()` followed by enter to exit Python.

## Booleans<a name="booleans"></a>
Arithmetic may look familiar, but Boolean expressions may not. We also call them logical expressions because they are based on Boolean logic. While numbers have lots of values, there are only two Boolean values, *True* and *False*.

Just like arithmetic has operators, there are operators used in Logical expressions as well. Let's start with the *comparison* operators. These let us compare things to each other. In Python, some of them look like this.

|Operator  |Meaning                     |
|:--------:|----------------------------|
|<         |Is less than                |
|>         |Is greater than             |
|==        |Is equal to                 |
|!=        |Is not equal to             |
|<=        |Is less than or equal to    |
|>=        |Is greater than or equal to |

The easiest thing to compare are numbers, so let's look at some examples.

```
5 > 3      evaluates to True
5 < 3      evaluates to False
5 == 3     evaluates to False
5 != 3     evaluates to True
```

You can try this yourself in the interactive Python shell. Remember to type `python` to get it started and `quit()` to exit.

Comparing two values gives us a Boolean value, but we can also combine boolean values using one of the *Logical* operators. 

|Operator  |Meaning                        |
|:--------:|-------------------------------|
|and       |True if both operands are true |
|or        |True if either operand is true |
|not       |Negates a single operand       |

These may look a little strange. If you think about it in English it makes more sense, as these are straight out of Aristotlian Logic. 

Let's say I make a statement like
```
I will jump off this bridge if (today is Tuesday) and (the current time is after 4pm)
```
I added the parenthesis so you could see the operands. If both today is Tuesday AND it is currently after 4pm, I'll jump (True), otherwise, nah. If either condition is False (not true) then the whole thing is not true (False).

The meaning changes if I use *or* instead
```
I will jump off this bridge if (today is Tuesday) or (the current time is after 4pm)
```
Now if either condition is True, I'm jumping. In other words, BOTH conditions have to be False to make the whole thing False. 

We can say this very succinctly with a couple of little tables.

A and B

|A    |B    |Result |
|-----|-----|-------|
|True |True |True   |
|True |False|False  |
|False|True |False  |
|False|False|False  |

A or B

|A    |B    |Result |
|-----|-----|-------|
|True |True |True   |
|True |False|True   |
|False|True |True   |
|False|False|False  |

A few examples with numbers might help. You can type these into your python intepreter to verify.

```
4 > 8 and 3 == 3                evaluates to False
4 > 8 or 3 == 3                 evaluates to True
10 <= 10 and True               evaluates to True
1 < 2 and 2 < 3 and 6 + 1 == 7  evaluates to True
```

All of the operators we have seen so far take two operands, one on each side. The `not` operator only takes one. It negates whatever you put after it. So `not False` would yield True. May not sound very exciting, but it can help structure some complex decision making as we'll see later. For now, just a few examples you can try.

```
3 > 1 and not 5 == 5          evaluates to False
not False and not False       evaluates to True
not True or not True          evaluates to False
not 6 < 10 or 2 == 3          evaluates to False
```

## Other Expressions<a name="otherexpressions"></a>

# Statements<a name="statements"></a>
## Assignments<a name="assignments"></a>
## Conditionals<a name="conditionals"></a>
## Loops<a name="loops"></a>