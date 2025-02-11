from abc import ABC, abstractmethod
from typing import Dict, List
from src.domain.models import Users


class FindUser(ABC):
    """ Interface to FindUser use case """

    @abstractmethod
    def by_id(self, user_id: int) -> Dict[bool, List[Users]]:
        """ Sepecific Case """
        raise NotImplementedError("Should implement method: by_id")

    @abstractmethod
    def by_name(self, name: str) -> Dict[bool, List[Users]]:
        """ Sepecific Case """
        raise NotImplementedError("Should implement method: by_name")

    @abstractmethod
    def by_id_and_name(self, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """ Sepecific Case """
        raise NotImplementedError("Should implement method: by_id_and_name")
