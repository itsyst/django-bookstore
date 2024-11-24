from rest_framework import status
import pytest


@pytest.fixture
def create_genre(api_client):
    def do_create_genre(genre):  #We don't pass the genre as a parameter because it's not recognized by the fixture.
        return api_client.post('/genres/', genre)
    return do_create_genre

    
@pytest.mark.django_db
class TestCreateGenre:
    # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self, create_genre):
        response = create_genre({'name': 'Tragedy++'})  # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 401 (Unauthorized) for unauthenticated users
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self, authenticate, create_genre):
        authenticate(is_staff=False)

        response = create_genre({'name': 'Tragedy++'}) # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 403 (forbiden) for none admin user
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_if_data_is_invalid_return_400(self, authenticate, create_genre):
        authenticate(is_staff=True)

        response = create_genre({'name': ''}) # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 403 (forbiden) for none admin user
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data['name'] is not None

    def test_if_data_is_valid_return_201(self, authenticate, create_genre):
        authenticate(is_staff=True)
        
        response = create_genre({'name': 'Tragedy++'}) # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 403 (forbiden) for none admin user
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['id'] > 0

# RUN TEST: pytest
# RUN TEST: ptw