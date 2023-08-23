from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
        self.country =country
        self.code = code
        self.product = product 
        self.cost = float(cost)
        self.quantity = int(quantity)
    
        


    def get_cost(self):
        return self.cost
        '''
        Add the code to return the cost of the shoe in this method.
        '''

    def get_quantity(self):
        return self.quantity
        '''
        Add the code to return the quantity of the shoes.
        '''

    def __str__(self):
        shoe_info = [[self.country,self.code, self.product, f"{self.cost:,.2f}",self.quantity]]
        shoe_tab = tabulate(shoe_info, headers=["Country", "Code", "Product", "Cost", "Quantity"],tablefmt="simple_outline")
        return shoe_tab
        
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    content = []
    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code
    '''
    with open('inventory2.txt','r') as f:
        for line in f: 
            content.append(line)
    
    content.pop(0)
    for item in content:
        product_country, product_code, product_decript, product_cost, product_quantity = item.split(",")
        product = Shoe(product_country,product_code,product_decript,product_cost,product_quantity)
        shoe_list.append(product)

        
   

def capture_shoes():
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
    shoe_code = input("\n\nEnter shoe product code : ")
    shoe_type = input("Enter shoe description/type : ")
    shoe_country = input("Enter location/country of the stock : ")

    while True:
        try:
            shoe_cost = float( input("Enter the cost of the product : ")) 
            break
        except ValueError:
            print("OOOPS! Invalid Entry. Please Try again. ")

    while True:
        try:
            shoe_quantiy = int (input( "Enter the quantity of the shoe in stock : "))
            break
        except ValueError: 
            print("OOOPS! Invalid Entry. Please Try again. ")
    
    new_shoe = Shoe(shoe_country,shoe_code,shoe_type,shoe_cost,shoe_quantiy)
    shoe_list.append(new_shoe)
    print("\n\nThe following shoe has been successfully added to the inventory listing : ")
    print(new_shoe)


def print_table():
    '''
    This function will create data for the table to be stored in a 
    lists of lists then append the table data with shoelist info so it can be printed in a table format
      '''
    shoe_table = [["Country", "Code", "Product", "Cost", "Quantity"]]

    for shoe in shoe_list:
        shoe_table.append([shoe.country, shoe.code, shoe.product, f"R{shoe.cost:,.2f}", shoe.quantity])
    
    print("\n\nTotal Inventory Listing :\n")
    print(tabulate(shoe_table, headers="firstrow", tablefmt="psql"))


def view_all():
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''
 
    if len(shoe_list) <= 0 :
        read_shoes_data()
        print_table()
               
    else:
        print_table()
         
def write_to_file (listz):
    with open('inventory2.txt', 'w') as file :
        file.write("Country,Code,Product,Cost,Quantity\n")
        for item in listz:
            file.write(f"{item.country},{item.code},{item.product},{int(item.cost)},{item.quantity}\n")

    



def re_stock():
    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''
    if len(shoe_list)<=0 :
        print("OOOPs you haven't imported any data yet. Please load data first then continue. ")
    
    else:
        list_quantities = [shoe_quant.get_quantity() for shoe_quant in shoe_list]
        lowest_gty = min(list_quantities)
    #shoes with lowest qty 
        lowstock_table = [["Country", "Code", "Product", "Cost", "Quantity"]]
        low_stock = [low_shoe  for low_shoe  in shoe_list if low_shoe.get_quantity() == lowest_gty]
        for stock in low_stock:
            lowstock_table.append([stock.country, stock.code, stock.product, f"R{stock.cost:,.2f}", stock.quantity])

        print("\n\nThe following shoes have the lowest levels of stock : ")
        print(tabulate(lowstock_table,headers= "firstrow",tablefmt="simple_outline" ))
    
    #Identify the low cost item in the shoe list and change its quantity and update the file 
        while True: 
            restock_query = input("\n\nDo you want to restock these products : \n (a)- Yes \n (b)- No ")   
            if restock_query == 'a' :
                for shoe_a in low_stock:
                    for shoe_b in shoe_list:
                        if shoe_a == shoe_b:
                         
                         while True:
                                try:
                                    restock_qty = int(input(f"Enter restock quantity for {shoe_b.code}:  "))
                                    break
                                except ValueError:
                                    print("Invalid entry. Please try again.")
                        
                         shoe_b.quantity += restock_qty
                         print("\n\nProduct quantity has been updated successfully : ")
                         print(shoe_b)
                         write_to_file(shoe_list)
                         print("\nInventory file has been updated successfully! ")
                break
        
            elif restock_query == 'b':
                break
            else:
                print("Invalid Entry. Please try again. ")



def seach_shoe():
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
     request shoe code from user  and search using filter function.
     assuemed multiple entries in different countries could have the same code 
    '''
    if len(shoe_list)<=0 :
        print("OOOPs you haven't imported any data yet. Please load data first then continue. ")
    
    else: 

        while True:
            search_code = input("Enter shoe code : ")
            if any(shoe_object.code == search_code for shoe_object in shoe_list):
                found_shoes = filter(lambda shoe_x: shoe_x.code == search_code, shoe_list)
                shoefound_table = [["Country", "Code", "Product", "Cost", "Quantity"]]
                for shoe_t in found_shoes:
                    shoefound_table.append([shoe_t.country, shoe_t.code, shoe_t.product, f"R{shoe_t.cost:,.2f}", shoe_t.quantity])

                print(f"\n\nShoes Info with product code {search_code} : ")
                print(tabulate(shoefound_table,headers= "firstrow",tablefmt="simple_outline" ))
                break
        
            elif search_code == 'none':
                break
    
            else: 
                print("Invalid entry, please try again or type 'none' to return to main menu : ")





    

def value_per_item():  
    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''
    if len(shoe_list)<=0 :
        print("OOOPs you haven't imported any data yet. Please load data first then continue. ")

    else: 
        totalvalue_table = [["Country", "Code", "Product", "Cost", "Quantity","Total Value"]]
        for shoe_xv in shoe_list:
            shoe_cost = shoe_xv.get_cost()
            shoe_quantity = shoe_xv.get_quantity()
            shoe_val = float(shoe_cost)*float(shoe_quantity)
            totalvalue_table.append([shoe_xv.country, shoe_xv.code, shoe_xv.product, f"R{shoe_xv.cost:,.2f}", shoe_xv.quantity, f"R{shoe_val:,.2f}"])
        
        print ("\n\nTotal sock value report : ")
        print(tabulate(totalvalue_table,headers= "firstrow",tablefmt="simple_outline" ))    



def highest_qty():
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

    if len(shoe_list)<=0 :
        print("OOOPs you haven't imported any data yet. Please load data first then continue. ")
    
    else:
        list_high_quantities = [shoe_highquant.get_quantity() for shoe_highquant in shoe_list]
        highest_gty = max(list_high_quantities)
    #shoes with lowest qty 
        highstock_table = [["Country", "Code", "Product", "Cost", "Quantity"]]
        high_stock = [high_shoe  for high_shoe  in shoe_list if high_shoe.get_quantity() == highest_gty]
        for stock_h in high_stock:
            highstock_table.append([stock_h.country, stock_h.code, stock_h.product, f"R{stock_h.cost:,.2f}", stock_h.quantity])

        print("\n\nThe following shoes have are listed as for sale  : ")
        print(tabulate(highstock_table,headers= "firstrow",tablefmt="simple_outline" ))

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
while True:

    menu = input(''' \n \nSelect one of the following options below:
r - Read Shoe data 
a - Add new shoe details
va - View all shoe data
rs - Restock shoes
s - Search  a shoe
tp - Total Value of sku
hq - Highest quantity sku
e  - Exit 

               
''')
    

    if menu == 'r':
         read_shoes_data()
         print("\n\nAll shoe data has been imported successfully from file !")

    elif menu == 'a':
        capture_shoes()

    elif menu == 'va':
        view_all()
    
    elif menu == 'rs':
        re_stock()

    elif menu == 's':
        seach_shoe()
    
    elif menu == 'tp':
        value_per_item()

    elif menu == 'hq':
        highest_qty()

    elif menu == 'e':
        print("Goodbye !!!!")
        exit()
    
    else : 
        print("\nOOPs Incorrect selection. Please try again! ")