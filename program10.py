# In-Memory Inventory Tracker


def merge_inventory(*stores):
    """Merge inventory from multiple store dictionaries."""
    inventory = {}

    for store in stores:
        for product, quantity in store.items():
            inventory[product] = inventory.get(product, 0) + quantity

    return inventory


def get_stock(inventory, product):
    """Safely get stock for a product."""
    return inventory.get(product, 0)


def low_stock(inventory, limit=10):
    """Find products with stock below the given limit."""
    return {
        product: quantity
        for product, quantity in inventory.items()
        if quantity < limit
    }


def add_inventory(inventory, updates):
    """Merge/update inventory using dictionary update operator."""
    inventory |= updates
    return inventory


# -------------------------
# Store Inventories
# -------------------------

store1 = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15,
    "Monitor": 8
}

store2 = {
    "Laptop": 5,
    "Mouse": 20,
    "Headphones": 12,
    "Monitor": 7
}

store3 = {
    "Laptop": 3,
    "Keyboard": 10,
    "Headphones": 8
}


# Merge all stores
inventory = merge_inventory(store1, store2, store3)

print("Combined Inventory:")
print(inventory)


# Check product stock
print("\nLaptop stock:", get_stock(inventory, "Laptop"))
print("Tablet stock:", get_stock(inventory, "Tablet"))


# Find low-stock products
print("\nLow Stock:")
print(low_stock(inventory, 15))


# Add new inventory
new_stock = {
    "Laptop": 5,
    "Tablet": 10
}

add_inventory(inventory, new_stock)

print("\nAfter Inventory Update:")
print(inventory)
