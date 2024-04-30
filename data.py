from faker import Faker

fake = Faker()


class ScooterTestData:
    COURIER_CREATION = {"login": fake.user_name(),
                        "password": fake.password(),
                        "firstName": fake.name()
                        }
    COURIER_CREATION_ONLY_REQUIRED_FIELDS = {"login": fake.user_name(),
                                             "password": fake.password(),
                                             }
    COURIER_CREATION_ONE_REQUIRED_FIELD_MISS = {"login": fake.user_name()
                                             }