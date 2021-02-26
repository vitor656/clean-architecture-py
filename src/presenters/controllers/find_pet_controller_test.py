from faker import Faker
from .find_pet_controller import FindPetController
from src.infra.test import PetsRepositorySpy
from src.data.test import FindPetSpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handle():
    """ Testing handle method """

    find_pet_use_case = FindPetSpy(PetsRepositorySpy())
    find_pet_controller = FindPetController(find_pet_use_case)
    http_request = HttpRequest(query={"pet_id": faker.random_number()})

    response = find_pet_controller.route(http_request)

    # Testing Inputs
    assert find_pet_use_case.by_pet_id_param["pet_id"] == http_request.query["pet_id"]

    # Testing Outputs
    assert response.status_code == 200
    assert response.body
