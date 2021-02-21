from typing import Type, Dict, List
from src.domain.models import Pets
from src.data.interfaces import PetsRepositoryInterface
from src.domain.use_cases import FindPet as FindPetInterface


class FindPet(FindPetInterface):
    """ Class to define use case Find Pet """

    def __init__(self, pets_repository: Type[PetsRepositoryInterface]):
        self.pets_repository = pets_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Select Pet by id

        :param
            - pet_id: id of the Pet
        :return
            - Dictionary with info of the process
        """

        response = None
        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = self.pets_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """
        Select Pet by user_id

        :param
            - user_id: id of the owner
        :return
            - Dictionary with info of the process
        """

        response = None
        validate_entry = isinstance(user_id, int)

        if validate_entry:
            response = self.pets_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(
        self, pet_id: int, user_id: int
    ) -> Dict[bool, List[Pets]]:
        """
        Select Pet by id and user_id

        :param
            - pet_id: id of the pet
            - user_id: id of the owner
        :return
            - Dictionary with info of the process
        """

        response = None
        validate_entry = isinstance(user_id, int) and isinstance(pet_id, int)

        if validate_entry:
            response = self.pets_repository.select_pet(user_id=user_id, pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}
