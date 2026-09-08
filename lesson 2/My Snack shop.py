# PART 1 - TYPES OF DATA
snack_name = "chips" 
price = 1.50 
quantity = 10
is_available = True

print("Snack:", snack_name)
print("price :$ ",price)
print("In Stock:",quantity)
print("Available?",is_available)

print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))


# PART 2 - ARITHMETIC OPERATORS
total = price * quantity
print("Total value : $",total)
print("sale price :$",price - 0.25)
print("Double Stock :",quantity *2)

# PART 3 - COMPARISON OPERATORS
print("Is price under $2?",price < 2)
print("More than 5 in the stock?",quantity > 5)
print("Is price exactly $1.50?",price ==1.50)


#PART 4 - STRING OPERATORS
shop_name = "Quick" + " "+"Bites"
print("Shop name :", shop_name)
print("Letters in snack name:", len (snack_name))
print("First Letter:",snack_name[0])


# PART 5 - SWAPPING VALUES
price_a = 1.50
price_b = 3.00
print("Before:",price_a,"and",price_b)

temp  =price_a
price_a = price_b
price_b = temp
print("After:",price_a,"and",price_b)