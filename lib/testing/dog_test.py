#!/usr/bin/env python3

from dog import Dog

import io
import sys

class Dog:
    def __init__(self, name="Unknown", breed="Unknown"):
        self._name = None
        self._breed = None
        self.name = name  # Trigger setter for name validation
        self.breed = breed  # Trigger setter for breed validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")