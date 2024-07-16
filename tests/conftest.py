import pytest

from src.processing import filter_by_state, list_of_dict, sort_by_date


@pytest.fixture
def test_list_of_dict():
    return "EXECUTED"


@pytest.fixture
def test_list_of_dict_1():
    return list_of_dict
