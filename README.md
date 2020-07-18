# to start work on project being in practice folder

    $ pip install -r grocery_store/requirements.txt
    $ pip install -e .
    $ python grocery_store/manage.py db upgrade
    $ python grocery_store/manage.py populate
    $ python grocery_store/manage.py populate_orders

To run server:

    $ python grocery_store/manage.py runserver
    
### The project is a grocery store of foods(goods).

### Main Role:
* User

### Scripts:
* Simple login / logout.
* The user can view a list of all products.
* The user can view a list of all their purchases, with date, place and price.
* If the user is a manager, he / she can view their stores.

### For login:
Take any user from grocery_store/fixture/users.csv or from db :)
For testing, all password for users in users.csv 'hello'.
Also you can create new user.