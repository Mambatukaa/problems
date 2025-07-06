"""
Abstract Factory can be summarized as follows:

There are some interfaces or abstract classes, each having multiple concrete implementations. They represent the objects that need to be created (let’s call them Target Objects).
There’s an abstract object (or an interface), known as a Creator, or a Factory that returns abstract versions of Target Objects. Each Target Object type has a creation method inside the Factory object associated with it.
There are multiple concrete implementations of the Factory object, each returning a specific set of the Target Object implementations.
When we need to return a specific set of the Target Object implementations, we initialize a specific implementation of the Factory object and call the creation methods on it.
"""



