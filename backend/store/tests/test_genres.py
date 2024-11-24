from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateGenre:
    # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        client = APIClient()
        response = client.post('/genres/', {'name': 'Tragedy++'}) # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 401 (Unauthorized) for unauthenticated users
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_if_user_is_not_admin_returns_403(self):
        client = APIClient()
        client.force_authenticate(user= {})
        response = client.post('/genres/', {'name': 'Tragedy++'}) # Simulate POST request
        print(response.json())  # This will show the error message if the request is invalid
        
        # Ensure the response status code is 403 (forbiden) for none admin user
        assert response.status_code == status.HTTP_403_FORBIDDEN

# RUN TEST: pytest
# RUN TEST: ptw