from faker import Faker

fake = Faker()


def create_user_data():
    payload = {
        "email": f"{fake.uuid4()}{fake.email()}",
        "password": f"{fake.random_int()}",
        "name": f"{fake.first_name()}{fake.uuid4()}"
    }
    return payload


user_data = create_user_data()