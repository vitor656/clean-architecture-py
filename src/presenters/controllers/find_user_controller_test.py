from faker import Faker
from .find_user_controller import FindUserController
from src.data.test import FindUserSpy
from src.infra.test import UserRepositorySpy
from src.presenters.helpers import HttpRequest

faker = Faker()


def test_handle():
    """ Testing handle method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest(query={"user_id": faker.random_number()})

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_param["user_id"] == http_request.query["user_id"]

    # Testing Output
    assert response.status_code == 200
    assert response.body


def test_handle_no_query_param():
    """ Testing handle method """

    find_user_use_case = FindUserSpy(UserRepositorySpy())
    find_user_controller = FindUserController(find_user_use_case)
    http_request = HttpRequest()

    response = find_user_controller.route(http_request)

    # Testing Inputs
    assert find_user_use_case.by_id_param == {}

    # Testing Output
    assert response.status_code == 400
    assert "error" in response.body
