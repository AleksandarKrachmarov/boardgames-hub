# BoardGameHub - Django Basics Project

BoardGameHub is a web application built with Django for managing and exploring a collection of board games, publishers, and categories.

## Project Features
- **Full CRUD Operations**: Complete create, read, update, and delete functionality for board games and related entities.
- **Category Filtering**: Dynamic filtering of board games by category directly from the catalog view.
- **Custom Template Filters**: Custom text-truncation filter for clean card descriptions.
- **Validations**: Custom form and model validations ensuring data integrity (e.g., player count checks).
- **Custom Error Pages**: Styled custom 404 error page.
- **Responsive UI**: Designed with Bootstrap for a clean and modern user experience.

## Prerequisites
- Python (latest stable version recommended)
- pip (Python package installer)

## Installation & Setup Instructions

1. Clone the repository:
    git clone https://github.com/AleksandarKrachmarov/boardgames-hub
    cd boardgames_hub

2. Create and activate a virtual environment:
    python -m venv .venv
    .venv\Scripts\activate  (on Windows)
    source .venv/bin/activate  (on macOS/Linux)

3. Install dependencies:
    pip install django

4. Apply database migrations:
    python manage.py makemigrations
    python manage.py migrate

5. Run the development server:
    python manage.py runserver

6. Access the application:
    Open your browser and navigate to http://127.0.0.1:8000/. You can manually create categories, publishers, and games directly through the user interface.