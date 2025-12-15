# Smart Appointment Manager

Smart Appointment Manager is a simple business and appointment management system built with Python.

This project was designed to demonstrate clean code, modular architecture, and real-world problem solving, focusing on junior-level backend opportunities.

---

## Features

- Client management (add and list clients)
- Service management (add and list services)
- Persistent data storage using JSON
- Command-line interface (CLI)
- Modular and organized project structure

---

## Project Structure

smart-appointment-manager/
- app/
  - main.py        # CLI entry point
  - clients.py     # Client business logic
  - services.py    # Service business logic
  - storage.py     # Data persistence layer
- data/
  - database.json  # Local data storage
- README.md
- .gitignore

---

## How to Run the Project

1. Make sure you have Python 3.10 or higher installed.

2. Clone the repository and navigate into it.

3. Run the application using the command below:

python app/main.py

---

## Example Usage

- Add new clients with name and phone number
- Register services with a name and price
- List all registered clients and services directly from the terminal

---

## Design Decisions

- Data is stored in a JSON file to keep the project simple and dependency-free
- Business logic is separated from the user interface
- Each module has a single responsibility
- The architecture allows easy migration to a web application in the future

---

## Future Improvements

- Appointment scheduling
- Time conflict validation
- User authentication
- Web interface using Flask
- Database migration to SQLite

---

## Author

Developed by Matheus Moraes  
GitHub: https://github.com/iMoraies
