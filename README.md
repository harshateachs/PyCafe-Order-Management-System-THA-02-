# PyCafé Order Management System

## Overview
PyCafé Order Management System is a simple Python script designed to assist the staff of a trendy café, PyCafé, in efficiently managing customer orders. The café offers a variety of delicious coffee, pastries, and sandwiches, and this system allows the staff to add and view customer orders effortlessly.

## Features
- **Add Order:** Staff can add new orders specifying the order ID, item name, and quantity. The system checks for duplicate order IDs to prevent errors.
- **View Orders:** Staff can view all existing orders with their respective details, including order ID, item name, and quantity.

## How to Use
1. Clone or download the repository to your local machine.
2. Ensure you have Python installed on your system.
3. Open the terminal or command prompt and navigate to the directory containing the script (`order_management.py`).
4. Run the script using the command `python order_management.py`.
5. Follow the on-screen prompts to add orders or view existing orders.
6. Enjoy efficient order management for PyCafé!

## Script Details
The script (`order_management.py`) contains the following functions:

### `add_order(order_id, item_name, quantity=1)`
Adds a new order to the system with the provided details. Checks for duplicate order IDs to avoid errors.

### `print_orders()`
Displays all existing orders along with their details.

## Example
```python
# Sample Usage
from order_management import add_order, print_orders

# Adding orders
add_order(1, "Latte", 2)
add_order(2, "Croissant")
add_order(3, "Veggie Sandwich", 3)

# Viewing orders
print_orders()
```
## Note
- Ensure unique order IDs are used to prevent conflicts.
- Modify the script as needed to incorporate additional features or customization.
