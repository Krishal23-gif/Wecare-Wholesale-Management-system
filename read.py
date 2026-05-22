def read_product_data(filename="products.txt"):
    products = {}
    try:
        file = open(filename, "r")
        lines = file.readlines()
        product_id = 1
        for line in lines:
            parts = line.split(",")
            if len(parts) == 5:
                products[product_id] = [
                    parts[0].replace("\n", ""),
                    parts[1].replace("\n", ""),
                    parts[2].replace("\n", ""),
                    parts[3].replace("\n", ""),
                    parts[4].replace("\n", "")
                ]
                product_id += 1
        file.close()
    except FileNotFoundError:
        print("Error: Product file not found.")
    except Exception as error:
        print("An unexpected error occurred: " + str(error))
    return products
