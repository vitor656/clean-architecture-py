from faker import Faker
from src.infra.config import DBConnectionHandler
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
