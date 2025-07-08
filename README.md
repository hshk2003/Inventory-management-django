# Inventory Management System (Django)

A full-featured Inventory Management System built with Django, supporting CRUD operations, user authentication, search, pagination, and admin management.

## Features

- Item listing, details, create, update, delete
- Category & Supplier management
- User authentication (login/logout)
- Search and pagination support
- Responsive Bootstrap UI
- Django admin panel

## Tech Stack

- Python 3
- Django
- SQLite
- HTML/CSS/Bootstrap

## Getting Started

```bash
git clone https://github.com/your-username/inventory-management-django.git
cd inventory-management-django
python -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
