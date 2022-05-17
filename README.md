# Fall 2022 - Shopify Backend Developer Intern Challenge

## Overview

An inventory tracking web application for a logistics company. This web app includes basic CRUD functionality, in which users can create inventory items and warehouses, edit them, delete them, and view a list of them. In addition, users can assign inventory to specific warehouses.

This web app is built with Python Flask on the backend with a SQLite database, and HTML5 on the frontend using minimal CSS for styling.

## Link to Replit
My app is deployed on [Replit](https://replit.com/@MelanieTai/inventory-tracking-system-web-app)

## Database
This web app uses SQLite as database because Replit only supports SQLite. This web app was originally built using PostgreSQL as database but was changed to SQLite to simplify deployment to Replit. If this web app is deployed to Heroku or AWS, I will choose PostgreSQL as database.

## Features

### View All Inventory and Warehouses

<p>Users can view a list of all inventory items and warehouses.</p>
<img src="/myapp/static/images_readme/index.png" alt="index page" width="600px"/>

### Create Inventory and Warehouse

<p>Users can create a new inventory item or a new warehouse.</p>
<img src="/myapp/static/images_readme/new_inventory.png" alt="new inventory page" width="600px"/>
<img src="/myapp/static/images_readme/new_warehouse.png" alt="new warehouse page" width="600px"/>

### Edit Inventory and Warehouse

<p>Users can edit an inventory item or a warehouse.</p>
<img src="/myapp/static/images_readme/edit_inventory.png" alt="edit inventory page" width="600px"/>
<img src="/myapp/static/images_readme/edit_warehouse.png" alt="edit warehouse page" width="600px"/>

### Delete Inventory and Warehouse

<p>Users can delete an inventory item or a warehouse. A flash message will pop up after deletion</p>
<img src="/myapp/static/images_readme/delete_inventory.png" alt="delete inventory page" width="600px"/>
<img src="/myapp/static/images_readme/delete_warehouse.png" alt="delete warehouse page" width="600px"/>

### Assign Inventory to Warehouse

<p>Users can assign inventory to specific warehouses.</p>
<img src="/myapp/static/images_readme/assign_inventory_to_warehouse.png" alt="edit/assign inventory page" width="600px"/>

## Technologies

### Languages:
* Python
* HTML5
* CSS
* SQL

### Frameworks & Libraries:
* Flask
* SQLAlchemy
* Python Unittest

### Database:
* SQLite

## How To Get Started

To download and use this web app please follow these instructions:

  1. Install [Python3](https://www.python.org/downloads/) 
  1. In your terminal, `git clone` this repository
  2. `cd shopify`
  3. Create virtual environment with `virtualenv env`
  4. Activate the virtual environment with `source env/bin/activate`
  5. `pip3 install -r requirements.txt`
  6. Build your database tables with `python3 -m myapp.database`
  7. Launch the server with `python3 run.py`
  8. The web app will be launched on your broswer [localhost:5000/](http://localhost:5000/)

## Testing

This web app uses Python Unittest for testing. The tests are located in the tests directory. To run the tests, run `python3 -m unittest tests/test*`

## Coming soon...

A few ideas of features to add in the future:

* Change warehouse dropdown menu to a search bar to accomodate a large amount of warehouses
* Show all inventory items in each warehouse
* Assign SKU to each inventory item
* Group inventory items into categories
* Splitting an inventory and assign to multiple warehouses
* Add distribution log to keep track of movement of inventory
* Track stock levels
* Identify low-turn stock