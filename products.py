
class Product:
    def __init__(self, name:str, price:float, quantity:int):
            if not name.strip():
                raise ValueError('Name cannot be an empty string')
            if price < 0 :
                raise ValueError('Price cannot be negative')
            if quantity <0:
                raise ValueError('Quantity cannot be negative ')
            self.name = name
            self.price = price
            self.quantity = quantity
            self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity:int):
        if quantity < 0:
            raise ValueError('Quantity cannot be negative')
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity:int) -> float :
        if quantity <= 0:
            raise ValueError("Purchase quantity must be positive")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")
        if not self.active:
            raise Exception('Product is inactive and cannot be purchased')

        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    bose.show()
    mac.show()
    bose.set_quantity(1000)
    bose.show()

if __name__ == '__main__':
    main()










