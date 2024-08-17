

# BookWeb App

A web-based platform for readers and publishers to explore, manage, and interact with books. The application allows users to search for books, rate them, and view summaries powered by the Ollama Qwen 2 0.5b model. This project is built using Django & Django REST Framework, PostgreSQL, and Docker, with Swagger for API documentation and token authentication via Django REST Framework.

## Features

- **User Authentication**: Secure registration and login for users with token-based authentication.
- **Book Management**: Publishers can add, update, and delete books.
- **Search and Filter**: Search for books by title, author.
- **Ratings and Reviews**: Users can rate and review books.
- **Favorites**: Users can favorite books and manage their list.
- **Book Summaries**: Get concise summaries of books using the Ollama Qwen 2 0.5b model.
- **API Documentation**: Explore the available endpoints with Swagger.
- **Token Authentication**: APIs secured using token-based authentication powered by Django REST Framework.

## Tech Stack

- **Backend**: Django & Django REST Framework
- **Database**: PostgreSQL
- **Containerization**: Docker 
- **Testing**: Pytest
- **AI Integration**: Ollama Qwen 2 0.5b model for generating book summaries
- **API Documentation**: Swagger
- **Authentication**: Token-based authentication with Django REST Framework

## Getting Started

### Prerequisites

- Docker

### Setup and Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/sudip-khanal/bookweb-app.git
    cd bookweb-app
    ```

2. Create a `.env` file in the root directory with the necessary environment variables:

    ```bash
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=postgres://username:password@db:5432/bookweb_db
    ```

3. Build and run the containers:

    ```bash
    docker-compose up --build
    ```

4. Apply migrations and create a superuser:

    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

5. Access the application:

    - Web app: [http://localhost:8000](http://localhost:8000)
    - Admin Panel: [http://localhost:8000/admin](http://localhost:8000/admin)
    - API Documentation (Swagger): [http://localhost:8000/swagger](http://localhost:8000/swagger)

## Running Tests

To run the tests using `pytest`:

```bash
docker-compose exec web pytest
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a pull request.
