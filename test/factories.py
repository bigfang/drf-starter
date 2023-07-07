import factory
from faker import Factory

from app.account.models import User

faker = Factory.create(locale='zh_CN')


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyFunction(faker.user_name)
    email = factory.LazyFunction(faker.email)

    class Meta:
        model = User
