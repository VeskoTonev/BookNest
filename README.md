# ReadTrack — Book and Reading Tracker

A Django web application for organizing books, tracking reading progress, managing personal reading lists, and setting reading goals.

## Table of Contents

- [Project Overview](#project-overview)
- [Motivation](#motivation)
- [Features](#features)
- [Technologies](#technologies)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Configuration](#configuration)
- [Database Setup](#database-setup)
- [Running the Application](#running-the-application)
- [How to Use](#how-to-use)
- [Testing](#testing)
- [Screenshots and Demo](#screenshots-and-demo)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

BookNest is a web application built with Django that helps readers organize their books and monitor their reading activity in one place.

The application allows users to explore a collection of books, organize books by author and genre, create reading lists, record reading progress, and work toward reading goals.

The project demonstrates the use of Django models, model relationships, forms, views, templates, URL routing, database operations, and reusable HTML layouts.

## Features

- **Book Collection Management**: Add, update, view, and delete books along with custom cover images, publication details, reading status (e.g., Reading, Completed, Want to Read), and ratings.
- **Authors & Genres Management**: Manage author profiles (biographies, birth years) and assign multiple genres to organize your library.
- **Custom Reading Lists**: Create curated collections and add books to specific lists with personalized reading notes.
- **Reading Challenges & Goals**: Set yearly reading targets and track your progress over time.
- **Responsive UI & Flash Messages**: Modern dashboard integrated with Bootstrap 5 and customized feedback messages for smooth user navigation.

---

## Motivation

Keeping track of books, reading progress, and personal reading goals can become difficult when information is spread across different places.

BookNest aims to make this process easier by providing a centralized application for organizing books and maintaining a structured reading routine.

The project was also developed to demonstrate fundamental Django web-development concepts, including database modeling, form handling, CRUD operations, validation, and dynamic template rendering.

## Features

### Book Catalog
- Browse the available books.
- View individual book details.
- Search for books by title.
- Filter books by genre.
- Sort books using available sorting options.
- View book information, including publication year, author, rating, and description where available.

### Authors and Genres
- Organize books by author.
- Associate books with one or more genres.
- Browse author information and related books.
- Maintain relationships between books, authors, and genres.

### Reading Lists
- Create and organize personal reading lists.
- Add books to reading lists.
- View the books associated with a list.
- Update and delete reading lists and their items.

### Reading Progress
- Track reading status using the available status options.
- Record completion information where supported.
- View book details and reading information.

### Reading Goals and Challenges
- Create and manage reading goals.
- Track progress toward reading targets.
- Use reading challenges to support consistent reading habits.

### Forms and Validation
- Use Django forms to create and update application data.
- Validate submitted information.
- Apply validation rules such as valid ratings, appropriate publication years, and duplicate-prevention checks where implemented.

### User Interface
- Navigate through a shared site layout.
- Use reusable templates and template inheritance.
- Access application pages through navigation links.
- View styled pages using HTML and CSS.


## Technologies

The project uses the following technologies:

- **Python** — application programming language.
- **Django** — web framework.
- **SQLite** —  default development database, 
- **HTML5** — page structure.
- **CSS3** — styling and layout.
- **Git and GitHub** — source control and repository hosting.
- **Image/Media Handling**: Pillow library for Django media uploads

## Project Structure

The project is organized into Django applications that separate related functionality.

```text
DjangoProject/
├── manage.py
├── requirements.txt
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── books/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── reading_list/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── challenges/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── ...
├── templates/
├── static/
└── db.sqlite3
```

The structure above illustrates the main components. Some folders and files may differ in the actual repository. The database file is generated or populated during development and should not necessarily be committed to Git.

### Main Django Applications

| Application | Responsibility |
|---|---|
| `books` | Book catalog, authors, genres, and related operations |
| `reading_list` | Reading lists and their associated book items |
| `challenges` | Reading goals and challenges |

## Installation

Follow these instructions to download and run the project locally.

### Prerequisites

Install the following software before starting:

- Python version compatible with the project's dependencies.
- Git, if cloning the repository.
- A terminal or command prompt.

### 1. Clone the Repository

Replace the example URL with the actual GitHub repository URL.

```bash
git clone https://github.com/VeskoTonev/BookNest.git
cd DjangoProject
```

Alternatively, download the repository as a ZIP archive and extract it.

### 2. Create a Virtual Environment

A virtual environment keeps the project's Python dependencies separate from other Python projects.

**Windows — Command Prompt or PowerShell:**

```bash
python -m venv .venv
```

Activate the environment in Command Prompt:

```bat
.venv\Scripts\activate
```

Or in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

**macOS or Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

Install the dependencies listed in `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Check the project's `settings.py` to determine whether environment variables are required.

If the project uses a `.env` file, document the variables that the application actually reads and provide a `.env.example` file containing placeholder values.

For example, a configuration may include:


## Database Setup

Django uses migrations to create and update database tables based on the project's models.

Run the following commands from the directory containing `manage.py`:

```bash
python manage.py makemigrations
python manage.py migrate
```

The first command creates migration files for model changes that have not yet been recorded. The second applies the migrations to the configured database.

If all migration files are already included in the repository and up to date, applying migrations is normally sufficient:

```bash
python manage.py migrate
```

To create an administrator account for Django's admin interface, if needed:

```bash
python manage.py createsuperuser
```

The administrator account is optional for normal use of the application and does not replace the application's own pages or forms.

## Running the Application

Start Django's development server:

```bash
python manage.py runserver
```

Open the following address in your browser:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

The development server runs locally and is intended for development and testing rather than production deployment.

To stop the server, press `Ctrl+C` in the terminal.

## How to Use

### Browse Books
Open the book catalog to explore the available books. Use the search field to find books by title and the genre and sorting controls to narrow or organize the results.

### View Book Details
Select a book to open its detail page and inspect the information available for that book.

### Manage Authors and Genres
Use the relevant application pages to browse or manage author and genre records, according to the actions provided by the interface.

### Create Reading Lists
Open the reading-list section, create a list, and add books to it. You can then view and manage the list and its associated items.

### Track Reading Progress
Use the available reading-status and completion fields to record your progress through books.

### Set Reading Goals
Open the goals or challenges section to create and manage reading targets and monitor your progress.

The exact navigation labels and available actions may vary depending on the current implementation.





## License

This project has been created for educational purposes.


---

## Additional Documentation

For further information about the technologies used in this project, consult:

- [Django Documentation](https://docs.djangoproject.com/)
- [Python Documentation](https://docs.python.org/3/)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)


## Project Status

ReadTrack is a coursework project under development. Features, documentation, and setup instructions should be updated as the implementation evolves.
