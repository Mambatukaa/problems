import asyncio
from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def play(self, fileName):
        pass


class PlayerCreator(ABC):
    @ abstractmethod
    def createPlayer(self) -> Player:
        pass


class WindowsPlayer(Player):
    """ overriding the play method"""
    async def play(self, fileName):
            print(f"Loading {fileName}...")
            await asyncio.sleep(2)
            print("Playing finished.")

class LinuxPlayer(Player):
    """ overriding the play method"""
    def play(self, fileName):
        print(f"LinuxPlayer playing: {fileName}")


class WindowsPlayerCreator(PlayerCreator):
    """ overriding the createPlayer method"""
    def createPlayer(self):
        return WindowsPlayer()



creator = WindowsPlayerCreator()
player = creator.createPlayer()
asyncio.run(player.play("song.mp3"))


