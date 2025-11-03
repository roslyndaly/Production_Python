# Simple Inventory Management System

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def remove_item(self, item_name, quantity):
        if item_name in self.items:
            if self.items[item_name] >= quantity:
                self.items[item_name] -= quantity
            else:
                print(f"Error: Not enough {item_name} to remove.")
        else:
            print(f"Error: Item '{item_name}' not found.")

    def check_inventory(self):
        return self.items


def main():
    inventory = Inventory()

    # Adding items to inventory
    inventory.add_item("Laptop", 10)
    inventory.add_item("Mouse", 25)
    inventory.add_item("Keyboard", 15)

    # Removing items from inventory
    inventory.remove_item("Mouse", 5)
    inventory.remove_item("Keyboard", 10)
    inventory.remove_item("Laptop", 5)

    # Checking the inventory status
    print("\nCurrent Inventory:")
    print(inventory.check_inventory())


if __name__ == "__main__":
    main()
