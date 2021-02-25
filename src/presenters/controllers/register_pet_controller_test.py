from faker import Faker
from .register_pet_controller import RegisterPetController
from src.data.test import RegisterPetSpy
from src.infra.test import PetsRepositorySpy
from src.presenters.helpers import HttpRequest


faker = Faker()


def test_route():
    """ Testing route method in RegisterPetController """

    register_pet_use_case = RegisterPetSpy(PetsRepositorySpy(), None)
    register_pet_route = RegisterPetController(register_pet_use_case)

    attributes = {
        "name": faker.word(),
        "specie": "Dog",
        "age": faker.random_number(),
        "user_information": {
            "user_id": faker.random_number(),
            "user_name": faker.word(),
        },
    }

    response = register_pet_route.route(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_pet_use_case.register_param["name"] == attributes["name"]
    assert register_pet_use_case.register_param["specie"] == attributes["specie"]
    assert register_pet_use_case.register_param["age"] == attributes["age"]
    assert (
        register_pet_use_case.register_param["user_information"]
        == attributes["user_information"]
    )

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body
