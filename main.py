import os

#A
def Add_product():
    with open("Product.txt", "a") as product_file:
        while True:
            product_id = input("Enter Product ID [4 numbers -> XXXX]: ")
            #Avoiding empty fields
            if not product_id:
                print("Error: Product ID cannot be empty.")
                continue
            #Make Sure The Product ID Is In A Form Of Integers
            if not product_id.isdigit():
                print("Error: ID must be number.")
                continue
            #Avoiding ID More or below than 4 characters
            if len(product_id) != 4:
                print("Error: Product ID must be exactly 4 numbers.")
                continue
            
        
            #Avoid Duplication
            is_duplicate = False
            try:
                with open("Product.txt", "r") as file:
                    products = file.readlines()
                    for i in range(0, len(products), 5):
                        if products[i].strip() == product_id:
                            print("Error: Product ID already exists. Please use a unique ID.")
                            is_duplicate = True
                            break
    
            except FileNotFoundError:
                pass
                
            if is_duplicate:
                continue
            
            break
            
        while True:
            product_name = input("Product Name: ")   
            if not product_name:
                print("Error: Product Name cannot be empty.")
                continue
            break
        
        while True:
            product_desc = input("Product Description: ")
            if not product_desc:
                print("Error: Product Description cannot be empty.")
                continue
            break
        
        while True: 
            product_price = input("Product Price (in MYR): ")
            #Make Sure The Product Price Is In A Form Of Number
            if not product_price.isdigit():
                print("Error: Price must be number.")
                continue
            if not product_price:
                print("Error: Product Price cannot be empty.")
                continue
            break
           
        while True: 
            product_quantity = input("Product Quantity: ")
            #Make Sure The Product Quantity Is In A Form Of Number
            if not product_quantity.isdigit():
                print("Error: Quantity must be number.")
                continue
            if not product_quantity:
                print("Error: Product Quantity cannot be empty")
                continue
            break
            
        product_file.write(f"{product_id}\n{product_name}\n{product_desc}\n{product_price}\n{product_quantity}\n") #put \n at the end to make a new line

        print("Product Added Successfully!")

#B 
def Update_product():
    try:
        with open("Product.txt", "r") as file:
            products = file.readlines()

        print("-------------------------")
        print("   Current Product List   ")
        print("")
        View_Inventory(username)
        print("")

        product_id = input("Enter the Product ID you wish to update: ")
        print("")
        updated_products = []
        found = False

        for i in range(0, len(products),5):  # Each product consists of  lines
            if products[i].strip() == product_id:
                found = True
                print("------- Current Product Details -------")
                print(f"Name                        : {products[i+1].strip()}")
                print(f"Description                 : {products[i+2].strip()}")
                print(f"Price (In MYR)              : {products[i+3].strip()}")
                print(f"Product Quantity            : {products[i+4].strip()}")
                print("")

                # New Data from User
                new_name = input("Enter a new Product Name (or press Enter to keep current data): ") or products[i+1].strip()
                new_desc = input("Enter a new Product Description (or press Enter to keep current data): ") or products[i+2].strip()
                new_price = input("Enter a new Product Price (or press Enter to keep current data): ") or products[i+3].strip()
                new_quan = input("Enter a new Product Quantity (or press Enter to keep current data): ") or products[i+4].strip()

                # Append updated product details
                updated_products.extend([product_id + "\n", new_name + "\n", new_desc + "\n", new_price + "\n", new_quan + "\n"])
            else:
                # Append current product details if no update is needed
                updated_products.extend(products[i:i+5])

        if not found:
            print("Product ID not found.")
        else:
            with open("Product.txt", "w") as file:
                file.writelines(updated_products)
            print("Product updated successfully!")

    except FileNotFoundError:
        print("Product.txt file does not exist. Please add products first.")


#C  
def add_supplier(filename="suppliers.txt"):
    supplier_id = input("Enter Supplier ID: ").strip()  
    name = input("Enter Supplier Name: ").strip()  
    contact = input("Enter Supplier Contact: ").strip()  

    if not name or not contact:
        print("Error: All fields are required.")
        return False
    if not contact.isdigit():
        print("Error: Contact must be numeric.")
        return False

    try:
        suppliers = []
        with open(filename, "r") as file:
            suppliers = [line.strip().split(",") for line in file]

        if any(supplier[0] == supplier_id for supplier in suppliers):
            print("Error: Supplier ID already exists.")
            return False
    except FileNotFoundError:
        print(f"Note: '{filename}' not found. Creating a new one.")

    try:
        with open(filename, "a") as file:
            file.write(f"{supplier_id}\n{name}\n{contact}\n")
        print("Supplier added successfully!")
        return True
    except Exception as e:
        print(f"Error: Unable to save supplier data. {e}")
        return False


#D
from datetime import datetime

# Record delivery status of order:
def get_delivery_status():
    options = ["Incomplete", "Pending", "Done"]
    print("Select order status:")
    for i, option in enumerate(options, start=1):
        print(f"{i}, {option}")
    while True:
        try:
            choice = int(input("Select the number corresponding to current delivery status of order:"))
            if 1 <= choice <= len(options):
                return options[choice - 1]
            else:
                print("Please select a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please select a number.")

# Function to place order:
def place_order():
    timestamp = datetime.now(tz= None).strftime("%d/%m/%Y %H:%M:%S")
    product_id = input("Enter product ID to order:")
    while True:
        try:
            order_quantity = int(input("Enter quantity to order:"))
            break
        except ValueError:
            print("Invalid quantity. Please enter a number.")
    supplier_id = input("Enter supplier ID:")
    delivery_status = get_delivery_status()
    
    # Update orders file:
    order_details = f"{timestamp}, {product_id}, {order_quantity}, {supplier_id}, {delivery_status}\n"            
    with open("orders.txt", "a") as file:
        file.write(order_details)
    
    # Generate receipt/invoice:
    print("\nOrder placed succesfully.")
    print(f"Product: {product_id}")
    print(f"order quantity: {order_quantity}")
    print(f"Supplier: {supplier_id}")
    print(f"Delivery status: {delivery_status}")
    print(f"Timestamp: {timestamp}")
   
   
#E
def View_Inventory(username):
    try:
        with open("Product.txt", "r") as file:
            products = file.readlines()
        
            var = 1

            for i in range(0, len(products), 5): 
                products[i].strip()
                print(f"------- Product {var} -------")
                print(f"ID                : {products[i].strip()}")
                print(f"Name              : {products[i+1].strip()}")
                print(f"Description       : {products[i+2].strip()}")
                print(f"Price (In MYR)    : {products[i+3].strip()}")
                print(f"Quantity          : {products[i+4].strip()}")
                print("")
                var += 1
        file.close()

        print(f"Current inventory item count: {var-1}")
        print("")

    except FileNotFoundError:
        print(f"No product has been added yet, please add a product first, {username}.")
    
    try:
        with open("suppliers.txt", "r") as file:
            supplier = file.readlines()

            var = 1

            for i in range(0, len(supplier), 3):
                supplier[i].strip()
                print(f"------- Supplier {var} -------")
                print(f"Supplier ID       : {supplier[i].strip()}")
                print(f"Supplier Name     : {supplier[i+1].strip()}")
                print(f"Supplier Contact  : {supplier[i+2].strip()}")
                print("")
                var += 1
        file.close()

        print(f"Current supplier count: {var-1}")

    except FileNotFoundError:
        print(f"No supplier has been added yet, please add a supplier first, {username}.")   
                
#F
def report():
    print("------- REPORT -------")

    try:
        with open("Product.txt", "r") as file:
            product = file.readlines()

            if not product:
                print("No products found in inventory.")
                return

            # Initialize variables
            total_products = 0
            total_price = 0
            most_expensive_product = None
            most_expensive_price = float("-inf")
            cheapest_product = None
            cheapest_price = float("inf")
            products_list = []
            total_quantity = 0

            # Loop through products
            for i in range(0, len(product), 5):  # Each product entry has 4 lines
                product_id = product[i].strip()
                product_name = product[i + 1].strip()
                product_desc = product[i + 2].strip()
                product_price = float(product[i + 3].strip())
                product_quantity = float(product[i + 4].strip())

                # Update statistics
                total_products += 1
                total_price += product_price
                total_quantity += product_quantity

                # Check for most expensive product
                if product_price > most_expensive_price:
                    most_expensive_product = product_name
                    most_expensive_price = product_price

                # Check for cheapest product
                if product_price < cheapest_price:
                    cheapest_product = product_name
                    cheapest_price = product_price

                # Check low stock products
                if product_quantity <= 10:
                    print("This product is low on stock.")

                # Add product to list
                products_list.append({
                    "ID": product_id,
                    "Name": product_name,
                    "Description": product_desc,
                    "Price": product_price,
                    "Quantity": product_quantity
                })


            # Calculate average price
            average_price = total_price / total_products if total_products > 0 else 0
        

            # Display Report
            print(f"1. Total Products: {total_products}")
            print(f"2. Total Inventory Value: MYR {total_price:.2f}")
            print(f"3. Average Product Price: MYR {average_price:.2f}")
            print(f"4. Most Expensive Product: {most_expensive_product} (MYR {most_expensive_price:.2f})")
            print(f"5. Cheapest Product: {cheapest_product} (MYR {cheapest_price:.2f})")
            print(f"6. Total Product Quantity: {total_quantity}")
            print("\n6. Products List:")


            for product in products_list:
                print(f"   ID: {product['ID']}, Name: {product['Name']}, Price: MYR {product['Price']:.2f}")

    except FileNotFoundError:
        print("No products found. Please add products first.")

    print("\n---------------------------------------\n")


#G
def main():
    global username
    username = input("Welcome to the system! Please kindly enter your name : ")
    #UserInitialInterface
    print("")
    print(f"Hello {username}. What can we do for you today?")

    counter = 1

    while counter == 1:
        print("")
        print("--------------- ACTION LIST ---------------")
        print("[1] Add a new product")
        print("[2] Update a product detail")
        print("[3] Add a new supplier")
        print("[4] Place an order")
        print("[5] View inventory")
        print("[6] Generate report")
        print("")
        print("[7] About us")
        print("[8] Exit the program")
        print("-------------------------------------------")
        print("")

        try: 
            userinput = int(input("Please enter the number of your wanted action (1-8): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        #[1] Add a new product
        if userinput == 1:
            Add_product()

        #[2] Update a product detail
        elif userinput == 2:
            Update_product()

        #[3] Add a new supplier
        elif userinput == 3:
            add_supplier()
        
        #[4] Place an order
        elif userinput == 4:
            place_order()
        
        #[5] View Inventory
        elif userinput == 5:
            View_Inventory(username)

        #[6] Generate report
        elif userinput == 6:
            report()   

        #[7] About us
        elif userinput == 7:
            print("")
            print("-------------------------------------------")
            print("Meet the AMAZING members of our group! :")
            print("[1] Kayxin Haydnsen Citro")
            print("[2] Mabellyn Chan May Ji")
            print("[3] Nicholas Andersen Salim")
            print("[4] Reina Miyasako")
            print("[5] Yohan Lim")
            print("-------------------------------------------")
            print("")

            #Continue
            usercontinue = input("Do you still want to continue using our program? (y/n) : ")
            usercontinue = usercontinue.lower()

            if usercontinue == "y":
                counter = 1
            elif usercontinue == "n":
                counter = 0
            else:
                print("Invalid input. Redirecting to home page.")
                counter = 1

        #[8] Exit
        elif userinput == 8:
            counter = 0

        #Invalid input
        else:
            print("Number invalid. please enter a number from our service.")

    #Exit
    print("Thank you for using our program!")

main()