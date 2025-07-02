#  Pizza Restaurants API

A Flask-based API for managing pizza restaurants and their available pizzas.

This project was built as part of the **Phase 4 Code Challenge** at Moringa School.

---

##  User Stories

**As a visitor**, I can:
- View a list of all restaurants.
- View detailed info about a single restaurant and its available pizzas.

**As a developer**, I can:
- Add a pizza to a restaurant with a price.
- Remove a restaurant (with cascading deletes).
- Fetch all pizzas and restaurant-pizza relationships.

---

##  Tech Stack

| Layer      | Technology                |
|------------|----------------------------|
| Backend    | Flask, Flask-SQLAlchemy    |
| API Design | Flask-RESTful              |
| Database   | SQLite with Alembic Migrations |
| Frontend   | React (provided)           |
| Testing    | Postman / `curl` / pytest  |

---

##  How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/karongoi/python-phase-4-code-challenge-pizza.git
cd python-phase-4-code-challenge-pizza

Set Up Backend
cd server
pipenv install
pipenv shell
flask db init
flask db migrate -m "Initial setup"
flask db upgrade
python seed.py
python app.py

