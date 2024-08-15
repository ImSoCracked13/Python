from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, max_speed = 0, color = '', model = ''):
        self._max_speed = max_speed # km/h
        self._color = color
        self._model = model

    @property
    @abstractmethod
    def fuel_effiency(self):
        pass

    def __str__(self):
        return f'max speed: {self._max_speed} - color: {self._color} - model: {self._model}'