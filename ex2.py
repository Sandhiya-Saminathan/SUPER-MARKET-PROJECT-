import datetime

class Supermarket:
    def __init__(self):
        self.products = {
            "milk": 20,
            "sugar": 15,
            "oil": 120,
            "rice": 60,
            "vegetables": 100,
            "fruits": 50
        }
        self.bill = {}

    def check_availability(self, product):
        return product in self.products

    def calculate_total(self, product, quantity):
        return self.products[product] * quantity

    def add_to_bill(self, product, quantity):
        if product in self.bill:
            self.bill[product] += quantity
        else:
            self.bill[product] = quantity

    def generate_bill(self):
        total = 0
        bill_content = "Supermarket Bill\n"
        bill_content += "----------------\n"
        for product, quantity in self.bill.items():
            price = self.calculate_total(product, quantity)
            bill_content += f"{product}: {quantity} x ${self.products[product]:.2f} = ${price:.2f}\n"
            total += price
        bill_content += "----------------\n"
        bill_content += f"Total: ${total:.2f}\n"
        current_time = datetime.datetime.now()
        bill_content += f"Generated on: {current_time.strftime('%Y-%m-%d %H:%M:%S')}\n"

        with open("bill.txt", "w") as f:
            f.write(bill_content)

        return bill_content

    def main(self):
        while True:
            your_products = input("Enter your item (or type 'done' to finish): ").strip().lower()
            if your_products == 'done':
                break
            if self.check_availability(your_products):
                print(f"Yes, {your_products} is available.")
                try:
                    quantity = int(input(f"How many {your_products} do you want: "))
                    if quantity <= 0:
                        raise ValueError("Quantity must be positive.")
                    self.add_to_bill(your_products, quantity)
                    print(f"{quantity} {your_products}(s) added to your bill.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print(f"Sorry, {your_products} is not available.")

        if self.bill:
            print("\nGenerating bill...\n")
            print(self.generate_bill())
            print(f"Bill written to 'bill.txt'.")
        else:
            print("No items were purchased.")

if __name__ == "__main__":
    market = Supermarket()
    market.main()
