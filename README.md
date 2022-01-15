# Challenge Front-end Refera

- lista
## Acceptance criteria

- Criteria

-Customer base
    -Table with "registered" customer data
    -Button to open the customer registration form, "New Customer"
    -Registration form with the consistencies 
    -Mask in the form fields 
    -Dialog message when clicking the "Save" button
    -"Cancel" button, must return to a list of customers

-Order Registration
    -Table with list of customers and orders
    -Button to open the order registration form, "New Order"
    -Registration form with consistencies
    -Mask in the form fields
    -Dialog message when clicking the "Save" button
    -"Cancel" button, must return to a list of orders
    -Button that edit order list
    -By clicking on the "Save" button, the order data must go to order list.

## Instalation

- First clone this repository and Install Packages
```terminal
https://github.com/Lnhacanhaca/Refera---FrontEnd-Challenge.git
cd project
pip install -r requirements.txt
```
- Setup Virtualenv Ubuntu  or Linux distro

```terminal
python3 -m venv venv
source venv/bin/activate
```
- How To Setup on Windows

```terminal
python -m venv venv
venv/Scripts/activate
```

- Migrate and start Server

```terminal
python manage.py makemigrations
python manage.py migrate
python manage.py runserver