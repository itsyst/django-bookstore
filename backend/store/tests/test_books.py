from rest_framework import status
from store.models import Genre
from model_bakery import baker
import pytest


@pytest.fixture
def create_book(api_client):
    def do_create_book(book):  #We don't pass the genre as a parameter because it's not recognized by the fixture.
        return api_client.post('/books/', book)
    return do_create_book

@pytest.mark.django_db
class TestCreateBook:
    def test_if_data_is_valid_retruns_201(self, authenticate, create_book):
        #Arrange
        authenticate(is_staff=True)
        genre = baker.make(Genre)
        
        #Act
        response = create_book({
            'ISBN': '6546546596888',
            'title': 'king++',
            'number_in_stock': 10,
            'daily_rate': 2,
            'genre': genre.id,
            'description': 'some description',
            'unit_price': 120
        })
        print(response.json())

        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0