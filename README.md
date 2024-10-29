# Django Bookstore Application

This project consists of a **Django backend** for managing the bookstore API and a **React frontend** for interacting with the API. Follow these steps to set up and run both parts of the application.

## Requirements

Before you begin, make sure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Node.js & npm](https://nodejs.org/) (Node.js version 12+ recommended)

## Getting Started

### 1. Clone the Repository

Clone this repository to your local machine:
```bash
git clone https://github.com/itsyt/django-bookstore.git
cd django-bookstore
```

## Backend Setup (Django)

### 2. Create a Virtual Environment

Inside the project directory, create and activate a virtual environment:
```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# For Windows
venv\Scripts\activate
# For macOS/Linux
source venv/bin/activate
```

### 3. Install Backend Dependencies

With the virtual environment activated, install the backend dependencies listed in `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

Navigate to the Django project directory and apply migrations:
```bash
python manage.py migrate
```

### 5. Start the Django Development Server

Run the following command to start the Django backend server on `http://127.0.0.1:8000/`:
```bash
python manage.py runserver
```

Your Django backend should now be running and ready to handle API requests.

## Frontend Setup (React)

### 6. Install Frontend Dependencies

Navigate to the `frontend` directory and install the React app dependencies using `npm`:
```bash
cd frontend
npm install
```

### 7. Start the React Development Server

After installing the dependencies, you can start the React development server:
```bash
npm start
```

This will run the frontend on `http://127.0.0.1:3000/`, and it should connect to the Django backend API running on `http://127.0.0.1:8000/`.

## Configuration

### API URL

If the API URL or port changes, update it in the `apiConfig.js` file in the `frontend/src` directory.

## Additional Notes

- **Django Admin Panel**: You can access the Django admin panel at `http://127.0.0.1:8000/admin`.
- **Frontend Development**: The React app has hot-reloading enabled, so any saved changes will automatically update in the browser.

## Troubleshooting

- If you encounter issues with package installations or missing dependencies, try deleting the `node_modules` folder in the `frontend` directory and running `npm install` again.
- Ensure your virtual environment is activated when running backend commands.

## License

This project is open-source and available under the [MIT License](LICENSE).
