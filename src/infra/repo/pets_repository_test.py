from faker import Faker
from src.infra.config import DBConnectionHandler
from src.infra.entities.pets import AnimalTypes
from src.infra.entities import Pets as PetsModel
from .pets_repository import PetsRepository

faker = Faker()
pets_repository = PetsRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """ Should insert pet in Pet table and return it """

    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    # SQL Commands
    new_pet = pets_repository.insert_pet(name, specie, age, user_id)

    engine = db_connection_handler.get_engine()

    query_pet = engine.execute(
        "SELECT * FROM pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    assert new_pet.id == query_pet.id
    assert new_pet.name == query_pet.name
    assert new_pet.specie == query_pet.specie
    assert new_pet.age == query_pet.age
    assert new_pet.user_id == query_pet.user_id

    engine.execute("DELETE FROM pets WHERE id='{}'".format(new_pet.id))


def test_select_pet():
    """ Should select a pet in PetsRepository and compare it """

    pet_id = faker.random_number(digits=4)
    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()

    specie_mock = AnimalTypes("fish")
    data = PetsModel(id=pet_id, name=name, specie=specie_mock, age=age, user_id=user_id)

    # SQL Commands

    engine = db_connection_handler.get_engine()
    engine.execute(
        "INSERT INTO pets (id, name, specie, age, user_id) VALUES ('{}', '{}', '{}', '{}' ,'{}');".format(
            pet_id, name, specie, age, user_id
        )
    )

    query_pets1 = pets_repository.select_pet(pet_id=pet_id)
    query_pets2 = pets_repository.select_pet(user_id=user_id)
    query_pets3 = pets_repository.select_pet(pet_id=pet_id, user_id=user_id)

    assert data in query_pets1
    assert data in query_pets2
    assert data in query_pets3

    engine.execute("DELETE FROM pets WHERE id='{}';".format(pet_id))
