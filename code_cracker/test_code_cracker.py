# encoding: utf-8
import pytest

from code_cracker_code import code_cracker, reverse_code_cracker, CRACKER


@pytest.fixture
def hidden_message():
    return '&/aad ldga('


@pytest.fixture
def cracked_message():
    return 'hello world'


def test_should_return_string(hidden_message):
    response = code_cracker(hidden_message)

    assert isinstance(response, str)


def test_should_return_same_size_message(hidden_message):
    response = code_cracker(hidden_message)

    assert len(response) == len(hidden_message)


def test_should_return_message_with_specific_chars(hidden_message):
    response = code_cracker(hidden_message)

    for c in response.replace(' ', ''):
         assert c in CRACKER.values()


def test_should_return_expected_cracked_message(
    hidden_message, 
    cracked_message
):
    response = code_cracker(hidden_message)

    assert response == cracked_message


def test_should_return_string_for_reverse_method(cracked_message):
    response = reverse_code_cracker(cracked_message)

    assert isinstance(response, str)


def test_should_return_same_size_message_for_reverse_method(cracked_message):
    response = reverse_code_cracker(cracked_message)

    assert len(response) == len(cracked_message)


def test_should_return_message_with_specific_chars_for_reverse_method(
    cracked_message
):
    response = reverse_code_cracker(cracked_message)

    for c in response.replace(' ', ''):
         assert c in CRACKER.keys()


def test_should_return_expected_hidden_message_for_reverse_method(
    hidden_message, 
    cracked_message
):
    response = reverse_code_cracker(cracked_message)

    assert response == hidden_message