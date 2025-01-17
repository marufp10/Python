# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
items_list = [1, 2, 3, 4, 5, 6]

# Find the length of the list
list_length = len(items_list)
print("List Length:", list_length)

# Get the first item, the middle item, and the last item of the list
first_item = items_list[0]
middle_item = items_list[len(items_list) // 2]
last_item = items_list[-1]

# Declare a list called mixed_data_types, (name, age, height, marital status, address)
mixed_data_types = ["Your Name", 28, 5.9, "Married", "123 Main Street"]

# Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Print the list of IT companies
print("IT Companies:", it_companies)

# Print the number of companies in the list
print ("Number of IT Companies:", len(it_companies))

# Print the first, middle, and last company
first_company= it_companies[0]
middle_company = it_companies[3]
last_company = it_companies[-1]

print("First company:", first_company)
print("Middle company:", middle_company)
print("Last company:", last_company)

# Modify one company
it_companies[1] = "Meta"
print(it_companies)



