from faker import Faker
from .register_user_controller import RegisterUserConstroller
from src.presenters.helpers import HttpRequest
from src.infra.test import UserRepositorySpy
from src.data.test import RegisterUserSpy

faker = Faker()


def test_route():
    """ Testing route for user registering """

    register_user_use_case = RegisterUserSpy(UserRepositorySpy())
    register_user_controller = RegisterUserConstroller(register_user_use_case)

    attributes = {"name": faker.name(), "password": faker.word()}

    response = register_user_controller.route(HttpRequest(body=attributes))

    # Testing Inputs
    assert register_user_use_case.register_param["name"] == attributes["name"]
    assert register_user_use_case.register_param["password"] == attributes["password"]

    # Testing Outputs
    assert response.status_code == 200
    assert "error" not in response.body
