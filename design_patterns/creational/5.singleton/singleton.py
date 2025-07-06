""""
The Singleton design pattern allows us to use a single instance of a particular object throughout our application. This is achieved with the help of a private constructor and a static method that can call this constructor from the outside.

Singleton can be summarized as follows:

A Singleton class that’s meant to be used as a single instance that’s shared throughout an application has a private constructor, so it can only be created inside of the class itself.
The class holds a private static field containing its own data type.
To instantiate the class from the outside, the class has a static method that returns the same data type as the class itself.
This method will create an instance of the class via the private constructor and populate the private static field with this instance. Then, this instance would be returned to the caller.
Any subsequent calls will just return the object instance that was already created.
We can understand the concept of the Singleton design pattern better through the following illustration:

"""



class Singleton():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls) # creates actual object in memory
        return cls._instance

    def __init__(self):
        self.value = 42


singleton = Singleton()
singleton2 = Singleton()


print(singleton.value, singleton2.value)
