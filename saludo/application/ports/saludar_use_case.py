from abc import ABC, abstractmethod


class SaludarUseCase(ABC):

    @abstractmethod
    def saludar(self, persona):
        pass