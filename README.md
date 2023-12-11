# Movie-Ticket-Booking

For developing our front end for the database we have used customer table, booking ticket table and a login table. The development of user interface is done using html. Creation of database and tables are performed in Postgre sql.
The back end and front end are connected using python language.
customer, movie, booking ticket, cashier and payment are the database entities

The connection of postgre sql to python is achieved by psycopg2 which is the most popular PostgreSQL database adapter for the Python programming language.

The linking of html files used for each of the webpage is done by using flask


First the login page will be displayed in the front end by the use of login.html file. 
If the user hasn’t already registered create and account option is placed at the bottom part of login page which will lead to registration page. 
It will ask user to input information such as username, password, mobile, email, address and area. When create button is clicked the details entered will be stored in the customer table. 
After creating the user account, it will directly go to home or index page which is displayed by the use of index.html file. A registered user can login using his registered username and password.
If either username of password entered is wrong it will display “invalid username or password”. The index page will contain a logout button, movie list with movie name, category, and book ticket button. 
When book ticket button is clicked, it will lead to checkout page. Checkout page is displayed by the use of checkout.html file. In the checkout page we inset the number of tickets, amount, booking date and time. 
When the checkout button is clicked after inserting the values it will lead to ticket booked page displayed by the use of orderplaced.html file. 
At the same time the values given in checkout page will be inserted into the table ticket booking. Finally the order placed page will give a message such as ‘congratulation ticket booked’
