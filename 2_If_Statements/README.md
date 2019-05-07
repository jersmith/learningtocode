# If-Statement problems

## Problem 1

In this problem we are going to solve a common problem: checking to see if a number is odd or even. If you think about how you would do this in your head, you would divide the number by two and see if it divides evenly. So how do we do that?

Let's see what happens when we divide a number by two. Open your Python shell and type an expession that divides an even number by two.

```powershell
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 8 / 2
4.0
```

Now try an odd number:

```powershell
>>> 9 / 2
4.5
```

Notice in both cases we get a number with a decimal point, even if the value comes out even (eg 4.0). This means the number is not an integer, it's a decimal number (also called a *floating point* number, or *float*). In Python, whenever you use division, the answer will *always* be a decimal number. But what we really want are two integers: the number of times our number can be divided by two, and the *remainder* that is left over.

Python has two special arithmetic operators to give us just that. If you just want the number of times a number divides into another, without any decimal parts, you can use *//*; this is called the *integer division* operator.

```python
9 // 2      # this will return 4, not 4.5
```

We could use this to see if a number is even. Could you guess how? Write a short program that takes a number as input from the user and print "Even" if the number is even or "Odd" if the number is odd.

## Problem 2

To get just the remainder, we can use th *%* operator; this is called the *modulo* operator.

```python
9 % 2       # this will be 1, why?
8 % 2       # this will be 0
9 % 3       # this will also be 0
```

This makes it even easier to determine if a number is odd or even. Update your previous program to use th *%* operator.

## Problem 3

Let's say we number the days of the week starting from 0. So Sunday is zero, Monday is one, up to Saturday which we'll call 6.

Let the user enter a number for the day of the week, then another number of days to add to this day. You need to tell the user which day of the week their new day falls on.

Here's an example of a correct program running:

```powershell
Enter a day of week (0 - 6): 5
Enter days to add: 4
Next day is: 2
```

Another test case you should try is adding 50 days.

## Problem 4

As a twist on problem 3, instead of printing the next day of the week, print whether it falls on a weekday or weekend (Saturday or Sunday).