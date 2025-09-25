from products import Product
from store import Store

def list_products(store:Store):
    """Show all active products."""
    products = store.get_all_products()
    if not products:
        print('No products available')
        return
    for i,product in enumerate(products,start=1):
        print(f"{i}. {product.show()}")

def show_total_quantity(store: Store):
    """show total quantity of items in store"""
    total = store.get_total_quantity()
    print(f"Total of {total} items in store")

def make_order(store:Store):
    """Handle user orders interactively."""
    orders = []
    while True:
        products = store.get_all_products()
        if not products:
            print('No products available for ordering!')
            break

        print('\n Available products:')
        for i,p in enumerate(products, start=1):
            print(f"{i}. {p.show()}")

        print('\n enter 0 to finish your order')
        try:
            choice = int(input("Which product # do you want? "))
        except ValueError:
            print('Please enter a valid number.')
            continue
        if choice == 0:
            break
        if choice < 0 or choice > len(products):
            print("Invalid product number.")
            continue

        try:
            quantity = int(input("What amount do you want? "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if quantity < 0:
            print("Quantity must be positive.")
            continue
        orders.append((products[choice-1],quantity))

    if orders:
        try:
            total_price = store.order(orders)
            print(f"\n✅ Order placed! Total payment: ${total_price}")
        except Exception as e:
            print(f"Error processing order: {e}")
    else:
        print('No items were ordered.')

def start(store:Store):
    """Main menu loop."""
    menu_options = {
        1:list_products,
        2:show_total_quantity,
        3:make_order
    }

    while True:
        print("\n    Store Menu    ")
        print("    ----------     ")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            user_choice = int(input("Please choose a number: "))
        except ValueError:
            print('Invalid input. Please enter a number between 1 and 4 .')
            continue

        if user_choice == 4:
            print('Good Bye!')
            break

        action = menu_options.get(user_choice)
        if action:
            action(store)
        else:
            print('Please enter a valid option (1-4')





def main():
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)




if __name__ == "__main__":
    main()







