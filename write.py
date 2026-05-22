def write_product_data(products, filename="products.txt"):
    try:
        file = open(filename, "w")
        for product_id in products:
            line = products[product_id][0] + "," + products[product_id][1] + "," + products[product_id][2] + "," + products[product_id][3] + "," + products[product_id][4] + "\n"
            file.write(line)
        file.close()
    except Exception as error:
        print("Error writing to file: " + str(error))
