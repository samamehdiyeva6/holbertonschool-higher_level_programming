#!/usr/bin/python3
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound() -> None:
        ...


class Dog(Animal):
    def sound():
        return "Bark"

class Cat(Animal):
    def sound():
        return "Meow"
