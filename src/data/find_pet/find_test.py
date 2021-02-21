from faker import Faker
from src.infra.test import PetsRepositorySpy
from .find import FindPet

faker = Faker()


def test_by_pet_id():
    """ Testing pet_id method in FindPet """

    pets_repo = PetsRepositorySpy()
    find_pet = FindPet(pets_repo)

    attributes = {"pet_id": faker.random_number(digits=2)}

    response = find_pet.by_pet_id(pet_id=attributes["pet_id"])

    # Testing Inputs
    assert pets_repo.select_pets_params["pet_id"] == attributes["pet_id"]

    # Testing outputs
    assert response["Success"] is True
    assert response["Data"]
