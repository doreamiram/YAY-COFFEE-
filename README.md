# YAY COFFEE! Project

## Project Overview
The **YAY COFFEE!** project is a web-based application designed to manage a coffee shop's online operations. This platform enables administrators to manage menu items, customers to place orders and submit reviews, and operators to handle orders efficiently.

## Users
The system includes three types of users, each with distinct roles and functionalities:
- **Admin:** Manages menu items and other administrative features.
- **Customer:** Places orders, submits reviews, and uploads photos.
- **Operator:** Views and closes open orders from customers.

## Processes
1. **Login:** All users must log in to access their designated features.
2. **Menu Management (Admin):** Admin users can add new items to the menu, each with a name, description, and price.
3. **Order Placement (Customer):** Customers can place an order by selecting items from the menu and entering their information.
4. **Order Handling (Operator):** Operators can view open orders and mark them as closed once fulfilled.
5. **Review Submission (Customer):** Customers can submit a review, rate their experience, and optionally upload a photo.

## Data Management
The application uses an SQLite database with the following tables:
- **Users**: Stores information on all users, including their username, password, and role.
- **Orders**: Tracks customer orders with details such as customer name, items ordered, and order status.
- **Items**: Manages menu items, including name, description, and price.
- **Reviews**: Stores customer reviews, ratings, and photo paths.

## Architecture
The **YAY COFFEE!** system follows the MVC (Model-View-Controller) architecture:
- **Model**: Handles data management and database interactions using SQLAlchemy.
- **View**: Defines HTML templates that display data and interact with users.
- **Controller**: The Flask app (`app.py`) routes user requests to the correct functionality and templates.


## Screenshots
Login screen where users enter credentials to access the system.
![תמונה של WhatsApp‏ 2024-10-29 בשעה 14 15 07_0a114cfb](https://github.com/user-attachments/assets/05a0d792-acba-47e9-bc7b-e102aed8c099)

Admin screen to add new menu items.
![תמונה של WhatsApp‏ 2024-10-29 בשעה 14 16 48_c27dbf47](https://github.com/user-attachments/assets/75282c0a-5595-4a06-87b2-9ed0519ec44b)

Customer screen to place a new order.
![תמונה של WhatsApp‏ 2024-10-29 בשעה 14 15 43_0a293183](https://github.com/user-attachments/assets/253f1b7a-a3d2-4e50-a8b2-95e2ad8506b4)

Operator screen to view and close open orders.
![תמונה של WhatsApp‏ 2024-10-29 בשעה 14 17 24_d0d4e659](https://github.com/user-attachments/assets/e8ead756-c51b-48ae-a280-7a4ddb5a1045)
