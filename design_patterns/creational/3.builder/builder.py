""""
The Builder design pattern is used for building an object in multiple steps. It’s especially useful when each part of the object, rather than the entire object, needs to be built conditionally. Another situation where the Builder design pattern is suitable is when we can’t know ahead of time which specific part we need to add to our object.


Builder can be summarized as follows:

There’s a Builder class that creates a specific type of object and adds various parts to it. We’ll refer to the output object as Target Object.
The Builder object has various methods to modify Target Object while keeping the implementation of Target Object inaccessible.
The Builder object has a method that needs to be called to produce Target Object once sufficient modifications have been applied to it and it’s ready to be used.
There might also be a Director object, which uses a specific implementation of Builder and is solely responsible for manipulating Builder.


Notes: The Director object isn’t strictly required.

"""
# play and stop button

from abc import ABC, abstractmethod

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


class Player:
    def __init__(self):
        self.play_button: PlayButton = None
        self.stop_button: StopButton = None

class IPlayerBuilder(ABC):
    @abstractmethod
    def add_play_button(self):
        pass

    @abstractmethod
    def add_stop_button(self):
        pass

    @abstractmethod
    def build_player(self) -> Player:
        pass


class WindowsPlayerBuilder(IPlayerBuilder):
    def __init__(self):
        self.player = Player()

    def add_play_button(self):
        self.player.play_button = WindowsPlayButton()

    def add_stop_button(self):
        self.player.stop_button = WindowsStopButton()

    def build_player(self) -> Player:
        return self.player

class PlayerDirector:
    def build_player(self, builder):
        builder.add_play_button()
        builder.add_stop_button()

        return builder.build_player()

# Usage
player_director = PlayerDirector()
player = player_director.build_player(WindowsPlayerBuilder())

# Test
player.play_button.play()
player.stop_button.stop()
