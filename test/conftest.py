import pytest
from rest_framework.test import APIClient

import factories


@pytest.fixture(scope='module')
def client():
    return APIClient()


def generate_fixture(factoryboy, num):
    @pytest.fixture(scope='function')
    def gen_fixture():
        rv = factoryboy.create_batch(size=num)
        return rv
    return gen_fixture


def inject_fixture(name, factoryboy, num=12):
    globals()[name] = generate_fixture(factoryboy, num)


inject_fixture('users', factories.UserFactory)
