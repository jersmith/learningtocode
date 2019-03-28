A brief introduction to coding, for Abi.

1. [Setup](#setup)
    1. [Editor](#editor)
    2. [Language](#language)
    3. [Shell](#shell)
    4. [Source Control](#sourcecontrol)
2. [Expressions](#expressions)
    1. [Numbers](#numbers)
    2. [Booleans](#booleans)
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

|Operator  |Action        |
|:--------:|--------------|
|+         |Addition      |
|-         |Subtraction   |
|*         |Multiplication|
|/         |Division      |

There are actually a few more that we'll ignore for now. And just like in math class, if you can't remember the order to apply the operators, you can always use parenthesis to force them to evaluate in a particular order:

```
(5 + 3) * (2 - 4)   is not 7, but -16
```


## Booleans<a name="booleans"></a>
# Statements<a name="statements"></a>
## Assignments<a name="assignments"></a>
## Conditionals<a name="conditionals"></a>
## Loops<a name="loops"></a>