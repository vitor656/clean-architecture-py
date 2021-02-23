from typing import Type, Dict, List
from src.domain.use_cases import RegisterPet as RegisterPetInterface
from src.data.interfaces import PetsRepositoryInterface
from src.data.find_user import FindUser
from src.domain.models import Users, Pets


class RegisterPet(RegisterPetInterface):
    """ Class to define use case: Register Pet """

    def __init__(
        self, pets_repository: Type[PetsRepositoryInterface], find_user: Type[FindUser]
    ):
        self.pets_repository = pets_repository
        self.find_user = find_user

    def register(
        self, name: str, specie: str, user_information: Dict[int, str], age: int = None
    ) -> Dict[bool, Pets]:
        """
        Register Pet

        :param
            - name: pet name
            - specie: tpe of the specie
            - age: age of the pet
            - user_information: Dictionary with user_id and/or user_name
        :return
            - Dictionary with informations for the process
        """

        response = None

        validate_entry = isinstance(name, str) and isinstance(specie, str)
        user = self.__find_user_info(user_information)
        checker = validate_entry and user["Success"]

        if checker:
            response = self.pets_repository.insert_pet(
                name=name, specie=specie, age=age, user_id=user_information["user_id"]
            )

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

        print(user_params)

        if "user_id" in user_params and "user_name" in user_params:
            user_found = self.find_user.by_id_and_name(
                user_information["user_id"], user_information["user_name"]
            )
        elif "user_id" not in user_params and "user_name" in user_params:
            user_found = self.find_user.by_name(user_information["user_name"])
        elif "user_id" in user_params and "user_name" not in user_params:
            user_found = self.find_user.by_id(user_information["user_id"])
        else:
            return {"Success": False, "Data": None}

        return user_found
