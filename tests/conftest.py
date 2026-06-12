import pytest


@pytest.fixture(scope = "function")
def say_hello():
    print("Hello World!")
    return 14

@pytest.fixture(scope = "session") # нужен для того чтобы подрубиться к БД один раз и дальше переиспользовать ее
def say_hello_session():
    print("Hello World!")