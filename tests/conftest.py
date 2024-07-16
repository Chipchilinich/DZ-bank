import pytest

from src.processing import list_of_dicts


@pytest.fixture
def test_list_of_dict():
    return "EXECUTED"


@pytest.fixture
def test_list_of_dict_1():
    return list_of_dicts
