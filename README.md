YAY COFFEE! - Management and Operation System for Café
Project Purpose and Overview
This project aims to provide a digital, secure system for a café to manage orders, users, and information processes. The system includes management interfaces for ordering items, handling customer requests, menu item management, and customer reviews.

User Types
Admin: User with full access to the system, including adding menu items and managing users.
Customer: User with access to order items from the menu and submit reviews.
Operator: User responsible for viewing and closing open orders.
Processes
Login Process: Each user must log in with a username and password. According to their role, they are directed to the appropriate screen.
Order and New Order Creation: A customer can create a new order and select items from the menu.
Order Management and Closure: The operator can view open orders and close them upon completion.
Adding Items to the Menu: The admin can add new items to the menu with details such as price and description.
Submitting Reviews: A customer can submit a review and upload a photo to be stored in the system.
Managed Data
Users: Username, password, and role in the system.
Menu Items: Item name, description, and price.
Orders: Order ID, customer name, ordered items, and order status.
Reviews: Review content, rating, and review photo.
Overall Architecture
Server-Side: Built with Flask, it manages user requests, orders, and reviews, with data access handled via SQLAlchemy and SQLite.
Client-Side: User interface built with HTML, CSS, and JavaScript, with a customized design for each user type and interactive interface.
Database: Managed with SQLite, containing tables for users, items, orders, and reviews.
Screenshots
Login Screen: Allows login for all user types.
Customer Screen: Allows customers to order items and submit reviews.
Operator Screen: Displays open orders and allows order closure.
Admin Screen: Allows the addition of menu items and user management.
