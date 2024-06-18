# WEB Letter

This repository contains the source code for **WEB Letter**, a book website built with Django REST Framework (backend) and Vue.js (frontend).

## Features

- Search and browse through a collection of books.
- View detailed information about each book, including title, author, description, and cover image.
- User authentication and authorization.
- Ability to add new books (admin only).
- Responsive design for optimal viewing experience on various devices.

## Installation

To run the project locally, follow these steps:

1. Clone this repository: `git clone <repository_url>`
2. Navigate to the backend directory: `cd backend`
3. Install backend dependencies: `pip install -r requirements.txt`
4. Run Django migrations: `make migrate`
5. Start the Django development server: `make run`
6. In another terminal, navigate to the frontend directory: `cd frontend`
7. Install frontend dependencies: `npm install`
8. Start the Vue.js development server: `npm run serve`

Visit `http://localhost:8080` in your web browser to view the WEB Letter website.

## Configuration

### Backend

- **Database**: By default, the project uses Postgres. You can change the database settings in `backend/settings.py` if needed.
- **Authentication**: User authentication is handled using Django's built-in authentication system. You can customize authentication settings or integrate with third-party authentication providers as per your requirements.

### Frontend

- **API Base URL**: Ensure that the `baseURL` in `front/src/stores` points to the correct backend URL where the Django REST Framework is running.
- **Environment Variables**: You may need to set environment variables for configuration in a production environment.

## Contributing

Contributions are welcome! If you have suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
