from products import Product

class Store:
    """
    Represents a store that holds and manages multiple products.

    Methods:
        add_product(product: Product): Adds a product to the store.
        remove_product(product: Product): Removes a product from the store.
        get_total_quantity() -> int: Returns the total stock of all products.
        get_all_products() -> list[Product]: Returns all active products.
        order(shopping_list: list[tuple[Product, int]]) -> float:
            Processes an order of multiple products and returns the total cost.
    """
    def __init__(self,products:list[Product]):
        self.products = products

    def add_product(self,product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self):
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list) -> float:
        total_price = 0
        for product,quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()

if __name__ == '__main__':
    main()









