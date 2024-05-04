from faker import Faker

fake = Faker()


class ScooterTestData:
    FAKE_COURIER_CREATION = {"login": fake.user_name(),
                             "password": fake.password(),
                             "firstName": fake.name()
                             }
    FAKE_COURIER_CREATION_ONLY_REQUIRED_FIELDS = {"login": fake.user_name(),
                                                  "password": fake.password(),
                                                  }

    SCOOTER_ORDER_DATA = {
        "firstName": fake.name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": 4,
        "phone": fake.phone_number(),
        "rentTime": 5,
        "deliveryDate": "2024-06-06",
        "comment": "Saske, come back to Konoha"
    }
