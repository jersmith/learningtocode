# Learning to Code

A brief introduction to coding.

1. [Setup](#setup)
    1. [Editor](#editor)
    2. [Language](#language)
    3. [Shell](#shell)
2. [Expressions](#expressions)
    1. [Numbers](#numbers)
    2. [Booleans](#booleans)
    3. [Other Expressions](#otherexpressions)
3. [Statements](#statements)
    1. [Assignments](#assignments)
    2. [Conditionals](#conditionals)
    3. [Loops](#loops)
4. [Strings](#strings)
5. [Lists](#lists)
6. Maps
7. Functions
8. Classes

# Setup<a name="setup"></a>
An introduction to coding should be based on concepts, not language details, so in many ways the choice of language is secondary. But in order to understand concepts, you need to implement them in *some* language, and for many reasons I won't express here, I've chosen Python. We'll focus on concepts, but use Python to express those concepts. You can then apply these concepts to additional languages at your leisure.

## Editor<a name="editor"></a>
For any coding, you'll need an editor. I recommend [Visual Studio Code](https://code.visualstudio.com/download), note that this is not the same as Visual Studio. It runs on Windows, Mac or Linux, has excellent documentation, and a rich ecosystem of addons/plugins so you can tailor it for most languages. This is your primary weapon, and you will spend a lot of time in it. So it pays to take time to learn how it works, create some files, delete some files, play with the themes/search, etc. You'll use this a lot, so pin it to the taskbar.

## Language<a name="language"></a>
Of course you'll need [Python](https://www.python.org/downloads/). Make sure when you install on Windows you allow it to overwrite your path so you can run it from anywhere. While you're downloading it from the python.org site, take a look around. There is a lot of documentation there that will be useful later.

## Shell<a name="shell"></a>
We run Python programs by using the `python` command in a shell. Every OS has one; on Windows you have a few choices. There is the old DOS shell called *cmd* and a much better, more recent shell, called *PowerShell*. A good reason for using PowerShell is that many of the commands that work in other shells (say for Mac, Linux or even DOS) work in PowerShell. You can find PowerShell in the Start menu, under *Windows PowerShell*. Pin this to the taskbar.

And that's enough preamble for now, let's get started!

# Expressions<a name="expressions"></a>
Languages are composed of expressions and statements. An expression is like a phrase, or fragment. It doesn't usually do much on its own but is used heavily in statements. A statement is like a complete sentence. Sentences are composed of phrases, and there are different kinds of statements just like there are grammatically different kinds of sentences.

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

```python
(5 + 3) * (2 - 4)   # is not 7, but -16
```
Expressions that use arithmetic operators and numbers are called *numeric* or *arithmetic* expressions. They work in Python just like in math class. Go ahead and open your shell and type `python`.

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

```python
5 > 3      # evaluates to True
5 < 3      # evaluates to False
5 == 3     # evaluates to False
5 != 3     # evaluates to True
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

```python
4 > 8 and 3 == 3                # evaluates to False
4 > 8 or 3 == 3                 # evaluates to True
10 <= 10 and True               # evaluates to True
1 < 2 and 2 < 3 and 6 + 1 == 7  # evaluates to True
```

All of the operators we have seen so far take two operands, one on each side. The `not` operator only takes one. It negates whatever you put after it. So `not False` would yield True. May not sound very exciting, but it can help structure some complex decision making as we'll see later. For now, just a few examples you can try.

```python
3 > 1 and not 5 == 5          # evaluates to False
not False and not False       # evaluates to True
not True or not True          # evaluates to False
not 6 < 10 or 2 == 3          # evaluates to False
```

## Other Expressions<a name="otherexpressions"></a>

While numeric and logical expressions are the most common, expressions can also be composed from any other type. Both numbers and Booleans are what are known as *primitive* types, because they themselves cannot be composed of anything lower. We'll see how to compose other types using these later, but there is another primitive type you will use frequently, namely the string.

A string is a sequence of characters. In Python you can make a string by just putting characters within double quotation marks.

```python
"This is a string"
"So is this"
"Cat"
"You get the idea"
```

Since an expression evaluates to a value, the most common expressions are just values. 

```python
6                  # this is an expression that evaluates to 6
True               # this is an expression that evaluates to True
"Dog"              # this is an expression that evaluates to "Dog"
```

There are sometimes special operators for certain types that you can use in expressions; not nearly as many as the operators for numbers and Booleans though. An example is the operator to join two strings together (we call this concatenating strings). It's the same operator used for addition with numbers.
```python
"I like " + "dogs"           # this evaluates to "I like dogs"
```

Since the `+` operator is used for addition with numbers as well as concatenation with strings we say it is *overloaded*. This means you have to know the types on either side of the plus to know if you'll get a number or a string. But what happens if you have one of each?

```python
6 + "dog"           # Won't work!
```

Thankfully Python sees these types don't match and will throw an error. Go ahead and try it.

Some languages won't fail, but will instead try converting the types into something *reasonable* and keep chugging. The problem is that what may seem *reasonable* is usually not what you intend, so the error that Python gives is a huge blessing. Usually if you try to do something unreasonable in Python it will graciously fail for you.

That's about it for expressions for now. As we come across useful operators in other contexts I'll try to point them out, but this is more than enough to jump into statements. 

# Statements<a name="statements"></a>

Where expressions are composed of values and operators, statements are very specific and composed of one or more expressions in a particular context. Statements do something. We'll look at the three most common statements now.

## Assignments<a name="assignments"></a>
The *assignment* statement is the most fundamental statement in programming. It is ubiquitious, sublime, and so apparently simple that its nuance can be easily lost if you try to just breeze past it. This is the line where programming starts, so we will be spending some time here. Be patient.

First, an example.

```python
age = 5
```

On the left we have a string, but it's not in double quotes. This means it's not a *string*, it's a *name*. We are introducing a new name in our program called `age`. When we introduce a new name via an assignment, the name represents what we call a *variable*. It's a variable because its value *varies*. We can set it, then reset it, so that it keeps changing.

After the name, you have a single `=` symbol. Note that this is not overloading. In all of the expressions we went through there was never a single `=` by itself. With comparisons there is always another symbol next to the `=`. That's the telltale sign of an assignment, a name followed by a single `=`. That symbol means *set the name to a value*. What value? The value of the expression on the right. 
The expression can be any valid expression.

So the *syntax* of an assignment statement could be described like this:
```
<some name> = <some expression>
```
In Python statements end with a new line. There is no ending semi-colon like some other languages, you simply start a new line. Each statement needs to be on its own line.

Ok, so why would we create a variable and just set its value to 5? So we can use it in another expression!

```python
age = 5
my_age = age + 43
```
In this example there are two variables introduced, `age` and `my_age`. But the expression used to set `my_age` has a variable in it. This is the first time we've seen an expression that has anything but explicit numbers, Booleans or strings. Those explicit numbers, Booleans and strings are called *literals*, because their value is *lilterally* what you see. 

A variable is different. The name represents some value, but you don't necessarily know what that value is just by looking. And just because you know what that value is now, doesn't mean you'll know what its value is later. The value `5` never changes, but the variable `age` can, it just happens to be `5` right now.

Just a few more points to make before we jump into our first programming project. When the name is on the left, it doesn't have to exist yet because you are introducing (or reassigning) the variable. But any name in the expression on the right must have already been introduced or you'll get an error.

```python
my_age = today + 3         # Error! The variable today doesn't exist yet!
```

Finally, when you create a name for a variable it can be almost anything, almost. It can contain letters, digits and underscores, but it must not begin with a digit. Underscores are the conventional way to separate words, for example `my_age` instead of `myage`. There are also a handful of words used by the language that are reserved. Which is why they are called `reserved keywords`. You've already seen a few, `and`, `or` and `not` cannot be used as variable names because they are already used by the language. There are 35 reserved keywords, you can find the list [here](https://docs.python.org/3.7/reference/lexical_analysis.html#identifiers).

That is a lot to cover at once. Now would be a great time to do some coding. If you look in the folder called [1_Assignment_Statements](1_Assignment_Statements) you'll find  all the info you need to practice what we've learned so far with some realish problems. The answers are in that folder as well, but try to solve the problems yourself before comparing how you did it with how I might of done it. Be sure you are really comfortable with those problems before moving on.

## Conditionals<a name="conditionals"></a>
The next type of statement we're going to look at is for making decisions. These kinds of statements are called *conditional* statements because they either execute subsequent statements or not based on a condition. The first such statement we'll look at is the `if` statement. It looks like this:

```
if <condition>:
  <statement block>
```
The keyword `if` is a reserved word. The *condition* is any valid Boolean expression. If this expression evaluates to `True`, then the statement block is executed, otherwise it is skipped.

A statement block is one or more statements grouped together. In some languages they are grouped by putting them inside of brackets `{}`. In Python they are indented from the previous statement, usually by 4 spaces. Since Python uses indentation to mark a block, you have to be pretty careful how you space your code. Notice also the colon at the end of the `if` statement, it's required to mark the end of the `if` and the beginning of the block.

Let's look at a few examples.

```python
x = int(input("Type a number: "))

if x > 5:
    print("You typed a number greater than 5")
```

When you run this, if you type a number greater than 5 the `print` statement will execute, otherwise it will not. Here's another one.

```python
x = input("Type a name: ")

if x == "Andy":
    x = "Handy " + x

print(x)
```

With this one, if you type the name *Andy* it will reassign `x` by putting the string *Handy* in front of the name.

Sometimes we don't want to just skip a statement block if a condition isn't met, we would like to execute a different block instead. This is where the `else` clause comes in. It works like this:

```
if <condition>:
  <statement block>
else:
  <some other statement block>
```

This makes our first example more useful.

```python
x = int(input("Type a number: "))

if x > 5:
    print("You typed a number greater than 5")
else:
    print("You typed a number less than 6")
```

Now we're able to make *binary* decisions. Given some condition, if it's `True` do one thing, and if not do something else. But sometimes we have more than two choices, and this is where the `elif` clause comes in. It's short for *else if*, which is what many other languages use. But Python uses `elif`. It works like this.

```python
name = input("Type a name: ")

if name == "Abi":
    age = 10
elif name == "Berki":
    age = 8
else:
    age = 0

print(age)
```

You may have more than two names to choose from, so you can chain these `elif` clauses as long as you want. The first match will execute, the rest will be skipped.

```python
name = input("Type a name: ")

if name == "Abi":
    age = 10
elif name == "Berki":
    age = 8
elseif name == "Evi":
    age = 4 
elif name == "Noah":
    age = 2
else:
    age = 0

print(age)
```

This is a very powerful concept, so it's worth some practice. There are some problems you can work through in the [2_If_Statements](2_If_Statements) folder.

## Loops<a name="loops"></a>

If-Statements are powerful for making a decision. Loops are very similar, but instead of executing a block if a condition is true, a loop will execute a block then check the condition again. If the condition is still true, it will execute it again. It will keep doing this until the condition is false. The simplest loop is the *while* loop, it looks like this.

```python
while <condition>:
    <statement block>
```

It's important to realize that the statement block should update the condition so that it eventually returns False. Otherwise you have what's known as an infinite loop. When your program goes into an infinite loop, you will need to press Ctrl-C to stop it (this will kill your program and exit Python). To see what this is like, try running this program:

```python
while True:
    print("This won't stop, press Ctrl-C")
```

The easiest conditions to check are with numbers. Here's a program that will print the first 10 powers of 2.

```python
start = 1
power = 0
while power < 10:
  print(start)
  start = start * 2
  power = power + 1
```

Notice the pattern here; there is a condition variable *power*, it gets initialized, checked, then modified. This is a very common pattern for writing loops.

We can use this approach with other types and conditions, not just numbers. Here's a program to generate a random 10-digit phone number. It uses a special build in command to generate a random number, but pay attention to the loop.

```python
# we have to import random to use this command
import random

phone_number = ""

# The len() command tells us how long a string is
while len(phone_number) < 10:
  # The randint function takes a start and stop range, and returns a random
  # integer in that range
  phone_number = phone_number + str(random.randint(0, 9))

print(phone_number)
```

Time to practice. Try the problems in the [3_Loop_Statements](3_Loop_Statements) folder.

# Strings<a name="strings"></a>

So far we've been dealing mostly with numbers and Booleans. Strings are another built-in type and they are just as important as Numbers and Booleans, but how to manipulate them may seem a little strange at first. In this section we'll cover the basics.

Strings can be thought of as a sequence of individual characters. The string "cat" has three characters, "c", "a", "t". We say *characters* instead of *letters* because letters imply only those characters used to write words. In the Latin alphabet, letters are "a" through "z", as well as the upper case letters "A" through "Z". Characters can be digits as well, "0" through "9", or punctuation marks like "," or ":". We use the term *character* generically to mean any of these. In Python they may be characters from non-Latin character sets as well, such as Cyrilic or Arabic. 

Python does not have a separate type for characters, just strings. So "cat" is a string of length 3, "c" is a string of length 1. Strings can be created with double quotes or single quotes. It's useful to use one if your string will contain the other.

```python
string1 = "This string isn't in single quotes"
string2 = 'He said "she had it" before I did'
```

Strings are *immutable*, which means once created they cannot be changed. When we manipulate strings, we typically create new strings from existing ones. Let's say you wanted to check if a word started with the letter "c".

```python
string1 = "cat"
string2 = "able"

if (string1[0] == "a"):
  print("starts with a") # does not print

if (string2[0] == "a"):
  print("starts with a") # this one prints
```

In this example we can get the specific character in a string by using the `[]` brackets to *index* the String. The first character is at index 0, the second character is at index 1, and so on. When we index a string like this, we get a new string with just the character at that index. The original string is unmodified.





# Lists<a name="lists"></a>

We've talked about three types so far: numbers, booleans, and strings. These are built-in, primitive types. Now we're going to talk about another built-in type that is used to hold more than one value at a time; the *List*. This isn't a primitive type, but a *collection* type. It's used to collect things, in an order.

You can think of a list as a container where you have to line all of the things it contains up in a line. You can then consider the first item, the second item, the last item and so on. What are the items? Anything you can assign to a variable! 

Here's an example of a list of numbers:

```python
[5, 6, 10, 11]
```
We create a literal list using square brackets, and putting values inside separated by commas.

Since a list is a type, when we create a list, we create a value. This means we can assign a list to a variable.

```python
ages = [12, 10, 8, 2]
```

We can now do things to the list by using the variable. We can see how many things are in the list by using *len*:

```python
ages = [12, 10, 8, 2]

print( len(ages) ) # prints 4
```

We can change the items in the list by assigning different values to them by *indexing* the variable with a number, in square brackets. The number is which element in the list to change. We start the indexing with the number zero, which is the first element. The number one is then the second element, and so on.

```python
ages = [12, 10, 8, 2]
ages[0] = 6
ages[2] = 4

print( ages ) # prints [6, 10, 4, 2]
```

We can add a new item to the end of the list by calling *append*.

```python
ages = [12, 10, 8, 2]
ages.append(23)

print( ages ) # prints [12, 10, 8, 2, 23]
```

Notice how we use the period to call *append* and how this is different than how we called *len* to get the size of the List. They are both examples of built-in *functions*, we'll learn how to write our own later. But a function is like a command, you do it to something. In the case of *len*, it's a global function and you pass in the thing you want to get the length of. We'll see later you can get the length of other things besides lists this way. We've been using *print* and *input* which are global functions as well. But *append* is a function that works specifically on lists. You have to have a list, then use the period followed by *append* to append something to a specific list. 

There are other functions you can call on lists:

```python
ages = [12, 10, 8, 6]
ages.clear()    # the list is now empty
print( ages )   # prints []

ages.append(5)
ages.append(10)
ages.append(15)

print( ages )   # prints [5, 10, 15]

ages.insert(1, 25) # inserts 25 at index 1
print( ages )      # prints [5, 25, 10, 15]

firstAge = ages.pop(0)  # removes the item at index 0 and returns it
print( firstAge )       # prints 5
print( ages )           # prints [25, 10, 15]

ages[len(ages) - 1] = 99  # set the last item to 99
print( ages )             # 
```





