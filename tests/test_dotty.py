from __future__ import annotations

import pytest

from dotty import Dotty


@pytest.fixture
def dotty_data_simple():
    return {
        "foo": "bar",
        "bin": 1,
        "test": True,
    }


@pytest.fixture
def dotty_data_complex():
    return {
        "bin": {
            "test": True,
            "hello": {
                "world": 1,
            },
        },
    }


def test_key_error(dotty_data_simple):
    dotty_instance = Dotty(dotty_data_simple)
    with pytest.raises(KeyError):
        dotty_instance.missing_key


def test_simple_data(dotty_data_simple):
    dotty_instance = Dotty(dotty_data_simple)
    assert dotty_instance.foo == "bar"
    assert type(dotty_instance.foo) == str

    assert dotty_instance.bin == 1
    assert type(dotty_instance.bin) == int

    assert dotty_instance.test == True
    assert type(dotty_instance.test) == bool


def test_complex_data(dotty_data_complex):
    dotty_instance = Dotty(dotty_data_complex)

    assert type(dotty_instance.bin) == Dotty
    assert type(dotty_instance.bin.hello) == Dotty
    assert dotty_instance.bin.test == True
    assert dotty_instance.bin.hello.world == 1


def test_json(dotty_data_complex):
    dotty_instance = Dotty(dotty_data_complex)
    json_string = '{"bin": {"test": true, "hello": {"world": 1}}}'
    assert dotty_instance.json() == json_string
