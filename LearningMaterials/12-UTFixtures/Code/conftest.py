import pytest # type: ignore

# Fixture to create a sample address book
@pytest.fixture
def sample_address_book():
    address_book = {
        'Alice': 'alice@example.com',
        'Bob': 'bob@example.com',
        'Charlie': 'charlie@example.com',
        'David': 'david@example.com',
        'Eve': 'eve@example.com',
        'Frank': 'frank@example.com',
        'Grace': 'grace@example.com',
        'Hannah': 'hannah@example.com',
        'Ivan': 'ivan@example.com',
        'Jack': 'jack@example.com',
        'Kate': 'kate@example.com',
        'Liam': 'liam@example.com',
        'Molly': 'molly@example.com',
        'Nancy': 'nancy@example.com',
        'Oscar': 'oscar@example.com',
        'Peter': 'peter@example.com',
        'Quinn': 'quinn@example.com',
        'Rachel': 'rachel@example.com',
        'Steve': 'steve@example.com',
        'Tina': 'tina@example.com',
        'Ursula': 'ursula@example.com',
        'Victoria': 'victoria@example.com',
        'Walter': 'walter@example.com',
        'Xavier': 'xavier@example.com',
        'Yvonne': 'yvonne@example.com',
        'Zack': 'zack@example.com'
    }
    return address_book