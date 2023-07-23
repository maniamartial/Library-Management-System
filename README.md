**Overview**<br>
Library Management System (LMS) is a web-based application for managing books, members, and transactions in a library. This project is built using Django, a powerful and flexible web framework for Python.

**Features**<br>
-Add, view, and edit books with details such as title, author, quantity in stock, publisher, and more.</br>
-Add, view, and edit members with details like name, member ID, books borrowed, and outstanding debts.</br>
-Record transactions, issue and return books, and keep track of rent fees.</br>
-Manage the library's book inventory and members' information efficiently.</br>

**Installation**<br>
To run the Library Management System on your local machine, follow these steps:<br>

Clone the repository:</br>
'''python
_git clone https://github.com/your-username/library-management-system.git_

Create a virtual environment (optional but recommended):
_python -m venv env
source env/bin/activate  # On Windows, use 'env\Scripts\activate'_


Install the required dependencies:
_pip install -r requirements.txt_

Apply database migrations:
_python manage.py migrate_

Create a superuser to access the Django admin panel:
_python manage.py createsuperuser_

Start the development server:
_python manage.py runserver_


**Homepage**<br>


![Home page books](https://github.com/maniamartial/Library-Management-System/assets/60258622/0799509a-2bb3-4b79-acfb-8ed481177895)


**Adding A Book**

![Add a book](https://github.com/maniamartial/Library-Management-System/assets/60258622/2b9889b8-fbd8-45ba-8df9-92355c7f26fd)

**Updating the book**
![Update the book](https://github.com/maniamartial/Library-Management-System/assets/60258622/2f3decb6-6891-4d22-a2a0-de1b9630d2cd)

**Delete the book**
![delete the book](https://github.com/maniamartial/Library-Management-System/assets/60258622/ee23116c-7878-4a7f-ae82-f7bfb31c459a)


**Lending a book to Clients/ Creating transaction**
![transactin where we are lending book](https://github.com/maniamartial/Library-Management-System/assets/60258622/76f46d9f-ae10-49b1-892f-47276b55e93a)

**Transaction List showing book leased, member etc**
![all books rented transaction](https://github.com/maniamartial/Library-Management-System/assets/60258622/0fb4f815-fb1f-4ec4-8312-df1613b843d7)

**Update transaction**
![update transaction](https://github.com/maniamartial/Library-Management-System/assets/60258622/2c133fc5-fdc2-4084-bb58-a7e07f9d1155)


**Members List**
![members list](https://github.com/maniamartial/Library-Management-System/assets/60258622/258ab0f6-45be-4461-a33c-bc2efcd230fb)

**Add a member**
![add a nuew member](https://github.com/maniamartial/Library-Management-System/assets/60258622/02b8f692-4471-41d6-a2db-21a6d7cfcff3)

**Update a member**
![update member](https://github.com/maniamartial/Library-Management-System/assets/60258622/0399395d-6024-4055-913f-284fd3e786f4)


**Returning the book**
![Returning teh book](https://github.com/maniamartial/Library-Management-System/assets/60258622/f911584d-b811-4b97-ac3c-bc17f3ae7a42)



