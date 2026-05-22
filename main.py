
from read import read_product_data
from operations import handle_sale, handle_restock, display_product_table

def main():
    print("\n" * 2)
    print("\t\t\t\t\t\tWeCare Wholesale")
    print("\t\t\tKamalpokhari, Kathmandu | Phone No: 9812345670")
    print("\n" + "=" * 90)
    print("\t\t\tWelcome to the system Admin! I hope you have a good day ahead!")
    print("=" * 90 + "\n")

    products = read_product_data()
    if not products:
        print("No product data found.")
        return

    while True:
        print("\n" + "-" * 60)
        print("MAIN MENU".center(60))
        print("-" * 60)
        print("1. Sell product to customer")
        print("2. Restock products from manufacturer")
        print("3. Exit the system")
        print("-" * 60)

        try:
            choice = int(input("Enter your choice (1, 2, or 3): "))
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")
            continue

        if choice == 1:
            handle_sale(products)
        elif choice == 2:
            handle_restock(products)
        elif choice == 3:
            print("\nThank you for using the system. Goodbye Admin!\n")
            break
        else:
            print("Invalid option. Please choose between 1, 2, or 3.")

if __name__ == "__main__":
    main()
