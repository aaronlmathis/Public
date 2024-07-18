def add_product(inventory, product_name, quantity, price):
    if product_name in inventory:
        print(f"Product '{product_name}' already exists.")
    else:
        inventory[product_name] = {'quantity': quantity, 'price': price}

def update_product(inventory, product_name, quantity=None, price=None):
    if product_name not in inventory:
        print(f"Product '{product_name}' does not exist.")
    else:
        if quantity is not None:
            inventory[product_name]['quantity'] = quantity
        if price is not None:
            inventory[product_name]['price'] = price

def delete_product(inventory, product_name):
    if product_name in inventory:
        del inventory[product_name]
    else:
        print(f"Product '{product_name}' does not exist.")

def view_inventory(inventory):
    if not inventory:
        print("Inventory is empty.")
    else:
        for product_name, details in inventory.items():
            print(f"Product: {product_name}, Quantity: {details['quantity']}, Price: {details['price']}")

def calculate_total_value(inventory):
    total_value = sum(details['quantity'] * details['price'] for details in inventory.values())
    return total_value

# Example usage
inventory = {}
add_product(inventory, 'apple', 50, 0.5)
add_product(inventory, 'banana', 100, 0.2)
update_product(inventory, 'apple', quantity=60)
update_product(inventory, 'banana', price=0.25)
view_inventory(inventory)
delete_product(inventory, 'banana')
total_value = calculate_total_value(inventory)
print(f'Total Inventory Value: ${total_value}')
