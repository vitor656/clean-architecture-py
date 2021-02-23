from faker import Faker
from src.infra.test import PetsRepositorySpy, UserRepositorySpy
from src.data.test import FindUserSpy
from .register import RegisterPet

faker = Faker()


def test_register():
    """  Testing Register method """

    pet_repo = PetsRepositorySpy()
    find_user = FindUserSpy(UserRepositorySpy())
    register_pet = RegisterPet(pet_repo, find_user)

    attributes = {
        "name": faker.name(),
        "specie": faker.name(),
        "age": faker.random_number(digits=1),
        "user_information": {
            "user_id": faker.random_number(digits=5),
            # "user_name": faker.name()
        },
    }

    response = register_pet.register(
        name=attributes["name"],
        specie=attributes["specie"],
        age=attributes["age"],
        user_information=attributes["user_information"],
    )

    # Testing inputs
    assert pet_repo.insert_pets_params["name"] == attributes["name"]
    assert pet_repo.insert_pets_params["specie"] == attributes["specie"]
    assert pet_repo.insert_pets_params["age"] == attributes["age"]

    # Testing FindUser Inputs
    assert find_user.by_id_param["user_id"] == attributes["user_information"]["user_id"]

    # Testing Outputs
    assert response["Success"] is True
    assert response["Data"]
