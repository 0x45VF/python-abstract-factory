from __future__ import annotations
from abc import ABC, abstractmethod

class Computer(ABC):

    @abstractmethod
    def TurnOn(self):
        pass

    @abstractmethod
    def TurnOff(self):
        pass

class MyComputer(Computer):

    def TurnOn(self):
        self.beep(length=5)

    def TurnOff(self):
        self.beep(length=3)
        
#0x45VF
