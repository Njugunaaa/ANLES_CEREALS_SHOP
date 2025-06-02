#  ANLES Cereal Shop
Author
Gichuhi Joshua Njuguna
Phase 3 - Moringa School SQLAlchemy CLI Project
##  Description

ANLES Cereal Shop is a command-line application built with Python and SQLAlchemy.  
It allows users to:

- View and manage customers
- View and manage cereals and prices
- Place and manage orders
- Track total cost per order
- Mark orders as successful

This project uses Object Relational Mapping (ORM) to interact with a SQLite database.

---

##  Folder Structure

ANLES_CEREALS_SHOP/
├── lib/
│ ├── init.py
│ ├── models.py
│ └── cli.py
├── migrations/
│ └── versions/
│ └── env.py
├── seed.py
├── README.md
├── .env
├── Pipfile
├── Pipfile.lock

yaml
Copy
Edit

---

##  Technologies Used

- Python 3.8+
- SQLAlchemy
- Alembic (for database migrations)
- SQLite
- Pipenv (virtual environment and dependency manager)

---

##  How to Run

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/ANLES_CEREALS_SHOP.git
cd ANLES_CEREALS_SHOP
Set up the virtual environment:

bash
Copy
Edit
pipenv install
pipenv shell
Run migrations:

bash
Copy
Edit
alembic upgrade head
Seed the database (optional):

bash
Copy
Edit
python seed.py
Run the app:

bash
Copy
Edit
python lib/cli.py
## Features
Add and view customers and cereals

Place new orders with price and quantity

Automatically calculates total price

View joined data (customer + cereal)

Mark orders as successful

Prevents double-marking of orders

Clear, user-friendly CLI prompts

=> Project Requirements Met
=> 3+ related tables with correct relationships

=> Alembic used for migration

=> SQLAlchemy ORM and CRUD operations

=> CLI with error handling and clean prompts

=> Data structures (lists/dictionaries) used appropriately

=> Virtual environment with Pipenv

=> README with all required sections



## License
This application is released under the MIT License.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.