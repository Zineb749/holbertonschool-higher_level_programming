#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal:
    @abstractmethod
    def sound(self):
        pass


class dog(Animal):
    def sound(self):
        return 'Bark'


class cat(Animal):
    def sound(self):
        return 'Meow'
