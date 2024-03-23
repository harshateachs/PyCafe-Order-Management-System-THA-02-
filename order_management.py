orders = []


def add_order(order_id, item_name, quantity=1):
    order_details = {'order_id': order_id, 'item_name': item_name, 'quantity': quantity}

    # Check if the order_id already exists
    for order in orders:
        if order['order_id'] == order_id:
            print(f"Error: Order with ID {order_id} already exists.")
            return

    orders.append(order_details)
    print(f"Order {order_id} for {quantity} {item_name}(s) added.")


def print_orders():
    print("\nAll Orders\n")
    for order in orders:
        print(f"Order ID: {order['order_id']}, Item: {order['item_name']}, Quantity: {order['quantity']}")


def main():
    # Call the add_order function to add a few orders.
    add_order(1, "Latte", 2)
    add_order(2, "Croissant")
    add_order(3, "Veggie Sandwich", 3)

    print_orders()


if __name__ == '__main__':
    main()
