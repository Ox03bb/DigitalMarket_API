<p align="center">
[![Python Version](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)  [![Django Version](https://img.shields.io/badge/Django-5.0.1-Green.svg)](https://www.djangoproject.com/) [![DRF Version](https://img.shields.io/badge/DjangoRestFramework-3.9.3-red)](https://www.django-rest-framework.org/)  [![SQLite3 Version](https://img.shields.io/badge/SQLite-3-silver.svg)](https://www.sqlite.org/index.html)
</p>

# API Endpointes
<br>
<table>
<thead>
<tr>
<th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Role</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Method</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span><var><span>/api/users</span></var></span></p></td>
<td><p><span><span>No role required</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Creates a new user with name, email , password,...etc</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/users</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>manager</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>List all users with ther info</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/users/{id}</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>manager</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Show the users number {id} info</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/users/me/</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Anyone with a valid user token</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Displays only the current user</span></span></p></td>
</tr>

 <tr>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
 </tr>

<tr>
<td><p><span><var><span>/api/login</span></var></span></p></td>
<td><p><span><span>Anyone with a valid username and password</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Generates access tokens that can be used in other API calls in this project</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/logout</span></var></span></p></td>
<td><p><span><span>Anyone has already logged in</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Deleting the token from the database for security reasons</span></span></p></td>
</tr>
</tbody>
</table>
</body>
</html>
 
 ## Menu-items endpoints
 
<table>
  <thead>
    <tr>
      <th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th>
      <th scope="col"><p><span><strong><span>Role</span></strong></span></p></th>
      <th scope="col"><p><span><strong><span>Method</span></strong></span></p></th>
      <th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><p><span><var><span>/api/menu-items</span></var></span></p></td>
      <td><p><span><span>Customer, delivery crew</span></span></p></td>
      <td><p><span><var><span>GET</span></var></span></p></td>
      <td><p><span><span>Lists all menu items. Return a </span></span><span><var><span>200 – Ok</span></var></span><span><span> HTTP status code</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items</span></var></span></p></td>
      <td><p><span><span>Customer, delivery crew</span></span></p><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><var><span>POST</span></var></span><span><span>, </span></span><span><var><span>PUT</span></var></span><span><span>, </span></span><span><var><span>PATCH</span></var></span><span><span>, </span></span><span><var><span>DELETE</span></var></span></p></td>
      <td><p><span><span>Denies access and returns </span></span><span><var><span>403&nbsp;– Unauthorized</span></var></span><span><span> HTTP status code</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items/{menuItem}</span></var></span></p></td>
      <td><p><span><span>Customer, delivery crew</span></span></p><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><var><span>GET</span></var></span></p></td>
      <td><p><span><span>Lists single menu item</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items/{menuItem}</span></var></span></p></td>
      <td><p><span><span>Customer, delivery crew</span></span></p></td>
      <td><p><span><var><span>POST</span></var></span><span><span>, </span></span><span><var><span>PUT</span></var></span><span><span>, </span></span><span><var><span>PATCH</span></var></span><span><span>, </span></span><span><var><span>DELETE</span></var></span></p></td>
      <td><p><span><span>Returns </span></span><span><var><span>403 - Unauthorized</span></var></span></p></td>
    </tr>
    <tr>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
      <td><p><span><span>&nbsp;</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items</span></var></span></p></td>
      <td><p><span><span>Manager</span></span></p></td>
      <td><p><span><var><span>GET</span></var></span></p></td>
      <td><p><span><span>Lists all menu items</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items</span></var></span></p></td>
      <td><p><span><span>Manager</span></span></p></td>
      <td><p><span><var><span>POST</span></var></span></p></td>
      <td><p><span><span>Creates a new menu item and returns </span></span><span><var><span>201 - Created</span></var></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items/{menuItem}</span></var></span></p></td>
      <td><p><span><span>Manager</span></span></p></td>
      <td><p><span><var><span>GET</span></var></span></p></td>
      <td><p><span><span>Lists single menu item</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items/{menuItem}</span></var></span></p></td>
      <td><p><span><span>Manager</span></span></p></td>
      <td><p><span><var><span>PUT</span></var></span></p></td>
      <td><p><span><span>Updates single menu item</span></span></p></td>
    </tr>
    <tr>
      <td><p><span><var><span>/api/menu-items/{menuItem}</span></var></span></p></td>
      <td><p><span><span>Manager</span></span></p></td>
      <td><p><span><var><span>DELETE</span></var></span></p></td>
      <td><p><span><span>Deletes menu item</span></span></p></td>
    </tr>
  </tbody>
</table>

## User group management endpoints

<table>
<thead>
<tr>
<th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Role</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Method</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span><var><span>/api/groups/manager/users</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all managers</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/groups/manager/users/{userId}</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Assigns the user in the payload to the manager group and returns </span></span><span><var><span>201-Created</span></var></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/groups/manager/users/{userId}</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>DELETE</span></var></span></p></td>
<td><p><span><span>Removes this particular user from the manager group and returns </span></span><span><var><span>200 – Success</span></var></span><span><span> if everything is okay.</span></span></p><p><span><span>If the user is not found, returns </span></span><span><var><span>404 – Not found</span></var></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/groups/delivery-crew/users</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all delivery crew</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/groups/delivery-crew/users/{userId}</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Assigns the user in the payload to delivery crew group and returns </span></span><span><var><span>201-Created</span></var></span><span><span> HTTP</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/groups/delivery-crew/users/{userId}</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>DELETE</span></var></span></p></td>
<td><p><span><span>Removes this user from the manager group and returns </span></span><span><var><span>200 – Success</span></var></span><span><span> if everything is okay.</span></span></p><p><span><span>If the user is not found, returns&nbsp; </span></span><span><var><span>404 – Not found</span></var></span></p></td>
</tr>
</tbody>
</table>

## Cart management endpoints 

<table>
<thead>
<tr>
<th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Role</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Method</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span><var><span>/api/cart</span></var></span></p></td>
<td><p><span><span>Customer</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns current items in the cart for the current user token</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/cart</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Adds the menu item to the cart. Sets the authenticated user as the user id for these cart items</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/cart</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>PUT</span></var></span></p></td>
<td><p><span><span>Update the quantity of product {id,cnt} OR delete one item from the cart {id} only</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/cart</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>DELETE</span></var></span></p></td>
<td><p><span><span>Deletes all menu items created by the current user token</span></span></p></td>
</tr>
</tbody>
</table>

## Order management endpoints

<table>
<thead>
<tr>
<th scope="col"><p><span><strong><span>Endpoint</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Role</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Method</span></strong></span></p></th>
<th scope="col"><p><span><strong><span>Purpose</span></strong></span></p></th>
</tr>
</thead>
<tbody>
<tr>
<td><p><span><var><span>/api/orders</span></var></span></p></td>
<td><p><span><span>Customer</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all orders with order items created by this user</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>POST</span></var></span></p></td>
<td><p><span><span>Creates a new order item for the current user. Gets current cart items from the cart endpoints and adds those items to the order items table. Then deletes all items from the cart for this user.</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders/{orderId}</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all items for this order id. If the order ID doesn’t belong to the current user, it displays an appropriate HTTP error status code.</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all orders with order items by all users</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders/{orderId}</span></var></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><span>Customer</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>PUT</span></var></span><span><span>, </span></span><span><var><span>PATCH</span></var></span></p></td>
<td><p><span><span>Updates the order. A manager can use this endpoint to set a delivery crew to this order, and also update the order status to 0 or 1.</span></span></p><p><span><span>If a delivery crew is assigned to this order and the </span></span><span><var><span>status = 0</span></var></span><span><span>, it means the order is out for delivery.</span></span></p><p><span><span>If a delivery crew is assigned to this order and the </span></span><span><var><span>status = 1</span></var></span><span><span>, it means the order has been delivered.</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders/{orderId}</span></var></span></p></td>
<td><p><span><span>Manager</span></span></p></td>
<td><p><span><var><span>DELETE</span></var></span></p></td>
<td><p><span><span>Deletes this order</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders</span></var></span></p></td>
<td><p><span><span>Delivery crew</span></span></p></td>
<td><p><span><var><span>GET</span></var></span></p></td>
<td><p><span><span>Returns all orders with order items assigned to the delivery crew</span></span></p></td>
</tr>
<tr>
<td><p><span><var><span>/api/orders/{orderId}</span></var></span></p></td>
<td><p><span><span>Delivery crew</span></span></p><p><span><span>&nbsp;</span></span></p></td>
<td><p><span><var><span>PATCH</span></var></span></p></td>
<td><p><span><span>A delivery crew can use this endpoint to update the order status to 0 or 1. The delivery crew will not be able to update anything else in this order.</span></span></p></td>
</tr>
</tbody>
</table>

## DataBase Diagrame : 
[![DB-Diagrame](https://img.shields.io/badge/DB_Diagrame-Silver)](https://drawsql.app/teams/django-34/diagrams/project)

#### This project is under Devlopment

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/DigitalMarket_API.git
    ```

2. Navigate to the project directory:

    ```bash
    cd DigitalMarket_API
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```
    
5. Run the development server:

    ```bash
    python manage.py runserver
    ```
    
6. Access the API at `http://localhost:8000/`.

# Using Docker 

1. Ensure you have Docker Engine  installed on your system.
  
2. open terminal/cmd .
   
3. Run the following command to build and start the Docker services:

```bash
docker-compose up -d
 ```
6. Access the API at `http://localhost:8000/`.
  
7. Access the phpMyAdmin at `http://localhost:80/`.
   
##### NOTE : if you faced any problem with django server, just Restart it.



<hr>

Feel free to reach out with any questions, feedback, or suggestions!
