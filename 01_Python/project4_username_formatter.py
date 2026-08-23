print("--- Professional Username & Email Generator ---")

# step 1: inputs
first_name = input("Enter your first name: ")
last_name = input("Enput your last name: ")

# step 2 : string operations
full_name = first_name + " " + last_name
clean_name = full_name.lower().replace(" ", "_")
name_length = len(first_name) + len(last_name)

# step 3: output display
print("\n--- Generated Profile ---")
print("Full Name:", full_name.title())
print("Suggested Username:", clean_name + "_official")
print("Suggested Email:", clean_name + "@Company.com")
print("Total Letters in Name:", name_length)