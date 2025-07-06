"""
The Prototype design pattern allows us to easily clone existing objects. Instead of copying all the data from one object to another field by field, we just have a method to clone the object inside the object itself.

This has two core advantages. Firstly, all of our code for copying an object resides in a single place in our code base, which enforces the don’t repeat yourself (DRY) principle. Secondly, it allows us to copy private fields into the new object, which we wouldn’t have been able to do at all if we just did a field-by-field copying.

The Prototype pattern can be summarized as follows:

A class has a method that returns an exact copy of the instance of the class.
This method may be called Clone or Copy.
This method performs a field-by-field copy of the class, including its private fields.
But even though the object that this method returns has the same values in all of its fields as the original object, it’s a completely different object reference, so modifying it won’t change the original object.

"""


from abc import abstractmethod, ABC
import copy
import random


class ICloneable(ABC):
    @abstractmethod
    def clone(self):
        pass


class CloneableObject(ICloneable):
    def __init__(self, name):
        self.id = random.randint(1, 100)
        self.name = name

    def clone(self):
        #return copy.deepcopy(self)
        clone = CloneableObject(self.name)
        clone.id = self.id
        return clone


obj1 = CloneableObject("Object 1")

obj2 = obj1.clone()


print(obj1.id, obj1.name)
print(obj2.id, obj2.name)
