from abc import ABC, abstractmethod
from typing import List
from src.domain.models import Pets


class PetsRepositoryInterface(ABC):
    """ Interface to Pets Repository """

    @abstractmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """ Abstract Method """
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def select_pet(self, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """ Abstract Method """
        raise NotImplementedError("Method not implemented")
