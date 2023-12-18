# CMS Desktop App

## Overview

Welcome to CMS, a desktop application designed to streamline cars management system.

## Technologies Used

```r
├── README.md
├── app
│   ├── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── authentication.py
│   │   ├── business_logic.py
│   │   └── data_handler.py
│   └── view
│       ├── __init__.py
│       ├── app.py
│       ├── dashboard_frame.py
│       └── login_frame.py
├── dbenv.sql
├── env
│   ├── omarenv.txt
│   └── psql_python.sh
├── main.py
├── models
│   ├── __init__.py
│   ├── base_model.py
│   ├── car.py
│   ├── customer.py
│   ├── engine
│   │   ├── __init__.py
│   │   └── db_storage.py
│   ├── reservation.py
│   ├── revenue.py
│   └── user.py
├── requirements.txt
├── resources
│   ├── images
│   │   ├── Graph_ORM.png
│   │   └── dashboard_frame.png
│   └── styles
│       └── styles.css
└── testbaseModel.py
```
### Database: PostgreSQL

Our app relies on PostgreSQL as the primary database. PostgreSQL is a powerful, open-source relational database management system known for its reliability and extensibility. It provides robust support for complex queries, transactions, and data integrity.

### Backend: SQLAlchemy and Python OOP

#### SQLAlchemy

We leverage SQLAlchemy as the Object-Relational Mapping (ORM) tool for interacting with the PostgreSQL database. SQLAlchemy simplifies database operations by allowing developers to interact with the database using Python classes and objects.

##### Tables
![](./resources/images/Graph_ORM.png)

#### Python OOP

The backend of CMS is built using Python, utilizing Object-Oriented Programming (OOP) principles. This design approach enhances code organization, modularity, and maintainability. Python's versatility and readability contribute to an efficient and scalable backend.

### GUI: CustomTkinter

Our Graphical User Interface (GUI) is crafted using CustomTkinter, a customized version of the Tkinter library in Python. CustomTkinter enhances the user experience by providing a tailored interface with intuitive navigation and a visually appealing design. It streamlines user interactions and ensures a seamless experience while interacting with the CMS desktop app.

### UI:

#### Dashboar:
![](./resources/images/dashboard_frame.png)

## Features

### PostgreSQL Database Features

- **Reliability:** PostgreSQL ensures data integrity and reliability, making it a suitable choice for managing critical information.
- **Scalability:** The database scales effortlessly to accommodate growing data volumes and complex queries.
- **Flexibility:** PostgreSQL supports a wide range of data types and allows for the implementation of custom functions, providing flexibility in data modeling.

### SQLAlchemy and Python OOP Backend Features

- **Modularity:** The use of SQLAlchemy and Python OOP promotes code modularity, making it easy to maintain and extend the backend functionality.
- **Security:** Our backend implementation follows best practices to ensure data security and prevent unauthorized access.
- **Transaction Support:** SQLAlchemy facilitates robust transaction management, ensuring data consistency and reliability.

### CustomTkinter GUI Features

- **Intuitive Design:** CustomTkinter provides a user-friendly interface with a focus on intuitive design, enhancing user experience and navigation.
- **Customization:** The GUI is highly customizable, allowing for branding and tailoring the interface to meet specific user preferences.
- **Responsive Layouts:** CustomTkinter ensures responsive layouts that adapt to different screen sizes, providing a consistent experience across devices.

## Getting Started

[Provide instructions on how to install and run the CMS desktop app. Include any dependencies or prerequisites.]

## License

This project is licensed under the [MIT License](LICENSE.md) - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- [List any contributors or external libraries/tools used in the project.]
