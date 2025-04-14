# Django To-Do List App

A beginner-friendly web application built with Django that lets users add and view their to-do tasks. This project is ideal for anyone learning backend development and wanting a hands-on introduction to Django.

## Features

- Add new tasks through a simple form
- View a list of all to-do tasks
- Mark completed tasks visually
- Admin panel to manage tasks
- Powered by Django's ORM and template system

## Project Structure

```
my_django_project/
├── mysite/              # Project settings
├── hello/               # To-do list app
│   ├── models.py        # Task model
│   ├── views.py         # View logic
│   ├── urls.py          # App URLs
│   └── templates/
│       └── hello/
│           └── home.html  # Main template
├── db.sqlite3           # SQLite database
└── manage.py            # Django project CLI
```

## Getting Started

### Prerequisites

- Python 3.11+
- pip (comes with Python)

### Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app
```

2. Create and activate a virtual environment:

```bash
python -m venv env
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate
```

3. Install the dependencies:

```bash
pip install django
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create a superuser (for admin panel):

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Future Improvements

- Edit and delete tasks
- Mark tasks as completed with checkboxes
- Filter tasks by status
- Add user authentication
- Deploy the app online (Heroku, Railway, etc.)

## License

This project is licensed under the MIT License.

## Author

Ed Heravi wishes you a joyful coding journey!


