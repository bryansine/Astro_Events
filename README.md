# AstroEventsSystem

**Event ticketing application built with Python and Django framework.**

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

AstroEventsSystem is a web-based application for managing event ticketing. Users can view, book, and manage events. Organizers can create, edit, and delete events. This project demonstrates the use of the Django framework for building scalable web applications.

## Features

- User authentication and authorization
- Event creation, editing, and deletion by organizers
- Event viewing and booking by attendees
- Email notifications for event updates
- Responsive design

## Installation

To set up the project locally, follow these steps:

1. **Clone the project repository:**
    ```sh
    git clone https://github.com/bryansine/AstroEventsSystem.git
    ```

2. **Navigate to the project directory:**
    ```sh
    cd AstroEventsSystem
    ```

3. **Create a Virtual Environment:**
    ```sh
    python3 -m venv myvenv
    ```

4. **Activate the Virtual Environment:**
    ```sh
    source myvenv/bin/activate
    ```

5. **Install Django:**
    ```sh
    pip install django
    ```

6. **Install Required Packages:**
    ```sh
    pip install -r requirements.txt
    ```

7. **Migrate the Database:**
    ```sh
    python manage.py migrate
    ```

8. **Create a Super User:**
    ```sh
    python manage.py createsuperuser
    ```

9. **Start the Development Server:**
    ```sh
    python manage.py runserver
    ```

## Usage

1. **Access the application:**
   Open your web browser and go to `http://127.0.0.1:8000`.

2. **Admin Panel:**
   Access the admin panel at `http://127.0.0.1:8000/admin` to manage users and events.

3. **User Registration and Login:**
   Users can sign up and log in to view and book events.

4. **Creating Events:**
   Logged-in organizers can create, edit, and delete events.


## Technologies Used

1. Python: Programming language
2. Django: Web framework
3. HTML/CSS: Frontend design
4. JavaScript: Frontend interactivity
5. CSS framework for responsive design
6. sqllite: Database
7. smtp: Email service for notifications


## contributers
1. Bryan sine

## License
This project is licensed under the MIT License. See the LICENSE file for details.
