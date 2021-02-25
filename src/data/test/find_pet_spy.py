from typing import Dict, List
from src.domain.models import Pets
from src.domain.test import mock_pet


class FindPetSpy:
    """ Class to define use case: Select Pet """

    def __init__(self, pets_repository: any):
        self.pets_repository = pets_repository
        self.by_pet_id_param = {}
        self.by_user_id_param = {}
        self.by_pet_id_and_user_id_param = {}

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """ Select Pet by Id """

        self.by_pet_id_param["pet_id"] = pet_id
        response = None

        validate_entry = isinstance(pet_id, int)

        if validate_entry:
            response = [mock_pet()]

        return {"Success": validate_entry, "Data": response}
