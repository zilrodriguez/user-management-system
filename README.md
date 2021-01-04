# User Management System

A Simple User Management System powered by Flask

## Table of Contents

  - [Overview](#overview)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [License](#license)
  - [Contact](#contact)

## Overview
A simple user management system with user roles and permissions made with Flask and MySQL Database. This application can be easily integrated in your own python flask project. It has a separate administrator and user page, allowing your administrators to create an account and build restricted access to certain users.

## Getting Started

### Prerequisites

To run the application you will need:

- Python 3.9
- Flask
- Flask-SQLALCHEMY
- Flask-WTF
- Flask-Login
- Flask-Bcrypt
- pymysql

Assuming you have Python, proceed to install the rest using the command below:

```
pip install -r requirements.txt
```

### Installation

1. Clone the repo.
   ```sh
   git clone https://github.com/zilrodriguez/user-management-system.git
   ```
2. Install the dependencies using.
   ```sh
   pip install -r requirements.txt
   ```
3. Set configuration `SQLALCHEMY_DATABASE_URI` to your MySQL Database in the `__init__.py` file.
   ```python
   mysql+pymysql://user:password@localhost/database_name
   ```
4. Create the database models.
   ```python
   from user_management.models import db
   db.create_all()
   ```
5. In order to login to the application, you'll need to create an administrator account.
   ```python
   from user_management import db, bcrypt
   from user_management.models import User
   
   hashed_password = bcrypt.generate_password_hash('your_password').decode('utf-8')
   
   user = User(email='your_email@demo.com', password=hashed_password, user_role='Administrator')
   db.session.add(user)
   db.session.commit()
   ```
6. Start the app using `python run.py`.
7. Visit [http://localhost:5000/](http://localhost:5000/) from your browser to access the app.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Contact me - [@zilrodriguez](https://www.facebook.com/zilrodriguez1019) - zilrodriguez1019@gmail.com

Project Link: [https://github.com/zilrodriguez/user-management-system](https://github.com/zilrodriguez/user-management-system)