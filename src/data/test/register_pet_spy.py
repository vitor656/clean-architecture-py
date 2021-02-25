from typing import Dict, List
from src.domain.test import mock_users, mock_pet
from src.domain.models import Users, Pets


class RegisterPetSpy:
    """ Class to define usecase: Register Pet """

    def __init__(self, pets_repository: any, find_user: any):
        self.pets_repository = pets_repository
        self.find_user = find_user
        self.register_param = {}

    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """ Register Pet """

        self.register_param["name"] = name
        self.register_param["specie"] = specie
        self.register_param["user_information"] = user_information
        self.register_param["age"] = age

        response = None

        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_info(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = mock_pet()

        return {"Success": checker, "Data": response}

    def __find_user_info(
        self, user_information: Dict[int, str]
    ) -> Dict[bool, List[Users]]:
        """
        Check user Info and select User

        :param
            - user_information: Dict with user_id and/or user_name
        :return
            - Dict with the response of the find_user use case
        """

        user_found = None
        user_params = user_information.keys()

        if "user_id" in user_params and "user_name" in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        elif "user_id" not in user_params and "user_name" in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        elif "user_id" in user_params and "user_name" not in user_params:
            user_found = {"Success": True, "Data": mock_users()}
        else:
            return {"Success": False, "Data": None}

        return user_found
