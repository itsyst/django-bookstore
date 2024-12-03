from locust import HttpUser, task, between
from random import randint

class WebsiteUser(HttpUser):
    wait_time = between(1,5)

    @task(2)
    def view_books(self):
        genre_id = randint(1,10)
        return self.client.get(f'/books/?genre_id={genre_id}', name='/books/')
    
    @task(4)
    def view_book(self):
        book_id = randint(1,1000)
        return self.client.get(f'/books/?book_id={book_id}', name='/books/:id')
    
    @task(1)
    def add_to_card(self):
        book_id = randint(1,10)
        return self.client.post(f'/carts/{self.cart_id}/items', name='/carts/items', json={'book_id': book_id, 'quantity': 1})

    def on_start(self):
        response = self.client.post('/carts/')
        result = response.json()
        self.cart_id = result['id']


# Run a test script
# locust -f locusts/browse_books.py