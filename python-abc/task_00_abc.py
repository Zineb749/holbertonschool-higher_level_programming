from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    This class enforces that any subclass must implement the `sound` method.
    """
    @abstractmethod
    def sound(self):
        """Abstract method that should be implemented by
        subclasses to define the animal's sound."""
        pass


class Dog(Animal):
    """Concrete subclass representing a dog.

    Implements the `sound` method to return the sound a dog makes.
    """
    def sound(self):
        return 'Bark'


class Cat(Animal):
    """Concrete subclass representing a cat.
    Implements the `sound` method to return the sound a cat makes.
    """
    def sound(self):
        return 'Meow'
