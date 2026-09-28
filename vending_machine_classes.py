"""Vending machine program
Author: Harry Wilson
To do: pause feature"""

from datetime import datetime

initial_stock = {
    "A1": {"name": "Bacon Crisps", "price": 0.75, "stock": 10},
    "A2": {"name": "Salted Crisps", "price": 0.75, "stock": 10},
    "B1": {"name": "Chocolate Bar", "price": 0.90, "stock": 10},
    "C1": {"name": "Apple Pieces", "price": 0.50, "stock": 10},
    "C2": {"name": "Raisins", "price": 0.85, "stock": 10},
}  # dictonary of vending machine stock


class Stock:
    """Represents the stock of a vending machine item."""

    machine = {}

    def add_stock(self, code, name, price, stock):
        """Adds a new item to the vending machine stock."""
        self.machine[code] = {"name": name, "price": price, "stock": stock}

    def update_stock(self, code, amount):
        """Updates the stock of an existing item in the vending machine."""
        if code in self.machine:
            self.machine[code]["stock"] += amount
        else:
            print("Not a Valid Code")

    def display_stock(self):
        """Displays the vending machine items, their prices, and current stock."""
        new_line(2)
        date_now = now_ts()
        print(f"Vending machine - {date_now}")
        for code, item in sorted(self.machine.items()):
            stock = item["stock"]
            print(f"[{code}] {item['name']}: £{item['price']:.2f} - {stock} left")

    def vaild_code(self, code):
        """Checks if a code is valid."""
        return code in self.machine

    def get_product(self, code):
        """Retrieves a product from the vending machine stock."""
        return self.machine.get(code, None)

    def sorted_items(self):
        """Returns the vending machine items sorted by code."""
        return sorted(self.machine.items())

    def get_stock(self, code):
        """Returns the stock of a specific item."""
        product = self.get_product(code)
        if product:
            return product["stock"]
        return 0


def now_ts():
    """Returns the current date and time as a string."""
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def main():
    """Main function to run the vending machine program."""

    working = True
    profit = 0.0
    stock = Stock()
    for code, item in initial_stock.items():
        stock.add_stock(code, item["name"], item["price"], item["stock"])

    while working is True:
        display(stock)
        working = choice(profit, stock)


def new_line(lines):
    """Prints a specified number of new lines."""
    print("\n" * lines)


def display(stock):
    """Displays the vending machine items and their prices."""
    new_line(2)
    date_now = now_ts()
    print(f"Vending machine - {date_now}")
    for code, item in stock.sorted_items():
        if item["stock"] > 0:
            print(f"[{code}] {item['name']}: £{item['price']:.2f}")

        else:
            print(f"[{code}] {item['name']}: OUT OF STOCK")
    print(
        "Enter 'R' to restock, 'P' to view profit, 'S' to stock machine, or 'END' to exit."
    )


def choice(profit, stock):
    """Handles user input for money and product selection."""

    new_line(2)
    user_code = input("Enter the product's code: ")  # asks for the product code
    user_code = user_code.upper()  # converts it to uppercase

    if stock.vaild_code(user_code) and stock.get_product(user_code)["stock"] > 0:
        product = stock.get_product(user_code)
        money = input("Enter some money (£?.?)")  # user inputs money
        money = money.replace("£", "")  # removes £ symbol if it was included
        money = money.replace(",", "")  # removes commas if they were included
        try:
            money = float(money)  # converts it into a float

        except ValueError:
            new_line(2)
            print("Invalid value for money. Please enter a valid amount.")
            return True

        if money > 100:
            new_line(2)
            print("That's a lot of money! Please enter a smaller amount.")
            return True

        if money >= product["price"]:
            cost = discount(product["price"])
            profit += cost
            money -= cost
            product["stock"] -= 1
            print(new_line(2))
            print(f"Dispensing {product['name']}. Enjoy!")
            print(f"Dispensing £{money:.2f} change.")

        else:
            new_line(2)
            print("Not enough money")
            print(f"Price: £{product['price']:.2f}")
            print(f"Your money: £{money:.2f}")

    elif user_code == "R":
        restock(stock)

    elif user_code == "P":
        new_line(2)
        print(f"Total profit £{profit}")

    elif user_code == "S":
        stock_machine(stock)

    elif user_code == "END":
        new_line(2)
        print(f"Total profit £{profit}")
        return False

    elif stock.get_stock(user_code) <= 0:
        new_line(2)
        print("Out of stock")

    else:
        new_line(2)
        print("INVALID CODE")

    return True


def restock(stock):
    """Restocks the vending machine items with new stock."""

    stock.display_stock()

    new_line(2)
    restocking = input("Would you like to restock (Y/N)? ")

    while restocking.upper() == "Y":
        new_line(2)
        user_code = input("Enter the product's code: ")

        if stock.valid_code(user_code):

            amount = input("How many do you want to add: ")

            try:
                amount = int(amount)
                stock.update_stock(user_code, amount)
            except ValueError:
                new_line(2)
                print("Invalid value for amount. Please enter a valid integer.")

        else:
            new_line(2)
            print("Not a Valid Code")
            display(stock)

        new_line(2)
        restocking = input("Would you like to restock again (Y/N)? ")


def stock_machine(stock):
    """Displays the current stock of the vending machine items."""

    stock.display_stock()

    stocking = "Y"

    while stocking.upper() == "Y":

        stocking = input(
            "Would you like to stock the machine with a new product (Y/N)? "
        )
        new_line(2)
        key = input("Enter the new product code: ")
        name = input("Enter the new product name: ")
        price = input("Enter the new product price: ")
        price = price.replace("£", "")
        stock = input("Enter the new product stock: ")

        try:
            price = float(price)
            price_ready = True

        except ValueError:
            print("Invalid value for price. Please enter valid numbers.")

        try:
            stock = int(stock)
            stock_ready = True

        except ValueError:
            print("Invalid value for stock. Please enter valid numbers.")

        if len(key) != 2:
            print("Invalid code. Code must be 2 characters long.")
            key_ready = False

        else:
            key_ready = True

        if price_ready and stock_ready and key_ready:
            stock.add_stock(key, name, price, stock)


def discount(price):
    """Determines if a discount applies based on the day and user status."""
    today = datetime.now()
    today = today.strftime("%A")

    if today == "Saturday":
        print("No Discount")

    else:
        new_line(2)
        student = input("Is student (Y/N): ")

        if student.upper() == "Y":
            new_line(1)
            print("Half Price")
            price = discount_half(price)

        else:
            discount_abilliaty = input("Has discount card (Y/N): ")

            if discount_abilliaty.upper() == "Y":
                new_line(1)
                print("Half Price")
                price = discount_half(price)

            else:
                new_line(1)
                print("No Discount")
    return price


def discount_half(price):
    """Applies a half price discount to the given price."""
    price /= 2
    return price


if __name__ == "__main__":
    main()
