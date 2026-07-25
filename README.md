# Python-based Inventory Management System

## Overview
This project is an Inventory Management System developed using Python for Programming Principles subject. It is designed to efficiently handle various aspects of inventory management, including product management, stock tracking, order processing, and reporting. The system utilizes input and display functions, lists, conditional statements, loops, and user-defined functions to process and retrieve data from text files.

## Features
*   **Add a new product:** Allows the user to add a new product to the inventory. It includes validation to ensure the product ID is exactly 4 numbers, inputs are not empty, and prices and quantities are numeric. It also checks for ID duplication before saving.
*   **Update product details:** Enables the user to update the details of an existing product. Users can search by Product ID and selectively update the name, description, price, or quantity.
*   **Add a new supplier:** Allows the user to add a new supplier to the system. It verifies that the contact information is numeric and that the supplier ID is unique.
*   **Place an order:** Facilitates the process of placing an order for a specific product. It captures the timestamp, product ID, quantity, supplier ID, and the delivery status (Incomplete, Pending, or Done).
*   **View inventory:** Displays the current inventory levels for all products. It also lists all registered suppliers and their contact details.
*   **Generate reports:** Generates reports such as low stock items, product sales, and supplier orders. The console report calculates total products, total inventory value, average product price, the most expensive product, the cheapest product, and flags items with a quantity of 10 or less.

## Data Storage and Files
The system uses separate text files for data persistence and initial data preparation:
*   `Product.txt`: Contains product details such as product ID, name, description, price, and quantity.
*   `suppliers.txt`: Stores supplier information, including supplier ID, name, and contact details.
*   `orders.txt`: Maintains records of orders, including the timestamp, product ID, order quantity, supplier ID, and delivery status.
*   `Project_Sept24(1).pdf`: The project description and marking rubrics reference document.

## Group Members
This is a group project developed by the following members:
*   Kayxin Haydnsen Citro
*   Mabellyn Chan May Ji
*   Nicholas Andersen Salim
*   Reina Miyasako
*   Yohan Lim
