"""
In Python, there are two common approaches to factories, as follows:

We define a function that creates objects of the required classes.

We define a class that has methods for creating objects. This is the Factory
design pattern, as described in books on object-oriented design patterns. In
languages such as Java, a factory class hierarchy is required because the
language doesn't support standalone functions.

In Python, a class isn't required to create an object factory, but this can be a good
idea when there are related factories or factories that are complex. One of the
strengths of Python is that we're not forced to use a class hierarchy when a
simple function might do just as well
"""

