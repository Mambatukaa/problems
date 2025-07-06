"""
Abstract Factory can be summarized as follows:

There are some interfaces or abstract classes, each having multiple concrete implementations. They represent the objects that need to be created (let’s call them Target Objects).
There’s an abstract object (or an interface), known as a Creator, or a Factory that returns abstract versions of Target Objects. Each Target Object type has a creation method inside the Factory object associated with it.
There are multiple concrete implementations of the Factory object, each returning a specific set of the Target Object implementations.
When we need to return a specific set of the Target Object implementations, we initialize a specific implementation of the Factory object and call the creation methods on it.



Family related objects in one go
"""



# play and stop button

from abc import ABC, abstractmethod



class WindowsPlayerUtility:
    def Start(self):
        print("starting")


class LinuxPlayerUtility:
    def Start(self):
        print("starting")

class PlayButton(ABC):
    @abstractmethod
    def play(self):
        pass

class StopButton(ABC):
    @abstractmethod
    def stop(self):
        pass


class WindowsPlayButton(PlayButton):
    def play(self):
        print("Windows playing")

class LinuxPlayButton(PlayButton):
    def play(self):
        print("Linux playing")

class WindowsStopButton(StopButton):
    def stop(self):
        print("Windows stopping")

class LinuxStopButton(StopButton):
    def stop(self):
        print("Linux stopping")

class PlayerCreator(ABC):
    @abstractmethod
    def createPlayButton(self) -> PlayButton:
        pass

    @abstractmethod
    def createStopButton(self) -> StopButton:
        pass


class WindowsPlayerCreator(PlayerCreator):
    def createPlayButton(self):
        return WindowsPlayButton()

    def createStopButton(self):
        return WindowsStopButton()

class LinuxPlayerCreator(PlayerCreator):
    def createPlayButton(self):
        return LinuxPlayButton()

    def createStopButton(self):
        return LinuxStopButton()
