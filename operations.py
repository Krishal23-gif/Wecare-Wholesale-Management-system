from datetime import datetime
from write import write_product_data

def display_product_table(products):
    print("\n" + "=" * 90)
    print("AVAILABLE PRODUCTS".center(90))
    print("=" * 90)
    print("ID\tName\t\t\tBrand\t\t\tQty\tPrice\tOrigin")
    print("-" * 90)
    for product_id in products:
        name = products[product_id][0]
        brand = products[product_id][1]
        quantity = products[product_id][2]
        price = str(int(products[product_id][3]) * 2)
        origin = products[product_id][4]
        print(str(product_id) + "\t" + name + "\t" + brand + "\t\t" + quantity + "\t" + price + "\t" + origin)
    print("-" * 90 + "\n")

def handle_sale(products):
    customer_name = ""
    while customer_name == "":
        customer_name = input("Enter customer name: ")
        if customer_name == "":
            print("Customer name cannot be empty.")

    while True:
        try:
            customer_phone = int(input("Enter customer phone number: "))
            break
        except ValueError:
            print("Invalid phone number. Digits only.")

    sold_items = []
    total_amount = 0

    while True:
        display_product_table(products)
        try:
            product_id = int(input("Enter product ID to sell: "))
            if product_id not in products:
                print("Invalid product ID.")
                continue

            quantity = int(input("Enter quantity to sell: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            available = int(products[product_id][2])
            unit_price = int(products[product_id][3]) * 2
            free_items = quantity // 3
            total_required = quantity + free_items

            if total_required > available:
                print("Insufficient stock available.")
                continue

            products[product_id][2] = str(available - total_required)
            total_cost = quantity * unit_price

            sold_items.append([product_id, products[product_id][0], quantity, free_items, unit_price, total_cost])
            total_amount = total_amount + total_cost
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue

        more = input("Add another item? (yes/no): ")
        if more.lower() != "yes":
            break

    shipping_cost = 0
    if total_amount < 1000:
        shipping_cost = total_amount * 0.10

    grand_total = total_amount + shipping_cost
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "invoice_" + timestamp + ".txt"
    file = open(filename, "w")

    print("\n" + "=" * 90)
    print("WeCare Wholesale".center(90))
    print("Kamalpokhari, Kathmandu | Phone: 9812345670".center(90))
    print("SALES INVOICE".center(90))
    print("=" * 90)
    print("Customer Name : " + customer_name)
    print("Phone Number  : " + str(customer_phone))
    print("Date          : " + str(datetime.now()))
    print("-" * 90)
    print("No  Product Name        Qty  Free   Price  Total")
    print("-" * 90)

    file.write("=" * 90 + "\n")
    file.write("WeCare Wholesale".center(90) + "\n")
    file.write("Kamalpokhari, Kathmandu | Phone: 9812345670".center(90) + "\n")
    file.write("SALES INVOICE".center(90) + "\n")
    file.write("=" * 90 + "\n")
    file.write("Customer Name : " + customer_name + "\n")
    file.write("Phone Number  : " + str(customer_phone) + "\n")
    file.write("Date          : " + str(datetime.now()) + "\n")
    file.write("-" * 90 + "\n")
    file.write("No  Product Name        Qty  Free   Price  Total\n")
    file.write("-" * 90 + "\n")

    count = 1
    for item in sold_items:
        row = str(count) + "   " + item[1] + " " * (20 - len(item[1])) + str(item[2]) + "    " + str(item[3]) + "    " + str(item[4]) + "   " + str(item[5])
        print(row)
        file.write(row + "\n")
        count = count + 1

    print("-" * 90)
    print("Subtotal      : Rs. " + str(total_amount))
    if shipping_cost > 0:
        print("Shipping (10%): Rs. " + str(shipping_cost))
    print("Grand Total   : Rs. " + str(grand_total))
    print("=" * 90)
    print("Thank you for shopping with us!".center(90))
    print("=" * 90 + "\n")

    file.write("-" * 90 + "\n")
    file.write("Subtotal      : Rs. " + str(total_amount) + "\n")
    if shipping_cost > 0:
        file.write("Shipping (10%): Rs. " + str(shipping_cost) + "\n")
    file.write("Grand Total   : Rs. " + str(grand_total) + "\n")
    file.write("=" * 90 + "\n")
    file.write("Thank you for shopping with us!".center(90) + "\n")
    file.write("=" * 90 + "\n")
    file.close()

    write_product_data(products)
    print("Bill has been saved to file: " + filename)

from datetime import datetime
from write import write_product_data

def handle_restock(products):
    display_product_table(products)
    try:
        product_id = int(input("Enter product ID to restock: "))
        if product_id not in products:
            print("Invalid product ID.")
            return
        quantity = int(input("Enter quantity to add: "))
        if quantity <= 0:
            print("Quantity must be positive.")
            return

        current_quantity = int(products[product_id][2])
        new_quantity = current_quantity + quantity
        products[product_id][2] = str(new_quantity)
        write_product_data(products)

        # Create restock invoice
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = "restock_" + timestamp + ".txt"
        file = open(filename, "w")

        print("\n" + "=" * 90)
        print("WeCare Wholesale".center(90))
        print("Kamalpokhari, Kathmandu | Phone: 9812345670".center(90))
        print("RESTOCK RECEIPT".center(90))
        print("=" * 90)
        print("Product Restocked:")
        print("-" * 90)
        print("ID   Product Name           Brand              Added   New Stock")
        print("-" * 90)

        name = products[product_id][0]
        brand = products[product_id][1]

        row = str(product_id) + "   " + name + " " * (22 - len(name)) + brand + "  " * (18 - len(brand)) + str(quantity) + "      " + str(new_quantity)
        print(row)
        print("-" * 90)
        print("Stock updated successfully.\n")

        # File writing
        file.write("=" * 90 + "\n")
        file.write("WeCare Wholesale".center(90) + "\n")
        file.write("Kamalpokhari, Kathmandu | Phone: 9812345670".center(90) + "\n")
        file.write("RESTOCK RECEIPT".center(90) + "\n")
        file.write("=" * 90 + "\n")
        file.write("Product Restocked:\n")
        file.write("-" * 90 + "\n")
        file.write("ID   Product Name           Brand             Qty Added   New Stock\n")
        file.write("-" * 90 + "\n")
        file.write(row + "\n")
        file.write("-" * 90 + "\n")
        file.write("Stock updated successfully.\n")
        file.close()

        print("Restock receipt saved as:", filename)

    except ValueError:
        print("Invalid input. Numbers only.")

