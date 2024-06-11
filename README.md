# AstroEventsSystem

**Event ticketing application built with Python and Django framework.**

## Introduction

AstroEventsSystem is a web-based application for managing event ticketing. Users can view, book, and manage events. Organizers can create, edit, and delete events. This project demonstrates the use of the Django framework for building scalable web applications.

**Deployed Site:** [Your Deployed Site Link](https://bryansine.github.io/)

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Testing](#testing)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [Related Projects](#related-projects)
- [License](#license)
- [Contact](#contact)

## Features

- User authentication and authorization
- Event creation, editing, and deletion by organizers
- Event viewing and booking by attendees
- Email notifications for event updates
- Responsive design

## Installation

## Installation

To set up the project locally, follow these steps:

1. **Clone the project repository:**
 
   ```git clone https://github.com/bryansine/Astro_events.git```
2.  Navigate to the project directory:
  ``` cd AstroEventsSystem```
3. Create a Virtual Environment:
 ``` python3 -m venv myvenv```
4.  Activate the Virtual Environment (macOS/Linux):
  ```source myvenv/bin/activate```
5.  Install Required Packages:
 ``` pip install -r requirements.txt```
6.  Migrate the Database:
  ```python manage.py migrate```
7.  Create a Super User:
  ```python manage.py createsuperuser```
8.  Start the Development Server:
 ``` python3 manage.py runserver```


## Usage

1. **Access the application:** Open your web browser and go to `http://127.0.0.1:8000`.
2. **Admin Panel:** Access the admin panel at `http://127.0.0.1:8000/admin` to manage users and events.
3. **User Registration and Login:** Users can sign up and log in to view and book events.
4. **Creating Events:** Logged-in organizers can create, edit, and delete events.

## Technologies Used

1. Python: Programming language
2. Django: Web framework
3. HTML/CSS: Frontend design
4. JavaScript: Frontend interactivity and semantic ui
5. CSS framework for responsive design
6. SQLite: Database
7. SMTP: Email service for notifications

## Contributing

I welcome contributions from the community. If you encounter any bugs or have feature requests, please submit them through GitHub issues.

## Related Projects

- [Project A](https://mosaiceventsdecor.com/): A related project that complements AstroEventsSystem.
- [Project B](https://agency.tikomatata.com/): Another project similar to Astro.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

**Author:** Bryan Sine
**LinkedIn:** [Bryan Sine](https://www.linkedin.com/in/bryansine)


## screenshot
![A screenshot](images/attendee.png)


